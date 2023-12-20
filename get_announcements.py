from bs4 import BeautifulSoup
import requests
from utils import rnl

def get_announcements(cookie_val, moodle_url="https://elearning.usm.my/sidang2324/my/"):
    page = requests.get(moodle_url, cookies={"MoodleSession": cookie_val})
    soup = BeautifulSoup(page.content, "html.parser")

    if soup.title.text != "Dashboard":
        return "Invalid cookie"

    ann_list = rnl(soup.find_all("div", {"class": "news-slider"})[0])

    announcements = []

    for i in ann_list:
        date = rnl(i.contents)[0].div.text
        announcement_contents = rnl(rnl(i.contents)[2].contents)

        url = announcement_contents[0].a.get("href")
        id = url.split("d=")[1]
        title = announcement_contents[0].a.text
        course_code = announcement_contents[1].strong.strong.text.strip().split("-")[0]
        lecturer = announcement_contents[1].text.split("by")[1].strip()
        contents = announcement_contents[2].text.replace("[Read More]", " ").strip()

        announcements.append(
            {
                "id": id,
                "url": url,
                "date": date,
                "course_code": course_code,
                "title": title,
                "lecturer": lecturer,
                "contents": contents,
            }
        )

    return announcements


if __name__ == "__main__":
    pass
