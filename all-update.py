import logging
#  logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)
test_channel_id=[
    os.environ["TEST_CHANNEL_ID"],
    os.environ["WG_ID"]
    ]

#  response = client.conversations_list(types="public_channel")

ts = '1616335942.000600'

for i in test_channel_id:
    print("====================")
    print("id = {}".format(i))
    print(client.conversations_history(channel=i, oldest=ts))

