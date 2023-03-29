import requests as rq
import bs4 as BS4
from typing import List
from selenium import webdriver
from langdetect import detect
import requests
from bs4 import BeautifulSoup
from nltk import sent_tokenize
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from selenium.webdriver.common.by import By



def get_page(url: str) -> BS4.BeautifulSoup:
    page = rq.get(url)
    soup = BS4.BeautifulSoup(page.content, "html.parser")
    return soup


def get_all_links(url: str) -> List[str]:
    page = get_page(url)
    a = []
    # raw_events = page.findAll("a")
    # events = [event.get("href") for event in raw_events]
    for link in page.find_all('a'):
        if link.has_attr('href'):
            path = url
            a.append(path.replace("index.html", link.attrs['href']))
    # for event in events:
    #     if event.co
    return a


def check_all_textf(url: str) -> bool:
    page = get_page(url)
    raw_events = page.get_text()
    lang = detect(raw_events)
    print(get_language_percentages(url))
    ratio = get_language_percentages(url)
    print(float(ratio.get("hinglish") + ratio.get("nepali")))
    if float(ratio.get("hinglish") + ratio.get("nepali")) > 0.25:
        return True
    return False


def check_all_image(url: str) -> bool:
    # page = get_page(url)
    # test = []
    # count = 1
    # images = page.findAll('img')
    # for image in images:
    #     # Print image source
    #     if "blur" in image['src']:
    #         print(image['src'])
    #         return False
    # return True
    # Create a webdriver object and launch a browser
    driver = webdriver.Chrome()

    # Go to the website with images
    driver.get(url)

    # Find the image elements on the page
    images = driver.find_elements(By.TAG_NAME, 'img')


    count = 0
    c=0
    # Loop over the images and save them to the directory
    for image in images:
        c=c+1
        # Get the image source url
        src = image.get_attribute("src")
        if "blur" in src:
            print(src)
            # Close the browser
            count= count+1
    # Close the browser
    driver.close()

    if(count>c/2):
        return False
    return True

def get_language_percentages(url):
    # Scrape HTML content from a page using Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from HTML elements using Beautiful Soup
    text = soup.get_text()

    # Use NLTK to detect the language of each sentence in the text
    sentences = sent_tokenize(text)
    words = wordpunct_tokenize(text.lower())
    lang_ratios = {}
    tokens = words

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        lang_ratios[language] = len(common_elements)

    # Count the number of sentences in each language and calculate the percentage
    ratios_sum = sum(lang_ratios.values())
    for key in lang_ratios.keys():
        lang_ratios[key] /= ratios_sum

    return lang_ratios
