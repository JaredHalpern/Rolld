import os
import re
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
	# not perfect - will allow for 1d66, 2d44, etc
	DICE_REGEX = "([\d]+)d(4|6|8|100|10|12|20)+(\+\d)*"

	matches = re.search(DICE_REGEX, parameter_text)

	if not matches:
		return jsonify({
				'text': 'Rolld Result: ' + 'INVALID DICE - Try again!',
				'attachments': [
							{
							'color': '#C70005',
							'author_name': 'Rolld!',
							'image_url': 'https://i.imgur.com/aSRSGkG.gif',
							}
							]
				})

	results = []
	modifier = 0
	
	numberOfRolls = int(matches.group(1))
	dieToUse = int(matches.group(2))
	if matches.group(3):
		modifier = int(matches.group(3))

	for x in range(numberOfRolls):
		randNum = random.randint(1,dieToUse)
		results.append(randNum)
	
	total = sum(results) 

	return jsonify({
		'text': 'Rolld Result: ' + str(total+modifier) + '. Breakdown ' + str(results),
		'response_type': 'in_channel',
		# 'attachments': [
		# 	            {
		# 	            'color': '#C70005',
  #               		'author_name': 'Rolld!',
  #               		'image_url': 'https://i.imgur.com/LPPo1BS.gif',
		# 	            }
		# 	            ]
		})	

def is_request_valid(request):
	is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
	is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

	return is_token_valid and is_team_id_valid

if __name__ == "__main__":
	app.run(debug=True)
