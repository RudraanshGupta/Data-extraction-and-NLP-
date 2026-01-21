# Data-extraction-and-NLP

# Automated Web Scraping & Textual Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![NLTK](https://img.shields.io/badge/NLTK-Natural_Language_Processing-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📋 Overview

This project implements a robust pipeline for **automated data extraction** and **linguistic analysis**. It is designed to iterate through a list of URLs, extract article content while excluding boilerplate HTML, and perform in-depth textual analysis to compute various readability and sentiment metrics.

The solution is split into two modular components:
1.  **Data Extraction:** Scrapes article titles and body text from provided URLs.
2.  **Data Analysis:** Processes the extracted text to calculate metrics such as Gunning Fog Index, Polarity Score, Subjectivity Score, and other linguistic attributes.

---

## 📑 Table of Contents

* [Project Architecture](#-project-architecture)
* [Features](#-features)
* [Prerequisites](#-prerequisites)
* [Installation & Setup](#-installation--setup)
* [Usage Guide](#-usage-guide)
* [Output Metrics Explained](#-output-metrics-explained)
* [File Structure](#-file-structure)

---

## 🏗 Project Architecture

The pipeline follows a linear execution flow:

1.  **Input Ingestion:** Reads `Input.xlsx` containing a list of `URL_ID` and `URL`.
2.  **Web Scraping (`Data Extraction.py`):**
    * Requests the webpage content.
    * Parses HTML using BeautifulSoup.
    * Cleans data (removes headers, footers, and navigation).
    * Saves individual text files named by `URL_ID`.
3.  **NLP Analysis (`DataAnalysis.py`):**
    * Reads the saved text files.
    * Loads stop words and master dictionaries (Positive/Negative).
    * Tokenizes and cleans text.
    * Computes linguistic variables.
4.  **Data Export:** Saves the calculated metrics into `Output Data Structure.xlsx`.

---

## 🚀 Features

* **Robust Scraping:** Handles HTML parsing efficiently to isolate article text.
* **Sentiment Analysis:** Determines if the text is positive, negative, or neutral using custom dictionaries.
* **Readability Scoring:** Calculates the **Gunning Fog Index** to determine the complexity of the text.
* **Linguistic Metrics:** Computes average sentence length, complex word count, syllable count, and personal pronoun usage.
* **Batch Processing:** Capable of handling large datasets of URLs via Excel input.

---

## ⚙ Prerequisites

Ensure you have **Python 3.x** installed. The project relies on the following external libraries:

* `pandas` (Data manipulation)
* `requests` (HTTP requests)
* `beautifulsoup4` (HTML parsing)
* `nltk` (Natural Language Toolkit)
* `openpyxl` (Excel file I/O)

---

## 💻 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/RudraanshGupta/Data-extraction-and-NLP-.git](https://github.com/RudraanshGupta/Data-extraction-and-NLP-.git)
    cd Data-extraction-and-NLP-
    ```

2.  **Install Dependencies**
    ```bash
    pip install pandas requests beautifulsoup4 nltk openpyxl
    ```

3.  **Prepare Auxiliary Files**
    Ensure the following support files (for stop words and sentiment dictionaries) are present in the directory (if required by `DataAnalysis.py`):
    * `StopWords_Generic.txt` (and other stop word files)
    * `MasterDictionary` folder (containing positive/negative word lists)

---

## 🕹 Usage Guide

### Step 1: Data Extraction
Run the extraction script to scrape the articles from the URLs listed in `Input.xlsx`.

```bash
python "Data Extraction.py"
