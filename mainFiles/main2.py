from bs4 import BeautifulSoup
import requests
from time import sleep

print("Put some skill you are not familiar with")
unknownSkill = input("> ")
print("Filtering Out : " + unknownSkill)


def findJobs():
    htmlText = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    ).text
    soup = BeautifulSoup(htmlText, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        publishedDate = job.find("span", class_="sim-posted").span.text

        if "few" in publishedDate:
            companyName = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            moreInfo = job.header.h2.a["href"]

            if unknownSkill not in skills:
                with open(f"./posts/post{index}.txt", "w") as f:
                    f.write(f"Company Name : {companyName.strip()} \n")
                    f.write(f"Skills Required : {skills.strip()} \n")
                    f.write("More Info : " + moreInfo.strip())
                print("File saved : " + str(index))


if __name__ == "__main__":
    while True:
        findJobs()
        timeWait = 5
        print("Waiting " + str(timeWait) + " minutes.....")
        sleep(timeWait * 60)