# Rolld
RPG-dice Slack integration

Rolld is a Slack Integration that makes it easy to roll dice in a Slack Channel. That's really all there is to it. I put this thing together in a few hours downtime. I don't plan to distribute it because I don't want all the dozens (there are dozens of us!) of gamers banging on my free-tier Heroku dyno.


![Rolld](https://i.imgur.com/LPPo1BS.gif)


Steps to set up this integration for your local Slack channel, using a free dyno on Heroku to host:

1. Clone the repo `git clone git@github.com:JaredHalpern/Rolld.git`
2. Make sure you have [Homebrew](https://brew.sh/) installed. If not, `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
3. Install the Heroku CLI: `brew install heroku/brew/heroku`
4. Verify Heroku CLI installation: 
  `heroku --version` should show you something like: 
  `heroku/7.0.35 (darwin-x64) node-v10.0.0`
5. Ensure you've created an account at [https://www.heroku.com](https://www.heroku.com). You can use the free-tier for now.
6. Login to Heroku via command line: `heroku login`
7. Change to the cloned Rolld directory: `cd Rolld`
8. Create a heroku app: `heroku create`. We'll configure Slack to point to this URL soon. This command also creates a remote pointing to Heroku.
9. Verify the remote is set up, `git remote -v`.
You should see something like: 
  `heroku  https://git.heroku.com/yass-rangers-61413.git (fetch)`
  `heroku  https://git.heroku.com/yass-rangers-61413.git (push)`
10. Go to Heroku Settings: `https://dashboard.heroku.com/apps/<your app name>/settings` and find the Domain. 
  It should say something like: `Your app can be found at https://yass-rangers-61413.herokuapp.com/`. Note down this url for the next step.
11. Log into to your Slack account via the web: [https://api.slack.com/apps](https://api.slack.com/apps)
12. Hit the Create New App button
13. Name the app and choose a workspace in which to deploy it.
14. In the `Add features and functionality` Section, Click `Slash Commands`.
15. Hit the `Create New Command` button.
16. Enter the Command you'd like to use to invoke the integration. `/roll` seems natural.
17. In Request URL, use the url from Step 11: `https://yass-rangers-61413.herokuapp.com/`
18. Hit the Save button in the lower right.
19. In the Install your app to your workspace section, hit the `Install App to Workspace` button to install the integration. We're not done yet though.
20. Scroll down a bit further on the Basic Information page and copy the `Verification Token`. Put it somewhere safe and temporary.
21. Next click on OAuth & Permissions on the left-hand side. Copy the OAuth token and put it somewhere safe and temporary.
22. This next part is a bit odd - we need to get the Team-ID. The best way to do that (that I've found) is to navigate to your team's Slack channel in a web browser, then right-click and inspect the source. Find the text, `team_id` and grab the value next to it. It'll be something like `Z4KRT3F6A`.
23. We need to set the environmental variables. Best practices say that it's a terrible idea to ever store things like tokens in source-control. We can do this via the Heroku command line, but I'll show you how to do it in the Heroku CLI. Go to `https://dashboard.heroku.com/apps/<your app name>/settings` and tap the `Reveal Config Vars` button. Enter the following Key-Value pairs: `SLACK_VERIFICATION_TOKEN | value from step 21`, `SLACK_ROLLD_TOKEN | value from Step 22`, `SLACK_TEAM_ID     | value from step 23`
24. Alternatively, the Heroku [CLI](https://devcenter.heroku.com/articles/config-vars) syntax for setting config variables: `heroku config:set SLACK_VERIFICATION_TOKEN=....your token....`
25. Push to the Heroku remote: `git push heroku master`
26. Open Slack, and run your command! `/roll 1d20`

I've probably missed a step or two. If you see something, feel free to file a PR and I'll update. Thanks!