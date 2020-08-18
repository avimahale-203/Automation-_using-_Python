import os
import bs4
import requests
from sys import*
def LinksDisplay(URL):
 res = requests.get(URL)
 print(type(res))
 soup = bs4.BeautifulSoup(res.text,Txml')
 print(type(soup)
 links = soup.find_all('a', href = True)
 return links
def main():
 print("-- hi avinash mahale--
 print("Application name :" +argv[0])
 if (len(argv) == 2):
  if (argv[1] =="-h") or (argv(1]="-H"):
   print("This Script is used to fetch links from wikipedia fle)
   exit()
 if (argv[ 1] a= "-u") or (argv[1] == "-U"):
  print("usage : ApplcationName")
  exit()

 try:
  url = "https://www.neweqg.com/Video-Cards-Video-Devices/Cateqgory/ID-387Tpkzvideo%20crd"1
  listout = ImageURLScrapper(url)
  print("Urls of all images")
for elements in listout:
 print(elements.a.img['data-src'l)
except Exception as E:
 print("Error : Invalid input",E)

if __name__=="__main__":
  main() 














Automation script which fetch url of all img using beautiful soup