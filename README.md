## Create a Slack App
- Go to [https://api.slack.com/apps]
- Create a new app ("Status App")
- Go to "OAuth & Permissions" menu
- Click on "Install App"
- In "Scopes" section, go to "User Token Scopes" and add the scope "users.profile:write"

## Create executable Links
- Install Python 3
- Install dependencies: `python3 -m pip install -r requirements.txt`
- Make `almorzando.sh` and `regreso.sh` exeutable files: `sudo chmod +x almorzando.sh regreso.sh`
- Create a link for lunch (in my case, in my home directory)
  - `ln -s $(pwd)/almorzando.sh /home/youruser/almorzando`
- Create a link for finish lunching
  - `ln -s $(pwd)/regreso.sh /home/youruser/regreso`

