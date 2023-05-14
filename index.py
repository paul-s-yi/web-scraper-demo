import requests
import csv
import time
import random
from bs4 import BeautifulSoup

# Creates file (or will just add to file if it already exists)
spec_file = open('specs.csv','w',newline='')
spec_fields = []

def get_page(url):
  # Forces program to wait between 5 and 10 seconds before accessing new page on site. Need this to avoid website denying access due to Too Many Requests
  sleep_secs = random.randint(5,10)
  time.sleep(sleep_secs) 
  return requests.get(url)

def link_grabber(models):
  # Loop through each device model and check if it is an iPhone (there are some iPads and Watches mixed in)
  for model in models:
    name = model.find('a').text.strip()
    if 'iPhone' in name:
      link = 'https://www.gsmarena.com/' + model.find('a')['href']
      response = get_page(link)
      soup = BeautifulSoup(response.content, 'html.parser')
      release_date = soup.find('span',{"data-spec": "released-hl"}).contents[0]
      print(release_date)
      specs_list = soup.find('div', id = 'specs-list')
      print(name,link)
      # spec_file.write



# Define the URL to scrape
base_url = 'https://www.gsmarena.com/'

# Send a GET request to the URL and store the response
response = get_page(base_url + 'apple-phones-48.php')

# Create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')
models = soup.find_all('li')
link_grabber(models)

# Find the different pages' endpoints and place them inside list
page_soup = soup.find('div', class_='nav-pages').find_all('a')
page_list = []
for page in page_soup:
    page_list.append(page.get('href'))

for endpoint in page_list:
  response = requests.get(base_url + endpoint)
  soup = BeautifulSoup(response.content, 'html.parser')
  # Find all the phone models listed on the page
  models = soup.find_all('li')
  link_grabber(models)

