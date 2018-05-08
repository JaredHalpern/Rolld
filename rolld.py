import os
import re #regex
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_ROLLD_TOKEN'))

slack_client.api_call(
  "chat.postMessage",
  channel="programming",
  text="Greetings! :tada:",
)