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
