import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://www.gsmarena.com/apple-phones-48.php'

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the phone models listed on the page
models = soup.find_all('li')
# print(models)
# Loop through each phone model and print the name and link
for model in models:
    name = model.find('a').text.strip()
    if 'iPhone' in name:
      link = 'https://www.gsmarena.com/' + model.find('a')['href']
      print(name, link)