import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import json 

driver = webdriver.Chrome()
driver.get("https://penncoursereview.com/department/CIS")
userName = driver.find_element(By.XPATH, "//*[@id='username']")
userName.send_keys("sharonyu")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("YXFsharon991125")

login =  driver.find_element(By.XPATH, "//*[@id='loginform']/button")
login.click()

wait = WebDriverWait(driver, 200000)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.rt-tr-group")))

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

def extract_course(soup):
    courseReviews = {}

    courseRows = soup.find_all('div', class_='rt-tr-group')



    # TODO: filter out courses below 5000 
    for course in courseRows:
        info = course.find_all('div', role='gridcell')
        # print(len(info))

        for i, j in enumerate(info):
            # title = ''
            if i == 1:
                title = j.get_text()
                courseReviews[title] = {}
                print(title)
            elif i == 2:
                courseReviews[title]['Course Quality'] = j.get_text()
                print(j.get_text())
            elif i == 3:
                courseReviews[title]['Instructor Quality'] = j.get_text()
                print(j.get_text())
            elif i == 4:
                courseReviews[title]['Difficulty'] = j.get_text()
                print(j.get_text())
            elif i == 5:
                courseReviews[title]['Workload'] = j.get_text()
                print(j.get_text())
            
    with open('courseRatings.json', 'w') as fp:
        json.dump(courseReviews, fp)
    print(courseReviews)

    return courseReviews

def main():
    url = "https://penncoursereview.com/department/CIS"
    # soup = get_page(url)
    if soup:
        extract_course(soup)

if __name__ == '__main__':
    main()