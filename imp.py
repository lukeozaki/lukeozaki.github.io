import requests
from bs4 import BeautifulSoup

URL = "https://toridoll-job.com/toridoll02/kyujin_l.htm?L=BMSList&BCD=sYP&SF=1&NOI=3000&P=1&SD=VAL99%2CUD%2CID&KCD_=&val91=010"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all("a", class_="job_link")
for link in links:
        link_url = link["href"]
        print(f"<a href=\"{link_url}\">{link_url}</a>\n")
