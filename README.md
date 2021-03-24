Backend of Slack Message Recording Bot
======================================


## Roadmap

- 210322
- [x] Verify script: Pull all update in X days from all channels
- [x] Write a function to handle paging properly
- [ ] Handle username conversion properly
- [ ] How to save conversation data?

## Feature Design

```bash
export SLACK_API_TOKEN="XXX"
./slack-message-recording.py --all-channel --join --store-repo="ofey404/slack-recording-repo.git"
```

## Reference
https://python-slackclient.readthedocs.io/en/latest/basic_usage.html#
