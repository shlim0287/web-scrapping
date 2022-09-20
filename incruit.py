from requests import get
from bs4 import BeautifulSoup


base_url = "https://search.incruit.com/list/search.asp?col=all&src=gsw*www&kw="
search_term = "python"
response = get(f"{base_url}{search_term}")


if response.status_code != 200:
    print("Can't open page")

else:
    result = []
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find_all("ul", class_="c_row")
    for job_cpname_lists in job_list:
        job_cpname_list = job_cpname_lists.find_all("div", class_="cl_top")
        for job_cpname in job_cpname_list:
            anchors = job_cpname.find_all("a")
    for job_Qualification_Guidelines in job_list:
        job_QG = job_Qualification_Guidelines.find_all("div", class_="cl_md")

        print(job_QG)
