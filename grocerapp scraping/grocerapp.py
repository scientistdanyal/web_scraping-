import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import schedule
import threading


# scraping function 
def scrape_category(category_link):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    products = []
    
    try:
        driver.get(category_link)
         
        
        # Extract category name
        my_list = category_link
        my_list=my_list.split('/')
    
        category_name = my_list[-2]

        timeout = 20

        # Wait for the product elements to be present
        product_elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'MuiGrid-root')]/p[contains(@class, 'MuiTypography-body1')]")))

        # Wait for the product quantity elements to be present
        product_quantity_elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='MuiTypography-root MuiTypography-caption']")))

        # Wait for the product price elements to be present
        product_price_elements = WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-subtitle2")))

        # Loop through product elements and extract data
        for name_element, quantity_element, price_element in zip(product_elements, product_quantity_elements, product_price_elements):
            product_name = name_element.text
            product_quantity = quantity_element.text
            product_price = price_element.text
            print(product_name,product_quantity,product_price)
            
            products.append({
                "category": category_name,
                "name": product_name,
                "quantity": product_quantity,
                "price": product_price,
                "date": time.strftime("%Y-%m-%d")
            })

        
    except Exception as e:
        print(f"An error occurred while processing category {category_link}: {e}")
    
    finally:
        driver.quit()
    
    return products





def run_scraping_job():
    print("Running scraping job...")
    # Configure Chrome WebDriver options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

    url = "https://grocerapp.pk/categories"
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(10)

    # Find the container that holds the category links
    category_buttons_container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div[1]/div[2]/div")))
    category_buttons = category_buttons_container.find_elements(By.CSS_SELECTOR, "a")

    # Store the links in a list
    category_links = [button.get_attribute("href") for button in category_buttons]
    print(category_links)

    max_threads = 8



    # Initialize the thread pool
    all_products = []
    with ThreadPoolExecutor(max_threads) as executor:
        for products in executor.map(scrape_category, category_links):
            all_products.extend(products)

    # Save data to CSV file
    csv_file = "./Catagories_groccer_data.csv"
    if os.path.exists(csv_file):
        # If the CSV file exists, open it in append mode
        with open(csv_file, "a", newline="", encoding="utf-8") as file:
            # Use the same CSV writer code you have to append data
            fieldnames = ["category", "name", "quantity", "price", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(all_products)
    else:
        with open(csv_file, "a", encoding="utf-8") as file:
    # Use the same CSV writer code you have to append data
            fieldnames = ["category", "name", "quantity", "price", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows(all_products)

    
schedule.every().day.at("16:03").do(run_scraping_job)

# This function keeps the script running so that the scheduled job can be executed
def run_continuously():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start a separate thread to run the schedule
schedule_thread = threading.Thread(target=run_continuously)
schedule_thread.start()

# Keep the main thread running
while True:
    time.sleep(1)
