# name = //div[@class='product-main']//h6
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import requests
import json
import csv
from urllib.parse import urljoin
import random
import os,time
options = Options()
# options.add_argument("--headless")



def download_image(img_url, sku_name, color,folder_path):
    
    
    response = requests.get(f'{img_url}')
    image_name = f'sku-{sku_name}-{color}.jpg'
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, 'wb') as file:
            file.write(response.content)



def scrape_data():
    driver = webdriver.Chrome()
    
    # Replace the URL with the actual URL you want to visit
    urls = ['https://www.emser.com/products/stone-fusion','https://www.emser.com/products/agio','https://www.emser.com/products/catch-in-color']
    for url in urls:
        folder_name = f'folder_{random.randint(10000, 99999)}'
        folder_path = os.path.join('', folder_name)
        os.makedirs(folder_path, exist_ok=True)
        driver.get(url)
        product_name = driver.find_element(By.XPATH,'//h6').text
        print(product_name)
        product_description = driver.find_element(By.XPATH, '//*[@id="shopify-section-static-product"]/section/article/div[2]/div/div[2]//p[1]').text
        print(product_description)
        carousel = driver.find_element(By.CLASS_NAME, 'swatch-view')

        # Find all the li elements within the carousel
        li_elements = carousel.find_elements(By.TAG_NAME, 'li')
        i = 1
        # Iterate through each li element and click on it
        for li_element in li_elements:
            # Click on the li element
            color_name = li_element.get_attribute('aria-label')
            print(color_name)
            time.sleep(2)
            driver.execute_script("arguments[0].click();", li_element)
            time.sleep(1)
            sku_element = driver.find_element(By.XPATH, '/html/body/main/div[1]/section/article/div[2]/div/div[3]/div/form/div[2]/span').text
            print(sku_element)
            sku_img = driver.find_element(By.XPATH, "//div[@class='gallery-navigation--scroller starapps']//span//img").get_attribute('src')
            download_image(sku_img, sku_element, color_name,folder_path)
            # Wait for a short duration to allow the new image to appear (you might need to adjust the sleep time)
            

            # Add your logic here to scrape the information or download the image
            
            if (i==3):
                try:
                    driver.find_element(By.XPATH, '//*[@id="swatch-option1"]/div/fieldset/div/div/div[2]/div').click()
                    i = 1
                except:
                    pass
            i +=1
            
        save_csv([product_name, product_description, folder_name])

    # Close the browser
    driver.quit()




def save_csv(data):
    csv_file_path = 'output.csv'

    # Check if the file exists to determine if a header should be written
    file_exists = False
    try:
        with open(csv_file_path, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header only if the file is newly created
        if not file_exists:
            writer.writerow(['Product Name', 'Product Description', 'Folder Name'])

        # Write data to CSV
        writer.writerow(data)
    


scrape_data()