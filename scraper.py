from bs4 import BeautifulSoup
import requests

url = input("Please Give URL of the Setlist from Setlist.fm")  
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')


span_elements = soup.find_all(class_="songLabel")


for span in span_elements:
    print(span.text)  
