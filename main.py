import os
import logging

from flask import Flask

from src.bot import process_accounts
from src.utils.slack import send_text_message

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@app.route("/")
def run():
    try:
        process_accounts()
        message = 'Bot succeeded'
        send_text_message(message)
        return message
    except Exception as e:
        logging.exception('Exception')
        send_text_message('<!channel> Bot failed ' + str(e))
        return 'Bot failed'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))