# Rolld
RPG-dice Slack integration ([source](https://github.com/JaredHalpern/Rolld))

Rolld is a Slack Integration that makes it easy to roll dice in a Slack Channel. That's really all there is to it. I put this thing together in a few hours downtime when I needed to take a break from writing the [book](https://amzn.to/2J2ItUa). I don't plan to distribute it via Slack because I don't want the dozens (there are dozens of us!) of Slack gamers banging on my free-tier Heroku dyno. But you can deploy your own Rolld app to a Heroku dyno and integrate it into a Slack channel of your choosing.


![Rolld](https://i.imgur.com/LPPo1BS.gif)


### Usage

Roll + modifiers

![Rolld](https://i.imgur.com/aL5LdwM.png)

Rolld also supports multiple rolls, eg: `/roll 2d6`

![Rolld](https://i.imgur.com/wWfiY08.png)

### Steps to Setup your own Rolld App

Steps to set up this integration for your local Slack channel, using a free dyno on Heroku to host:

1. Clone the repo `git clone git@github.com:JaredHalpern/Rolld.git`
2. Make sure you have [Homebrew](https://brew.sh/) installed. If not, `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

#### Heroku

3. Install the Heroku CLI: `brew install heroku/brew/heroku`
4. Verify Heroku CLI installation: 
  `heroku --version` should show you something like: 
  `heroku/7.0.35 (darwin-x64) node-v10.0.0`
5. Ensure you've created an account at [https://www.heroku.com](https://www.heroku.com). You can use the free-tier for now.
6. Login to Heroku via command line: `heroku login`
7. Change to the cloned Rolld directory: `cd Rolld`
8. Set the Heroku buildpack: `heroku buildpacks:set heroku/python`
9. Create a heroku app: `heroku create`. We'll configure Slack to point to this URL soon. This command also creates a remote pointing to Heroku.
10. Verify the remote is set up, `git remote -v`.
You should see something like: 
  `heroku  https://git.heroku.com/yass-rangers-61413.git (fetch)`
  `heroku  https://git.heroku.com/yass-rangers-61413.git (push)`
11. Go to Heroku Settings: `https://dashboard.heroku.com/apps/<your app name>/settings` and find the Domain. 
  It should say something like: `Your app can be found at https://yass-rangers-61413.herokuapp.com/`. Note down this url for the next step.

#### Create a Slack App

12. Log into to your Slack account via the web: [https://api.slack.com/apps](https://api.slack.com/apps)
13. Hit the Create New App button
14. Name the app and choose a workspace in which to deploy it.
15. In the `Add features and functionality` Section, Click `Slash Commands`.
16. Hit the `Create New Command` button.
17. Enter the Command you'd like to use to invoke the integration. `/roll` seems natural.
18. In Request URL, use the url from Step 11: `https://yass-rangers-61413.herokuapp.com/`
19. Hit the Save button in the lower right.
20. In the Install your app to your workspace section, hit the `Install App to Workspace` button to install the integration. We're not done yet though.

#### Verification / Permissioning

21. Scroll down a bit further on the Basic Information page and copy the `Verification Token`. Put it somewhere safe and temporary.
22. Next click on OAuth & Permissions on the left-hand side. Copy the OAuth token and put it somewhere safe and temporary.
23. This next part is a bit odd - we need to get the Team-ID. The best way to do that (that I've found) is to navigate to your team's Slack channel in a web browser, then right-click and inspect the source. Find the text, `team_id` and grab the value next to it. It'll be something like `Z4KRT3F6A`.
24. We need to set the environmental variables. Best practices say that it's a terrible idea to ever store things like tokens in source-control. We can do this via the Heroku command line, but I'll show you how to do it in the Heroku CLI. Go to `https://dashboard.heroku.com/apps/<your app name>/settings` and tap the `Reveal Config Vars` button. Enter the following Key-Value pairs: `SLACK_VERIFICATION_TOKEN | value from step 1 in this section`, `SLACK_ROLLD_TOKEN | value from Step 2 in this section`, `SLACK_TEAM_ID     | value from step 3 in this section`
25. Alternatively, the Heroku [CLI](https://devcenter.heroku.com/articles/config-vars) syntax for setting config variables: `heroku config:set SLACK_VERIFICATION_TOKEN=....your token....`

#### Deploy

26. Push to the Heroku remote: `git push heroku master`
27. Open Slack, and run your command! `/roll 1d20`

I've probably missed a step or two. If you see something, feel free to file a PR and I'll update. Thanks!

#### Useful links
[Testing Slack integrations locally](https://api.slack.com/tutorials/tunneling-with-ngrok), [Easily resize gifs online](https://ezgif.com/)

#### Credits
Thanks to Justin Isaf, [jisaf](https://github.com/jisaf) for adding modifiers.