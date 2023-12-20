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

## License
MIT License
