from bs4 import BeautifulSoup
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://abadis.ir/'
}

r = requests.Session()


class abadis:
    '''دریافت متن از سایت آبادیس'''

    def __init__(self, text=None, listtext=None):
        self.text = text
        self.listtext = listtext

    def get_data_html(self, text: str) -> str:
        ''' دریافت html '''
        urlabadis = f"https://abadis.ir/fatofa/{text}"
        page = r.get((urlabadis), headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        return soup

    def equivalent_text(self, text: str) -> str:
        '''
        دریافت کلمات برابر پارسی

        '''
        soup = abadis().get_data_html(text)
        if soup.find("div", attrs={"class": "boxMain"}):
            result_nameleg = soup.find("div", attrs={"class": "boxMain"})
            try:
                barbar = result_nameleg.find(
                    "b", string={"برابر پارسی"}).next_sibling.strip(": ")
                barbar = barbar.replace("، ", "|")
                barbar = barbar.replace(" ", "")
            except:
                barbar = None
        else:
            barbar = None

        return barbar

    def general_encyclopedia(self, text: str) -> str:
        '''
        دریافت دانشنامه عمومی

        '''
        p = []
        soup = abadis().get_data_html(text)
        if soup.find("div", attrs={"t": "دانشنامه عمومی"}):
            s = soup.find("div", attrs={"t": "دانشنامه عمومی"})
            for ddd in s.find_all("div", attrs={"class": "wikilink"}):
                ddd = ddd.find("a").text
                p.append(ddd)
        else:
            return None
        return p

    def comment(self, text: str) -> str:
        '''
        مشاهده کامنت که بیشترین لایک داره

        '''
        soup = abadis().get_data_html(text)
        s = soup.find("div", {"id": "cmts"})
        text_hrml = str(s)

        number_list = re.findall(r"[l]..\d+", text_hrml)
        replace = [list.replace('l=\"', '').strip() for list in number_list]
        maxnumber = max(replace, key=lambda value: int(value))
        return s.find("div", {"l": maxnumber}).text

    def equivalent_list(self, listtext: list) -> list:
        '''
        ورودی لیست و خروجی لیست 
        دریافت کلمات برابر پارسی

        '''
        listbarbar = []
        for listtexts in listtext:
            soup = abadis().get_data_html(listtexts)
            if soup.find("div", attrs={"class": "boxMain"}):
                result_nameleg = soup.find("div", attrs={"class": "boxMain"})
                try:
                    barbar = result_nameleg.find(
                        "b", string={"برابر پارسی"}).next_sibling.strip(": ")
                    barbar = barbar.replace("، ", "|")
                    barbar = barbar.replace(" ", "")
                    listbarbar.append(barbar)
                except:
                    listbarbar.append("None")
            else:
                listbarbar.append("None")

        return listbarbar
