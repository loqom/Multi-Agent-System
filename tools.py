from langchain.tools import tool
import requests 
from dotenv import load_dotenv 
load_dotenv()
from tavily import TavilyClient
import os
from rich import print
from bs4 import BeautifulSoup


tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

out=[]

@tool
def web_search(query:str)->str:
    """search the web for recent and reliable information about topic.Returns title,url and snippets""" 
    result=tavily.search(query=query,max_results=5)
    for r in result['results']:
        out.append(
            f"Title:{r['title']}\n\n URL:{r['url']}\n\nSnippet:{r['content']}"
        )
    return "\n-----\n".join(out)



@tool
def scrape_text (url:str)->str:
    """Scrape and return clean text content from a given url for deeper reading"""
    try:
        resp=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        soup=BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"Error fetching url:{str(e)}"
    
