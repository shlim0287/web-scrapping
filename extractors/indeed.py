from requests import get
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def get_page_count(keyword):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(
        "C://Users//임성현\\OneDrive\\바탕 화면\\chromedriver_win32\\chromedriver.exe", options=options)
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find_all("div", class_="css-tvvxwd ecydgvn1")
    if pagination == None:
        return 1

    for pages in pagination:
        anchors_page = pages.find_all("a", recursive=False)

    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


time.sleep(10)


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    for page in range(pages):

        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(
            "C://Users//임성현\\OneDrive\\바탕 화면\\chromedriver_win32\\chromedriver.exe", options=options)
        base_url = "https://kr.indeed.com/jobs"
        browser.get(f"{base_url}?q={keyword}&start={page*10}")

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList css-0")
        jobs = job_list.find_all('li', recursive=False)

        results = []
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor["aria-label"]
                link = anchor["href"]
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    "link": f"http://kr.indeed,com{link}",
                    "company": company.string,
                    "location": location.string,
                    "position": title

                }
                results.append(job_data)
        for result in results:
            print(result, "//////\n//////")

        time.sleep(10)


return results
