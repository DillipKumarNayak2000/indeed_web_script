import requests
from bs4 import BeautifulSoup

def scrape_indeed_jobs(keyword):
    base_url = "https://in.indeed.com"
    url = f"{base_url}/jobs?q={'+'.join(keyword.split())}&sort=date"  # Construct the URL

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


      # Adding a user-agent to mimic a browser request

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        job_elems = soup.find_all("div", class_="jobsearch-SerpJobCard")

        for job_elem in job_elems:
            title_elem = job_elem.find("h2", class_="title")
            company_elem = job_elem.find("span", class_="company")
            location_elem = job_elem.find("span", class_="location")

            if None in (title_elem, company_elem, location_elem):
                continue

            title = title_elem.text.strip()
            company = company_elem.text.strip()
            location = location_elem.text.strip()

            print(f"Title: {title}\nCompany: {company}\nLocation: {location}\n{'-' * 50}")

    else:
        print(f"Failed to fetch data : {response.status_code}")

# Usage
scrape_indeed_jobs("Python developer")