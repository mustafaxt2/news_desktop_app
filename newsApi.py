import requests

class NewsApi:
    newsList=[]
    tempList=[]
    def __init__(self) -> None:
        self._url="https://newsapi.org/v2/top-headlines?"
        self._apiKey="96d4893062974f74ab84841ce82c5096"
        self._country="us"

    def get_news(self,category,liste):
        NewsApi.newsList=[]
        response=requests.get(self._url,params={"apiKey":self._apiKey, "country":self._country ,"category":category})
        news=response.json()["articles"]
        
        for new in news:
            liste.append(new["title"])
            liste.append(new["url"])
        NewsApi.tempList=liste
        
news=NewsApi()