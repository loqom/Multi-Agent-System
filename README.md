# Multi-Agent Research System

A Multi-Agent AI Research System built using **LangChain**, **LangGraph**, **Mistral AI**, **Tavily Search**, and **BeautifulSoup**. The system uses multiple AI agents to collaboratively search the web, scrape relevant content, generate a structured research report, and review the final output.

---

## Features

- Multi-Agent architecture using LangGraph
- Search Agent powered by Tavily Search API
- Reader Agent for web scraping using BeautifulSoup
- Writer Chain for generating structured research reports
- Critic Chain for reviewing and improving generated reports
- LCEL (LangChain Expression Language) based workflow
- Environment variable support using `.env`

---

## Tech Stack

- Python
- Mistral AI
- LangChain
- LangGraph
- Tavily Search API
- BeautifulSoup4
- Requests
- Python-dotenv

---

## Project Structure

```
multi-agent-system/
│
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/loqom/Multi-Agent-System.git
cd Multi-Agent-System
```

### Create a virtual environment

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Running the Project

```bash
python pipeline.py
```

Example:

```
Enter a research topic:
Artificial Intelligence in Healthcare
```

---

## Workflow

```
User Input
    │
    ▼
Search Agent
    │
    ▼
Tavily Search
    │
    ▼
Reader Agent
    │
    ▼
BeautifulSoup Scraper
    │
    ▼
Writer Chain
    │
    ▼
Research Report
    │
    ▼
Critic Chain
    │
    ▼
Final Report & Feedback
```

---

## Requirements

Major dependencies:

- langchain
- langgraph
- langchain-mistralai
- mistralai
- tavily-python
- beautifulsoup4
- requests
- python-dotenv

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- FastAPI backend
- React frontend
- Multi-source web scraping
- PDF report generation
- Memory support
- RAG integration
- Docker support
- Streaming responses

---

## License

This project is licensed under the MIT License.

---

## Author

**Om Vishwakarma**

GitHub: https://github.com/loqom

LinkedIn: https://linkedin.com/in/om-vishwakarma-stu
