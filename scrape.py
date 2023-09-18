import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Amsterdam"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get all paragraphs
paragraphs = soup.find_all('p')

# Save the text content of each paragraph into a list
amsterdam_data = [para.text for para in paragraphs]

# Join the list elements to form a single string containing all data
amsterdam_text_data = ' '.join(amsterdam_data)

# Save the data to a text file
with open('amsterdam_data.txt', 'w', encoding='utf-8') as file:
    file.write(amsterdam_text_data)

