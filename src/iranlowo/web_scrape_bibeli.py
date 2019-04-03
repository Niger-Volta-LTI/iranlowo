# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import requests
import time

bib_books = dict()
bib_books['GEN'] = 50  # GEN.1.BMY --> GEN.50.BMY
bib_books['EXO'] = 40  # EXO.1.BMY --> GEN.40.BMY
bib_books['LEV'] = 27
bib_books['NUM'] = 36
bib_books['DEU'] = 34
bib_books['JOS'] = 24
bib_books['JDG'] = 21
bib_books['RUT'] = 4
bib_books['1SA'] = 31
bib_books['2SA'] = 24
bib_books['1KI'] = 22
bib_books['2KI'] = 25
bib_books['1CH'] = 29
bib_books['2CH'] = 36
bib_books['EZR'] = 10
bib_books['NEH'] = 13
bib_books['EST'] = 10
bib_books['JOB'] = 42
bib_books['PSA'] = 150
bib_books['PRO'] = 31
bib_books['ECC'] = 12
bib_books['SNG'] = 8
bib_books['ISA'] = 66
bib_books['JER'] = 52
bib_books['LAM'] = 5
bib_books['EZK'] = 48
bib_books['DAN'] = 12
bib_books['HOS'] = 14
bib_books['JOL'] = 3
bib_books['AMO'] = 9
bib_books['OBA'] = 1
bib_books['JON'] = 4
bib_books['MIC'] = 7
bib_books['NAM'] = 3
bib_books['HAB'] = 3
bib_books['ZEP'] = 3
bib_books['HAG'] = 2
bib_books['ZEC'] = 14
bib_books['MAL'] = 4
bib_books['MAT'] = 28
bib_books['MRK'] = 16
bib_books['LUK'] = 24
bib_books['JHN'] = 21
bib_books['ACT'] = 28
bib_books['ROM'] = 16
bib_books['1CO'] = 16
bib_books['2CO'] = 13
bib_books['GAL'] = 6
bib_books['EPH'] = 6
bib_books['PHP'] = 4
bib_books['COL'] = 4
bib_books['1TH'] = 5
bib_books['2TH'] = 3
bib_books['1TI'] = 6
bib_books['2TI'] = 4
bib_books['TIT'] = 3
bib_books['PHM'] = 1
bib_books['HEB'] = 13
bib_books['JAS'] = 5
bib_books['1PE'] = 5
bib_books['2PE'] = 3
bib_books['1JN'] = 5
bib_books['2JN'] = 1
bib_books['3JN'] = 1
bib_books['JUD'] = 1
bib_books['REV'] = 22


# generator which yields the appropriate bible strings
def bible_strings(prefix):
    for book in bib_books:
        # print(book, bib_books[book])
        for chapter in range(1, bib_books[book]+1):
            url_string = prefix + book + "." + str(chapter)
            # print(url_string)
            yield url_string


def scrape_chapter(url, bible_path):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    text = ""
    # Take out the <div> of name and get its value
    heading = soup.find_all('span', attrs={'class': 'heading'})

    # collect chapter heading
    try:
        text += heading[0].contents[0] + "."  # do we need headings, should these go to their own file?
        filename = bible_path + os.path.basename(url) + "/" + "heading.txt"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

    except IndexError:
        # print("IndexError @  " + url)
        text = ""

    verse_label = ""
    for spans in soup.find_all('span'):
        if 'data-usfm' in spans.attrs:
            if verse_label is not spans['data-usfm']:
                verse_label = spans['data-usfm']
            for item in spans.contents:
                if 'class' in item.attrs:
                    if item['class'][0] == 'content':
                        if len(item.text.strip()):
                            print(verse_label, item.text)
                            filename = bible_path + os.path.basename(url) + "/" + verse_label + ".txt"
                            os.makedirs(os.path.dirname(filename), exist_ok=True)
                            with open(filename, 'a', encoding='utf-8') as f:
                                f.write(item.text)
    return text


def get_bible_text(bible_version_url, bíbélì_dest_path):
    """English named convience method"""
    return rígba_bíbélì(bible_version_url, bíbélì_dest_path)


def rígba_bíbélì(bíbélì_version_url, bíbélì_dest_path):
    """
    Rígba ọ̀rọ̀ ìwé bíbélì - get Bíbélì Mímọ́, save files under bíbélì_path

    Parameters:
    argument1 (string): bible url,  i.e.: "https://www.bible.com/bible/911/")
    argument2 (string): bible_dest_path, where to save files, i.e.: "./bibeli_mimo_yoruba/

    Returns: None
    """

    for url_string in bible_strings(bíbélì_version_url):
            print("Rígba ọ̀rọ̀ ìwé " + url_string)
            blurb = scrape_chapter(url=url_string, bible_path=bíbélì_dest_path)
            time.sleep(5.5)
    return True


if __name__ == "__main__":

    # Bíbélì Mímọ́ ní Èdè Yorùbá Òde-Òní
    bíbélì_version = "https://www.bible.com/bible/911/"

    # Yorùbá Bible - Bible Society of Nigeria
    # bíbélì_version = "https://www.bible.com/bible/207/"

    # New International Version® NIV® - 2011 by Biblica, Inc.®
    # bíbélì_version = "https://www.bible.com/bible/111/"

    # King James Version (KJV)
    # bíbélì_version = "https://www.bible.com/bible/1/"

    bíbélì_path = "bibeli_mimo_yoruba_test/"
    rígba_bíbélì(bíbélì_version, bíbélì_path)
