from flask import Flask, Response, request
from flask_cors import CORS
from agents import search_agent, read_agent, writer_chain, critic_chain
import json

app = Flask(__name__)
CORS(app)

@app.route('/research')
def research():
    topic = request.args.get('topic', '')
    if not topic:
        return {'error': 'No topic provided'}, 400

    def stream():
        state = {}
        try:
            yield f"data: {json.dumps({'stage': 'search', 'status': 'active'})}\n\n"
            search = search_agent()
            result = search.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
            })
            state['search_results'] = result['messages'][-1].content
            yield f"data: {json.dumps({'stage': 'search', 'status': 'done', 'data': state['search_results']})}\n\n"

            yield f"data: {json.dumps({'stage': 'reader', 'status': 'active'})}\n\n"
            read = read_agent()
            result = read.invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results'][:800]}"
                )]
            })
            state['scraped_content'] = result['messages'][-1].content
            yield f"data: {json.dumps({'stage': 'reader', 'status': 'done'})}\n\n"

            yield f"data: {json.dumps({'stage': 'writer', 'status': 'active'})}\n\n"
            research_combined = (
                f"SEARCH RESULTS:\n{state['search_results']}\n\n"
                f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
            )
            state['report'] = writer_chain.invoke({
                "topic": topic,
                "research": research_combined
            })
            yield f"data: {json.dumps({'stage': 'writer', 'status': 'done'})}\n\n"

            yield f"data: {json.dumps({'stage': 'critic', 'status': 'active'})}\n\n"
            state['feedback'] = critic_chain.invoke({
                "report": state['report']
            })
            final = f"{state['report']}\n\n---\n\n🔍 Critic Review:\n{state['feedback']}"
            yield f"data: {json.dumps({'stage': 'critic', 'status': 'done', 'data': final})}\n\n"
            
        except Exception as e:
            # Send an error event back to the client if something fails
            yield f"event: error\ndata: {json.dumps({'error': str(e)})}\n\n"

    return Response(stream(), mimetype='text/event-stream',
                    headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)