import logging
from datetime import datetime

import tweepy
from gspread.exceptions import WorksheetNotFound

from src.utils.twitter import get_api as get_twitter_api
from src.utils.twitter import get_users_from_user_ids
from src.utils.gs import get_client as get_gs_client
from src.config import config


FIELDS = ['id', 'handle', 'name', 'bio', 'location', 'website', 'date_joined', 'followers', 'following', 'inserted_datetime']

def get_account_sheet(spreadsheet, account):
    try:
        account_sheet = spreadsheet.worksheet(account)
    except WorksheetNotFound:
        spreadsheet.add_worksheet(account, rows=10, cols=2)
        account_sheet = spreadsheet.worksheet(account)
        account_sheet.append_row(FIELDS)
    return account_sheet

def process_account(spreadsheet, twitter_api, account):
    logging.info('Processing account {}'.format(account))
    account_sheet = get_account_sheet(spreadsheet, account)
    existing_friends_ids = [int(friend_id) for friend_id in account_sheet.col_values(1)[1:]]
    all_friend_ids = [friend_id for friend_id in tweepy.Cursor(twitter_api.get_friend_ids, screen_name=account).items()] # https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friends-ids 5000ids/request 15req/min = 75,000
    new_friend_ids = [friend_id for friend_id in all_friend_ids if friend_id not in existing_friends_ids]
    if new_friend_ids:
        logging.info('Adding new friends: {}'.format(','.join([str(friend_id) for friend_id in new_friend_ids])))
        new_friends = get_users_from_user_ids(twitter_api, new_friend_ids) # https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup 100users/request 900requests/15min = 90,000users/15min
        friends_rows = [[str(friend.id), friend.screen_name, friend.name, friend.description, friend.location, friend.url, friend.created_at.strftime('%Y/%m/%d, %H:%M:%S'), friend.followers_count, friend.friends_count, datetime.now().strftime("%d/%m/%Y %H:%M:%S")] for friend in new_friends]
        account_sheet.insert_rows(friends_rows, row=2)


def process_accounts():
    gs_client = get_gs_client(config.GS_CREDS_FILE)
    twitter_api = get_twitter_api(config.TWITTER_API_KEY, config.TWITTER_API_SECRET, config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)

    spreadsheet = gs_client.open('Twitter bot')
    accounts = spreadsheet.worksheet('accounts').col_values(1)[1:]

    for account in accounts:        
        process_account(spreadsheet, twitter_api, account)