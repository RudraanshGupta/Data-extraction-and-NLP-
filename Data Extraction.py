import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import os

# Loading the URLs from the input Excel file
input_file = 'Input.xlsx'
output_folder = 'scraped_articles'  # Folder to save titles and article text

# Creating output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loading the input Excel file into a DataFrame
df = pd.read_excel(input_file)

# Function to extract title and article text 
async def fetch_title_and_article(session, url, url_id):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                # Extracting the title
                title = soup.find('title').get_text() if soup.find('title') else 'No Title'

                # Extracting article text
                article = soup.find('article')
                if article:
                    article_text = article.get_text()
                else:
                    # Fallback to paragraphs if 'article' tag doesn't exist
                    article_text = '\n'.join([p.get_text() for p in soup.find_all('p')])

                # Saving the title to a text file
                title_file_path = os.path.join(output_folder, f"{url_id}_title.txt")
                with open(title_file_path, 'w', encoding='utf-8') as title_file:
                    title_file.write(title)

                # Saving the article text to a text file
                article_file_path = os.path.join(output_folder, f"{url_id}_article.txt")
                with open(article_file_path, 'w', encoding='utf-8') as article_file:
                    article_file.write(article_text)

                print(f"Successfully extracted title and article for {url_id}")
            else:
                print(f"Failed to fetch URL: {url} with status code: {response.status}")
    
    except Exception as e:
        print(f"Error extracting data from {url}: {e}")
