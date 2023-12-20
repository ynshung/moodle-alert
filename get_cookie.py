import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_cookie(email, password, moodle_url="https://elearning.usm.my/sidang2324/my/"):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(moodle_url)
    if driver.current_url == "https://elearning.usm.my/sidang2324/login/index.php":
        driver.find_element(
            By.XPATH,
            '//*[@id="region-main"]/div/div/div[2]/div/div[2]/div/a',
        ).click()
        driver.find_element(By.ID, "userNameInput").send_keys(email)
        driver.find_element(By.ID, "passwordInput").send_keys(password)
        driver.find_element(By.ID, "submitButton").click()

    # Dismiss alert
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    cookie = driver.get_cookie("MoodleSession")["value"]

    driver.quit()

    return cookie


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <email> <password>")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]

    try:
        print("Got cookie:", get_cookie(email, password))
    except Exception as e:
        print(e)
        sys.exit(1)
