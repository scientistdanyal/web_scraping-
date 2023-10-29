import requests
from bs4 import BeautifulSoup
import pandas as pd

reviewlist = []

def get_soup(url):
    try:
        r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 5}, timeout=10)  # Add timeout here
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass

for x in range(1, 10):
    soup = get_soup(f'https://www.amazon.com/Kamado-Joe-KJ23RHC-Classic-Charcoal/product-reviews/B01INNA89S/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    if soup:
        get_reviews(soup)
        print(len(reviewlist))
    else:
        print("Error scraping the page.")
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_excel('kamado-joe-reviews.xlsx', index=False)  # Adjust the file name as needed
print('Fin.')
