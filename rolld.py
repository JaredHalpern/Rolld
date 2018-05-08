import os
import re #regex
from slackclient import SlackClient

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_client = SlackClient(os.environ.get('SLACK_ROLLD_TOKEN'))

slack_client.api_call(
  "chat.postEphemeral",
  channel="programming",
  text="Greetings! :tada:",
  user="jared"
)