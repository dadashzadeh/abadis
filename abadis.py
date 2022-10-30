from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://abadis.ir/'
}

r = requests.Session()


class Abadis:
    '''Receive text from Abadis site'''

    def __init__(self, text=None, list_text=None):
        self.text = text
        self.list_text = list_text

    def get_data_html(self, text: str) -> str:
        urlabadis = f"https://abadis.ir/fatofa/{text}"
        page = r.get((urlabadis), headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        return soup

    def get_equivalent_persian_text(self, text: str) -> str:
        soup = Abadis().get_data_html(text)
        
        if soup.find("div", {"class": "boxMain"}):
            html_content = soup.find("div", {"class": "boxMain"})
            try:
                equivalent = html_content.find(
                    "b", string={"برابر پارسی"}).next_sibling.strip(": ")
                equivalent_replace = equivalent.replace("، ", "|")
                equivalent_text = equivalent_replace.replace(" ", "")
            except:
                return None
        else:
            return None

        return equivalent_text

    def get_general_encyclopedia(self, text: str) -> str:
        list_encyclopedia = []
        
        soup = Abadis().get_data_html(text)
        if soup.find("div", {"t": "دانشنامه عمومی"}):
            html_content = soup.find("div", {"t": "دانشنامه عمومی"})
            for list_text in html_content.find_all("div", {"class": "wikilink"}):
                text_encyclopedia = list_text.find("a").text
                list_encyclopedia.append(text_encyclopedia)
        else:
            return None

        return list_encyclopedia

    def get_the_most_liked_comment(self, text: str) -> str:
        soup = Abadis().get_data_html(text)
        html_content = soup.find("div", {"id": "cmts"})

        # Find the number of likes
        number_list = re.findall(r"[l]..\d+", str(html_content))
        replace = [list.replace('l=\"', '').strip() for list in number_list]
        
        # The most number of likes
        maxnumber = max(replace, key=lambda value: int(value))
        return html_content.find("div", {"l": maxnumber}).text

    def get_equivalent_persian_list(self, list_text: list) -> list:
        equivalent_persian_list = []

        for list_texts in list_text:
            soup = Abadis().get_data_html(list_texts)
            if soup.find("div", {"class": "boxMain"}):
                html_content = soup.find("div", {"class": "boxMain"})
                try:
                    equivalent_list = html_content.find(
                        "b", string={"برابر پارسی"}).next_sibling.strip(": ")
                    equivalent_replace = equivalent_list.replace("، ", "|")
                    equivalent_replace = equivalent_replace.replace(" ", "")
                    equivalent_persian_list.append(equivalent_replace)
                except:
                    equivalent_persian_list.append("None")
            else:
                equivalent_persian_list.append("None")

        return equivalent_persian_list
