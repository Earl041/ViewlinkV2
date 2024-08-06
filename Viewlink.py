import aiohttp
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
from time import sleep

# Tetapan untuk Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

# Satu User-Agent sahaja
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/91.0.4472.124 Safari/537.36"

async def open_url(url):
    # Mulakan sesi HTML dengan aiohttp
    async with aiohttp.ClientSession() as session:
        headers = {'User-Agent': user_agent}
        async with session.get(url, headers=headers) as response:
            print(f"Opened {url} with status code {response.status}")
            # Tunggu beberapa saat untuk mensimulasikan tindakan manusia melihat iklan
            await asyncio.sleep(random.uniform(3, 7))

    # Buka Chrome dengan Selenium untuk simulasi klik
    driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=chrome_options)
    driver.get(url)
    
    # Tunggu sehingga elemen klik dapat dilihat
    sleep(random.uniform(3, 7))  # Simulasikan menunggu

    try:
        # Klik butang "Click Here To Your Link Destination"
        button = driver.find_element(By.XPATH, '//*[@id="makingdifferenttimer"]')
        button.click()
        print("Clicked the button")
    except Exception as e:
        print(f"Failed to click the button: {e}")
    finally:
        driver.quit()

    # Tunggu lagi untuk simulasi manusia melihat iklan
    await asyncio.sleep(random.uniform(3, 7))

async def main(url, count):
    tasks = [open_url(url) for _ in range(count)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    url = input("Please enter the URL to be accessed: ")
    count = 500000  # Bilangan kali untuk membuka URL
    asyncio.run(main(url, count))
