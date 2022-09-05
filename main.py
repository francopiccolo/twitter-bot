from src.bot import process_accounts
from src.utils.slack import send_text_message

if __name__ == '__main__':
    try:
        process_accounts()
        send_text_message('Bot succeeded')
    except Exception as e:
        send_text_message('<!channel> Bot failed ' + str(e))