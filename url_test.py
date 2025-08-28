import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/india-celebrates-77th-independence-day/article67195627.ece"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    article_text = " ".join([p.get_text() for p in paragraphs])

    print("Extracted News Text:\n")
    print(article_text[:1000])  # print first 1000 characters
else:
    print("Failed to fetch article. Status code:", response.status_code)
