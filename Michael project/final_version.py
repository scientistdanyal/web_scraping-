from bs4 import BeautifulSoup
import datetime
import requests
import time
import csv
from tecsting import inner_data


def main():
    page = 1
    while True:
        url = f'https://uia.org/ybio?page={page}'
        response = requests.get(url)
        time.sleep(2)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.select('tbody tr')

            for element in elements:
                name = element.select_one('td h3').text
                name = name.replace('\n', '')
                inner_url = element.select_one('td h3 a')['href']
                acrony_element = element.select_one('td:nth-of-type(2)')
                acrony_text = acrony_element.text.strip()
                founded = element.select_one('td:nth-of-type(3)').text.strip()
                city_hq = element.select_one('td:nth-of-type(4)').text.strip()
                country = element.select_one('td:nth-of-type(5)').text.strip()
                type_1 = element.select_one('td:nth-of-type(6)').text.strip()
                type_2 = element.select_one('td:nth-of-type(7)').text.strip()
                uia_id = element.select_one('td:nth-of-type(8)').text.strip()
                inner_data(name, inner_url, acrony_text, founded, city_hq,country,type_1,type_2,uia_id)
                
        page +=1
        if (page == 1080):
            break
            # Add code to extract other data as needed




if __name__=='__main__':
    main()