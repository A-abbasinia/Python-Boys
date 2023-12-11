from googlesearch import search
import requests
from bs4 import BeautifulSoup

def search_google(question):
    query = question + " site:wikipedia.org"
    search_results = list(search(query, num_results=1, lang="fa"))
    if search_results:
        page_url = search_results[0]
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        description = soup.find("p").text.strip() if soup.find("p") else ""
        return description, page_url
    else:
        return "", ""

# مثال استفاده
question = input("لطفاً سوال خود را وارد کنید: ")
description, link = search_google(question)
print("متن توضیح: ", description)
print("لینک: ", link)
