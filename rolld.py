import os
import re #regex
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_ROLLD_TOKEN'))

def test():
	slack_client.api_call(
	  "chat.postMessage",
	  channel="Cprogramming",
	  text="Greetings! :tada:",
	)

if __name__ == "__main__":
	test()