# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:35:23 2023

@author: HP
"""

# Google Scholar SearchBar Scraping 

from bs4 import BeautifulSoup
import requests 

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


url = 'https://scholar.google.co.in/scholar?hl=en&as_sdt=0%2C5&as_ylo=2023&as_vis=1&q=offshore+wind+india&btnG='
#<a href="/citations?view_op=view_citation&amp;hl=en&amp;user=9SBYirYAAAAJ&amp;citation_for_view=9SBYirYAAAAJ:u5HHmVD_uO8C" class="gsc_a_at">The HIPASS catalogue—III. Optical counterparts and isolated dark galaxies</a>
response = requests.get(url,headers=headers)

soup=BeautifulSoup(response.content,'lxml')

soup.select('')

################# AUTHOR CODE 

require 'google_search_results' 

params = {
  engine: "google_scholar_author",
  hl: "en",
  author_id: "znb3ckwAAAAJ",
  api_key: "secret_api_key"
}

search = GoogleSearch(params)
hash_results = search.get_hash

##############

# Google Scholar Author Scraping 
import pandas as pd

from serpapi import GoogleSearch

import os,json

from urllib.parse import urlsplit, parse_qsl 

def ws_google_scholar_authour():
    # 
    params = {
      engine: "google_scholar_author", # key
      hl: "en", 
      author_id: "znb3ckwAAAAJ",
      api_key: "secret_api_key"
    }
    search = GoogleSearch.new(params)
    hash_results = search.get_hash
    
    author_research_data = {
        "author_data":{},
        "author_articles":[]
    }
    
    author_research_data["author_data"] ["name"]=hash_results.get("author").get("name")
    author_research_data["author_data"] ["email"]=hash_results.get("author").get("email")
    author_research_data["author_data"] ["websites"]=hash_results.get("author").get("websites")
    author_research_data["author_data"] ["interests"]=hash_results.get("author").get("interests")
    author_research_data["author_data"] ["affiliations"]=hash_results.get("author").get("affiliations")
    author_research_data["author_data"] ["thumbnail"]=hash_results.get("author").get("thumbnail")
    
    author_research_data["author_data"] ["cited_by_table"]=hash_results.get("cited_by",{}).get("table")
    author_research_data["author_data"] ["cited_by_graph"]=hash_results.get("cited_by",{}).get("graph")
   
    author_research_data["author_data"] ["public_access_link"]=hash_results.get("public_access",{}).get("link")
    author_research_data["author_data"] ["public_access_available"]=hash_results.get("author",{}).get("available")
    author_research_data["author_data"] ["public_access_not_available"]=hash_results.get("author",{}).get("not_available")
    author_research_data["author_data"] ["thumbnail"]=hash_results.get("author",{}).get("thumbnail")
    
    # extracting all articles pubhlished by the author 
    
    while True:
        results = search.get_dict()
        
        for article in results.get("articles",[]):
            print(f"Extracting article : {article.get('title')}")
            
            author_research_data['author_articles'].append()({
                "article_title":article.get('title'),
                "article_link":article.get('link'),
                "article_citation_id":article.get('citation_id'),
                "article_authors":article.get('authors'),
                "article_publication":article.get('publication'),
                "article_value":article.get("cited_by",{}).get("value"),
                "article_cited_by_value":article.get("cited_by",{}).get("link"),
                "article_link":article.get("cited_by",{}).get("cites_id"),
                "article_publication":article.get('year')
                })


        if "next" in results.get("serpapi_pagination",[]):
            search.params_dict.update(dict(parse_qsl(urlsplit(hash_results.get("serpapi_pagination").get("next")).query)))
        else:
            break 
    
    print(json.dumps(author_research_data,indent=2,ensure_ascii=False))
    print(f"Done. Extracted{len(author_research_data['author_articles'])-1}articles.") # counts an extra -1 line
    
    # Give article to csv 
    #CG_author_articles.csv
    pd.DataFrame(data=author_research_data["author_articles"]).to_csv(
        f"{author_research_data['author_data']['name'].lower().replace(' ','_')}_author_articles.csv",
        encoding = 'utf-8'
        )
    
    return author_research_data


ws_google_scholar_authour   

os.getcwd()
    


