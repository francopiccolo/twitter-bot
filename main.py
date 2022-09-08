import logging

from src.bot import process_accounts
from src.utils.slack import send_text_message

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    try:
        process_accounts()
        send_text_message('Bot succeeded')
    except Exception as e:
        logging.exception('Exception')
        send_text_message('<!channel> Bot failed ' + str(e))