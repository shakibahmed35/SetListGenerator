from bs4 import BeautifulSoup
import requests

def get_songs(url):

   
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')


    span_elements = soup.find_all(class_="songLabel")


    songs = [span.text for span in span_elements] 
    artist_name = input("Please Give Artists Name: ")
    return songs, artist_name

if __name__ == "__main__":
    url = input("Please Give URL of the Setlist from Setlist.fm: ")
    get_songs(url)
    
