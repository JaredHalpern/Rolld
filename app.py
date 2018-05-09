import os
import re #regex
from slackclient import SlackClient
from flask import Flask, request, session, make_response

slack_client = SlackClient(os.environ.get('SLACK_ROLLD_TOKEN'))

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	slack_client.api_call(
	"chat.postMessage",
	channel="Cprogramming",
	text="Greetings! :tada:",
	)
	return 'Hello World.'

@app.route("/roll", methods=['GET', 'POST'])
def test():
	slack_client.api_call(
	  "chat.postMessage",
	  channel="Cprogramming",
	  text="Greetings! :tada:",
	)

if __name__ == "__main__":
	app.run(debug=True)