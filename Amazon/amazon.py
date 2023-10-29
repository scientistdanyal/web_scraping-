import requests
from bs4 import BeautifulSoup
import pandas as pd

reviewlist = []

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 5})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'name ' : item.find('span', {'class': 'a-profile-name'}).text.strip(),
            # 'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').replace('Amazon.com: Customer reviews:', '').strip(),
            'title': item.find('a', {'data-hook': 'review-title'}).text[18:].strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            'date': item.find('span', {'data-hook': 'review-date'}).text.split()[-3:]
            }
            reviewlist.append(review)
    except:
        pass

for x in range(1,10):
    soup = get_soup(f'https://www.amazon.com/Kamado-Joe-KJ23RHC-Classic-Charcoal/product-reviews/B01INNA89S/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_excel('sony-headphones.xlsx', index=False)
print('Fin.')