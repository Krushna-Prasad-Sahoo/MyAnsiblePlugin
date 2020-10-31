#!/usr/bin/python3
from newspaper import Article
import nltk
nltk.download('punkt')
import os
import time
class FilterModule(object):
  def filters(self):
     return {
       "news_filter": self.news_filter,
     }
  def news_filter(self, url):
    article = Article(url, language="en") # en for English
    article.download()
    article.parse()
    article.nlp()

    os.system("clear")
    os.system("tput setaf 3")
    print("-------------------- Article Title --------------------")
    time.sleep(2)
    os.system("tput setaf 6")
    print(article.title) #prints the title of the article
    print("\n")
    time.sleep(1)
    os.system("tput setaf 3")
    print("-------------------- Article Text--------------------")
    time.sleep(2)
    os.system("tput setaf 6")
    print(article.text) #prints the entire text of the article
    print("\n")
    time.sleep(1)
    os.system("tput setaf 3")
    print("-------------------- Article Summary --------------------")
    os.system("tput setaf 6")
    time.sleep(2)
    print(article.summary) #prints the summary of the article
    os.system("tput setaf 7")
    print("\n")
