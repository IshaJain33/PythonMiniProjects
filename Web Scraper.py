''' install beautifulsoup4 by using below command - if not installed
pip install requests beautifulsoup4'''
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract all headings (<h2> tags as an example)
        headings = soup.find_all("h2") 
        print("\nExtracted Headings from the Page:")
        for idx, heading in enumerate(headings, 1):
            print(f"{idx}. {heading.text.strip()}")
        
        # Extract all links (<a> tags)
        links = soup.find_all("a", href=True)
        
        print("\nExtracted Links from the Page:")
        for idx, link in enumerate(links[:10], 1):  # Display only first 10 links
            print(f"{idx}. {link['href']}")
    
    else:
        print("Failed to retrieve the webpage. Check the URL or your connection.")
website_url = input("Enter the website URL to scrape: ")

scrape_website(website_url)
