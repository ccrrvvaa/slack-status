This python script changes profile status for one or many of your Slack accounts. 

## Create a Slack App
- Go to [https://api.slack.com/apps]
- Create a new app ("Status App")
- Go to "OAuth & Permissions" menu
- Click on "Install App"
- In "Scopes" section, go to "User Token Scopes" and add the scope "users.profile:write"

## Create executable Links
- Install Python 3
- Install dependencies: `python3 -m pip install -r requirements.txt`
- Edit bash scripts `almorzando.sh` and `regreso.sh` to go to the directory of your script (in `cd` command line)
- Set executable permissions for bash scripts: `sudo chmod +x almorzando.sh regreso.sh`
- Copy the file `.env.tmp` as a new file with the name: `.env`
- Put your slack tokens in this file `.env`
- Edit the file lunch.py to put only the token's names (from `.env`) that you want to use
- Create a link for lunch status script (in my case, my home directory)
  - `ln -s $(pwd)/almorzando.sh /home/myuser/almorzando`
- Create a link for returning from lunch script
  - `ln -s $(pwd)/regreso.sh /home/myuser/regreso`
 
## Execution
- To have lunch: `cd ~ && ./almorzando`
- To return from lunch: `cd ~ && ./regreso`

Note: This steps are made for Linux users
