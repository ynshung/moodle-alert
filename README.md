# Moodle Alerts

Get prompt notifications for new Moodle announcements. Designed for [USM's e-Learning](https://elearning.usm.my/sidang2324/my/) platform.

## Usage
Intended for USM students but can be customized for other Moodle sites.
1. Install dependencies with `pip install -r requirements.txt`
2. Create `.env` file with the following variables:
    - `EMAIL`: USM Identity email
    - `PASSWORD`: USM Identity password
    - `TELEGRAM_BOT_TOKEN`: Telegram bot token
    - `TELEGRAM_CHAT_ID`: Telegram chat ID
3. Run `python main.py`

## Screenshots
<img src="https://github.com/ynshung/moodle-alert/assets/61302840/00bce1ec-63fe-471b-b055-1f357daa4786" width=400 />
<img src="https://github.com/ynshung/moodle-alert/assets/61302840/f139b2af-e56f-484f-97a3-517dedb7c9df" height=200 />


## License
MIT License
