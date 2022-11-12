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
        page = r.get((urlabadis), headers=headers, timeout=10)
        soup = BeautifulSoup(page.content, 'lxml')
        return soup

    def get_data_all_text_abadis(self, text: str) -> dict:
        ''' get data Persian equivalent , equivalent , Opposite , encyclopedia '''
        all_comment = []
        list_encyclopedia = []

        soup = Abadis().get_data_html(text)

        if soup.find("div", attrs={"class": "boxMain"}):
            html_boxMain = soup.find("div", attrs={"class": "boxMain"})

            # get equivalent
            try:
                equivalent = html_boxMain.find(
                    "b", string={f"مترادف {text}"}).next_sibling.strip(": ")
                equivalent = equivalent.replace(" ", "").split("،")
                equivalent = [re.sub(r'\W', '', remove)
                              for remove in equivalent]

            except:
                equivalent = None

            # get Opposite
            try:
                Opposite = html_boxMain.find(
                    "b", string={f"متضاد {text}"}).next_sibling.strip(": ").split("، ")
                Opposite = [re.sub(r'\W', '', remove) for remove in Opposite]
            except:
                Opposite = None

            # get Persian equivalen
            try:
                Persian_equivalent = html_boxMain.find(
                    "b", string={"برابر پارسی"}).next_sibling.strip(": ").split("، ")
                Persian_equivalent = [re.sub(r'\W', '', remove)
                                      for remove in Persian_equivalent]
            except:
                Persian_equivalent = None

            # get name encyclopedia
            if soup.find("div", {"t": "دانشنامه عمومی"}):
                html_encyclopedia = soup.find("div", {"t": "دانشنامه عمومی"})
                for list_text in html_encyclopedia.find_all("div", {"class": "wikilink"}):
                    text_encyclopedia = list_text.find("a").text
                    list_encyclopedia.append(text_encyclopedia)
            else:
                list_encyclopedia.append(None)

            # get the most liked comment
            try:
                html_comment = soup.find("div", {"id": "cmts"})
                # Find the number of likes
                number_list = re.findall(r"[l]..\d+", str(html_comment))
                replace = [list.replace('l=\"', '').strip()
                           for list in number_list]

                # The most number of likes
                maxnumber = max(replace, key=lambda value: int(value))
                get_the_most_liked_comment = html_comment.find(
                    "div", {"l": maxnumber}).text
            except:
                get_the_most_liked_comment = None

            # comments
            if soup.find_all("div", {"class": "cmt"}):
                html_comments = soup.find_all("div", {"class": "cmt"})
                try:
                    for all in html_comments:
                        all = all.text
                        all_comment.append(all)
                except:
                    pass
            else:
                all_comment.append(None)

        else:
            return None

        return {"مترادف": equivalent,
                "متضاد": Opposite,
                "برابر": Persian_equivalent,
                "دانشنامه عمومی": list_encyclopedia,
                "بیشترین کامند لایک شده": get_the_most_liked_comment,
                "کامنت": all_comment
                }