import requests
from bs4 import BeautifulSoup

def scrape_view_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the specific text container using its class name
        text_container = soup.find('div', id='textcontainer', class_='page_content')
        
        # Check if the text container is found
        if text_container:
            # Extract the text content
            text_content = text_container.text.strip()
            
            return text_content
        else:
            print("Text container not found on the page.")
            return None
    else:
        print(f"Failed to fetch URL: {url}")
        return None

def main():
    url = "https://catalog.njit.edu/about-university/directory/faculty/"
    view_content = scrape_view_content(url)
    
    # Check if view content is scraped successfully
    if view_content:
        # Define the file path
        file_path = r"C:\Users\f3l1x\OneDrive\Desktop\Automation\professor_njit.txt"
        
        # Write the scraped content to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(view_content)
        
        print(f"Scraped content saved to: {file_path}")
    else:
        print("No view content scraped.")


if __name__ == "__main__":
    main()
