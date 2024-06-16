from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r'C:\\Users\\mathi\AppData\\Local\\Microsoft\\WindowsApps\\geckodriver.exe')

driver = webdriver.Firefox(service=service)
driver.get('https://www.tui.no/?agent=googleads&utm_medium=paidsearch&utm_source=google&gad_source=1&gclid=CjwKCAjwmrqzBhAoEiwAXVpgokAlDZUigmS1D0NXjjTSKBlQJhof3RKWUpNRsWq9WhLI1iZTU8J6KxoCWzsQAvD_BwE&gclsrc=aw.ds')

def Search():
    accept_cookie = driver.find_element(By.ID, 'cmCloseBanner')
    accept_cookie.click()

    departure_airport = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/tui-choice-search-panel/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/input')
    departure_airport.click()
    time.sleep(1)

    departure_airport_checkbox = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/section/div/div/div/div/div[1]/div[2]/ul/li')
    departure_airport_checkbox.click()
    time.sleep(1)

    finish = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/footer/div/div/span/button')
    finish.click()
    time.sleep(1)

    try:
        popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'primeForPushModalContent'))
        )

        button = popup.find_element(By.ID, 'primeForPushDecline')
        button.click()

        print('Button clicked successfully.')
    except Exception as e:
        print('Popup or button not detected:', e)

    destination_options = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/tui-choice-search-panel/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/span[1]')
    destination_options.click()
    time.sleep(1)

    destination = driver.find_element(By.XPATH, '/html/body/div[4]/section/div/div/div/section/div/div/div/div/div[1]/div/ul/li[23]/a')
    destination.click()
    time.sleep(3)

    dest1 = driver.find_element(By.XPATH, '/html/body/div[4]/section/div/div/div/section/div/div/div/div/div[2]/div/div[4]/div[1]/div/label/span[2]')
    dest2 = driver.find_element(By.XPATH, '/html/body/div[4]/section/div/div/div/section/div/div/div/div/div[2]/div/div[8]/div[1]/div/label/span[2]')
    dest1.click()
    dest2.click()
    
    departure_date = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/tui-choice-search-panel/div/div/div/div/div[2]/div[1]/div/div/div[3]/div/div/div/input')
    departure_date.click()
    time.sleep(1)

    date_dropdown = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div/div/section/div/div/div/div/div[1]/div[1]/div/div/select')
    date_dropdown.click()
    time.sleep(1)

    month = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div/div/section/div/div/div/div/div[1]/div[1]/div/div/select/option[4]')
    month.click()
    time.sleep(1)

    date = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div/div/section/div/div/div/div/div[1]/div[2]/table/tbody/tr[4]/td[6]')
    date.click()    

    flexible_date = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div/div/section/div/div/div/div/div[2]/ul/li[1]/label/span[1]')
    flexible_date.click()

    finish_date = driver.find_element(By.XPATH, '/html/body/div[5]/section/div/div/div/footer/div/div/span/button')
    finish_date.click()

    amount_of_travelers = driver.find_element(By.NAME, 'Rooms & Guests')
    amount_of_travelers.click()

    search = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/tui-choice-search-panel/div/div/div/div/div[2]/div[1]/div/div/div[6]/button')
    search.click()
    
Search()