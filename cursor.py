import logging
#  logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ['SLACK_API_TOKEN']
client = WebClient(token=slack_token)

id_tc = os.environ['TEST_CHANNEL_ID'],
id_wg = os.environ['WG_ID'],
id_random = os.environ['RANDOM_ID']

test_channel_id=[
        id_tc,
        id_wg,
        id_random
    ]


def pull_all(channel):
    message = []
    try:
        ans = client.conversations_history(channel=channel)
        message.extend(ans.data['messages'])
        while ans.data['has_more']:
            cursor = ans.data['response_metadata']['next_cursor']
            ans = client.conversations_history(channel=channel, cursor=cursor)
            message.extend(ans.data['messages'])
    except SlackApiError as e:
        # You will get a SlackApiError if 'ok' is False
        print(e.response['error'])
        assert e.response['error']  # str like 'invalid_auth', 'channel_not_found'
    return message

ans = pull_all(id_random)
