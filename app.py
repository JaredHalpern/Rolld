import os
import re #regex
import random
from slackclient import SlackClient
from flask import abort, Flask, jsonify, request

slack_client = SlackClient(os.environ.get('SLACK_ROLLD_TOKEN'))

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['POST'])
def test():
	if not is_request_valid(request):
		abort(400)

	command = request.form.get('command', None)
	parameter_text = request.form.get('text', None)
	
	# https://regex101.com/r/K6q4PR/1/
	DICE_REGEX = "([1-99])d([4,6,8,10,12,20]{1,2})"

	matches = re.search(DICE_REGEX, parameter_text)

	if not matches:
		return jsonify({
				'response_type': 'in_channel',
				'text': 'Rolld Result: ' + 'Invalid dice',
				'attachments': [
								{
								'color': '#C70005',
								'author_name': 'Rolld!',
								'image_url': 'https://i.imgur.com/aSRSGkG.gif',
								}
								]
				})

	results = []
	
	numberOfRolls = int(matches.group(1))
	dieToUse = int(matches.group(2))

	for x in range(numberOfRolls):
		randNum = random.randint(1,dieToUse+1)
		results.append(randNum)

	return jsonify({
		'text': 'Rolld Result: ' + str(results),
		'response_type': 'in_channel',
		'attachments': [
			            {
			            'color': '#C70005',
                		'author_name': 'Rolld!',
                		'image_url': 'https://i.imgur.com/LPPo1BS.gif',
			            }
			            ]
		})	

def is_request_valid(request):
	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

	return is_token_valid and is_team_id_valid

if __name__ == "__main__":
	app.run(debug=True)