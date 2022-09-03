import os
import configparser

config_parser = configparser.ConfigParser()
config_parser.read('./config/local.ini')

class Config:
    def __init__(self, config_parser):
        self.TWITTER_API_KEY = config_parser['TWITTER']['API_KEY']
        self.TWITTER_API_SECRET = config_parser['TWITTER']['API_SECRET']
        self.TWITTER_ACCESS_TOKEN = config_parser['TWITTER']['ACCESS_TOKEN']
        self.TWITTER_ACCESS_TOKEN_SECRET = config_parser['TWITTER']['ACCESS_TOKEN_SECRET']
        self.GS_CREDS_FILE = config_parser['GS']['CREDS_FILE']
        self.SLACK_WEBHOOK_URL = config_parser['SLACK']['WEBHOOK_URL']

config = Config(config_parser=config_parser)