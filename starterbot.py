import logging
import pprint
#  logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)
channel_id=os.environ["TEST_CHANNEL_ID"]

def join_channel(channel_id):
  try:
    response = client.conversations_join(channel=channel_id)
    print("Response:")
    print(response)
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

def send_message(channel=channel_id, text="I'm here! :huaji:"):
  try:
    response = client.chat_postMessage(
      channel=channel,
      text=text
    )
  except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'

def list_conversation():
  response = client.conversations_list(types="public_channel")

#  print(client.conversations_list())
#  print(client.conversations_history(channel=channel_id))
#  print(client.conversations_history(channel="C01M9DUQ6UA"))

def all_channnel_id():
  response = client.conversations_list(types="public_channel")


