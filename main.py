import sys
import os
from utils import escape_characters
from time import sleep
from dotenv import load_dotenv
from get_cookie import get_cookie
from get_announcements import get_announcements
from send_telegram import send_telegram
from CookieManager import CookieManager
from AnnouncementTracker import AnnouncementTracker

moodle_url = "https://elearning.usm.my/sidang2324/my/"

if __name__ == "__main__":
    load_dotenv()

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    cookie_manager = CookieManager()
    tracker = AnnouncementTracker()

    if cookie_manager.exists():
        cookie = cookie_manager.get_cookie()
    else:
        cookie = get_cookie(email, password)
        cookie_manager.store_cookie(cookie)

    last_announcement_id = tracker.get_last_announcement_id()

    while True:
        print("Fetching announcements...")
        announcements = get_announcements(cookie)

        if announcements == "Invalid cookie":
            print("Invalid cookie, getting new cookie...")
            cookie = get_cookie(email, password)
            cookie_manager.store_cookie(cookie)
            continue

        # Only get announcements with id greater than last_announcement_id
        announcements = [
            announcement
            for announcement in announcements
            if int(announcement["id"]) > last_announcement_id
        ]

        # Sort announcements by id in ascending order
        announcements = sorted(announcements, key=lambda k: k["id"])

        if len(announcements) > 0:
            print("Sending Telegram message...")
            for announcement in announcements:
                send_telegram(
                    f"""*{escape_characters(announcement['title'])} \({announcement['course_code']}\)*
                    by _{escape_characters(announcement['lecturer'])}_\n
                    {escape_characters(announcement['contents'])}\n
                    [🔗 Read more]({announcement['url']})""",
                    os.getenv("TELEGRAM_BOT_TOKEN"),
                    os.getenv("TELEGRAM_CHAT_ID"),
                )

            last_announcement_id = int(announcement["id"])
            tracker.store_last_announcement_id(int(last_announcement_id))
        else:
            print("No new announcements.")

        sleep(60)