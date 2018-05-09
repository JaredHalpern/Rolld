# Rolld
RPG-dice Slack integration

Rolld is a Slack Integration that makes it easy to roll dice in a Slack Channel. That's really all there is to it. I put this thing together in a few hours downtime. I don't plan to distribute it because I don't want all the dozens (there are dozens of us!) of gamers banging on my free-tier Heroku dyno.

Steps to set up this integration for your local Slack channel:

1. Clone the repo `git clone git@github.com:JaredHalpern/Rolld.git`
2. Make sure you have [Homebrew](https://brew.sh/) installed. If not, `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
3. Install the Heroku CLI: `brew install heroku/brew/heroku`
4. Verify Heroku CLI installation:
```heroku --version
heroku/7.0.0 (darwin-x64) node-v8.0.0```
5. Ensure you've created an account at https://www.heroku.com
6. Login to Heroku via command line: `heroku login`
7. Change to the cloned Rolld directory: `cd Rolld`
8. Create a heroku app: `heroku create`. We'll configure Slack to point to this URL soon. This command also creates a remote pointing to Heroku.
9. Verify the remote is set up, `git remote -v`.
You should see something like:
```heroku  https://git.heroku.com/yass-girl-61413.git (fetch)
heroku  https://git.heroku.com/yass-girl-61413.git (push)```
10. Push to the Heroku remote: `git push heroku master`