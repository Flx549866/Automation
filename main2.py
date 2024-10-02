import os
import requests
from bs4 import BeautifulSoup

def scrape_view_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the specific view content container using its class
        view_content = soup.find('div', class_='faculty-entry')
        #view_content = soup.find('div', id='textcontainer',class_='page-content')
        # Check if the view content container is found
        if view_content:
            # Extract all text content within the container
            text_content = view_content.get_text(separator='\n').strip()
            return text_content
        else:
            print("View content container not found on the page.")
            return None
    else:
        print(f"Failed to fetch URL: {url}")
        return None

def main():
    # URL of the webpage containing the view content
   # url = "https://www.gse.harvard.edu/directory/faculty"
    url = "https://catalog.njit.edu/about-university/directory/faculty/"
    # Scrape the view content
    view_content = scrape_view_content(url)
    
    # Check if view content is scraped successfully
    if view_content:
        # Define the file path
        file_path = r"C:\Users\f3l1x\OneDrive\Desktop\Automation\professor.txt"
        
        # Write the scraped content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(view_content)
        
        print(f"Scraped content saved to: {file_path}")
    else:
        print("No view content scraped.")

if __name__ == "__main__":
    main()
