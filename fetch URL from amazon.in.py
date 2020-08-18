import os
import bs4
import requests
from sys import*
from urllib.request import urlopen
def URLScrapper(url):
 Connection = urlopen(url)
 raw_html = connection.read()
 connection.close()
 page_soup = bs4.BeautifulSoup(raw_html, "html.parser")
 container = page_soup.findAll("a", {"class":"a-link-normal a-text-normal"})
 return container

def main():
 print("--- AVINASH MAHALE---")
 print("Application name : " +argv[0])

 if (len(argv) == 2):
  if (argv[1] == "-h") or (argv[ 1] == "-H"):
   print("This Script is used to fetch URL")
   exit()

if (argv[ 1] == "-U") or (argv[ 1] =="-U"):
 print("usage : ApplicationName")
 exit()
try:
 url = "https://www.amazon. in/s?k=macbook&ref=nb_sb_noss"
 listout = URLScrapper(url)
 print("URL from website is :")
 for elements in listout:
  print(elements['href'])
  print()
except Exception as E:
 print("Error: Invald input",E)



if __name__=="__main__":
  main()




  Automation script which fetch URL from amazon.in using beautiful soap