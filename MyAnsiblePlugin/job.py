#!/usr/bin/python3
import os
import requests
import bs4
from bs4 import BeautifulSoup
import time
class FilterModule(object):
  def filters(self):
     return {
       "job_filter": self.job_filter,
     }
  def job_filter(self, role):
    role = role.replace(" ", "+")
    URL =  "https://www.indeed.com/jobs?q={0}+%2420%2C000&l=Los+Angeles&start=10".format(role)
    #URL =  "https://www.indeed.com/jobs?q=devops+engineer+%2420%2C000&l=Los+Angeles&start=10"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    #print(soup.prettify())

    def extract_job_title_from_result(soup):
     jobs = []
     for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
     return(jobs)
    os.system("clear")
    time.sleep(1)
    os.system("tput setaf 5")
    print("The job titles are as follows : ")
    print("\n")
    os.system("tput setaf 2")
    time.sleep(2)
    print(extract_job_title_from_result(soup))
    print("\n")
    time.sleep(5)

    def extract_summary_from_result(soup):
     summaries = []
     spans = soup.findAll('div', attrs={'class': 'summary'})
     for span in spans:
        summaries.append(span.text.strip())
     return(summaries)
    os.system("tput setaf 5")
    print("Respective Job Descriptions : ")
    print("\n")
    time.sleep(2)
    os.system("tput setaf 2")
    print(extract_summary_from_result(soup))
    print("\n")
     print("\n")
    time.sleep(5)

    def extract_salary_from_result(soup):
     salaries = []
     for div in soup.find_all(name='div', attrs={'class':'row'}):
        try:
            salaries.append(div.find('nobr').text)
        except:
            try:
                div_two = div.find(name='div', attrs={'class':'sjcl'})
                div_three = div_two.find('div')
                salaries.append(div_three.text.strip())
            except:
                salaries.append('Nothing_found')
     return(salaries)
    os.system("tput setaf 5")
    print("The respective companies are as follows with ratings : ")
    print("\n")
    time.sleep(2)
    os.system("tput setaf 2")
    print(extract_salary_from_result(soup))
    print("\n")
    time.sleep(5)

    def extract_location_from_result(soup):
     locations = []
     spans = soup.findAll('span', attrs={'class': 'location'})
     for span in spans:
        locations.append(span.text)
     return(locations)
    os.system("tput setaf 5")
    print("The previously mentioned jobs are found in following locations respectively : ")
    print("\n")
    os.system("tput setaf 2")
    time.sleep(2)
    print(extract_location_from_result(soup))
    print("\n")
    os.system("tput setaf 7")
    time.sleep(6)
