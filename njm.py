import oS
import bs4
import requests
from sys import *
from urllib.request import urlopen

def ImageURLScrapper(url):
 connection= urlopen(url)
 raw html = connection.read()
 connection.close()
 page_soup = bs4. BeautifulSoup(raw_html, "html.parser")
 container = page_soup.findAll("div",{"class":"item-container"})
 return container
def main():
 print("---- AVINASHMAHALE-----
 print("Application name : " +argv[0])
 if (len(argv) ==2):
  if (arqv[ 11 == "-h") or (argv[ 11 == "-H"):
   print("This Script is used to fetch URL of Images")
   exit()
  if (argv[1] == "-u") or (argv[1]== "-U")
print("usage : ApplicationName")
exit()
exit()
try:
url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20card"
listout = ImageURLScrapper(url)
print("urls of all images")
for elements in listout:
print(elements.a.img['data-src'])
except Exception as E:
print("Error: Invalid input",E)

if__name__=="__main__":
main() 