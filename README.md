# 1. Bot Luamod

[OBSOLETE] The Bot Luamod is a Discord Bot whose main function is to moderate a server, provide a logging system for monitoring, and offer features for members and developers, including AI commands (chatbot).

# 2. Features

I. General

- `ping` - Displays the bot's latency.

- `help` - Displays the list of commands.

- `avatar < member >` - Displays a member's avatar.

- `userinfo < member >` - Displays user information.

- `serverinfo` - Displays server information.

- `botinfo` - Displays bot profile information.

II. Moderators

- `warn < member > < reason >` - Warns a user.

- `unwarn < member >` - Removes all warnings from the user.

- `warnings < member >` - Views the number and reason(s) of warnings for a user.

- `warninglist` - Views the user(s) warned and the number of warnings each has.

- `clear < quantity >` - Deletes chat messages.

- `purge < member > < quantity >` - Deletes a member's chat messages.

- `slow < seconds >` - Activates slow mode in the channel.

- `lock` - Locks a channel.

- `unlock` - Unlocks a locked channel.

- `lockdown` - Locks all channels.

- `unlockdown` - Unlocks all channels.

- `mute < member > < minutes >` - Temporarily mutes a member.

- `unmute < member >` - Removes a member's mute.

- `kick < member >` - Kicks a member from the server.

- `ban < member >` - Bans a member from the server.

- `unban < ID >` - Removes a ban from a user by ID.

- `tempban < member > < quantity >` - Bans a member from the server for a period of time.

- `softban < member >` - Bans a member from the server for one second to clear messages.

- `setlog < channel >` - Sets a channel to receive server action logs.

III. Developers

- `restart` - Restarts the bot.

- `toswitchoff` - Turns off the bot.

- `log` - Views the bot's log history.

- `clearlog` - Clears the bot's log history.

- `reloadcog < cog >` - Reloads a specific cog.

- `debug` - Displays general and technical information about the bot.

IV. AI

- `on` - Turns on AI chat.

- `off` - Turns off AI chat.

# 3. Simple API

Simple API built with FastAPI to view the bot's overall status. Localhost.

# 4. Technologies

- Language: Python (≈ 3.13)
- Framework: FastAPI (0.116.1)
- Library: Discord.py (2.5.2)
- Code Versioning: Git (≈ 2.33.0)
- Containerization: Docker (≈ 28.0.0)
- Scanner: Trivy (≈ 0.65.0)
- CI: Github Actions

# 5. Clone the Repository

- Bash

`git clone https://github.com/jose-techcode/Bot-Luamod`

# 6. Project Folder

- Bash

`cd Bot-Luamod`

# 7. Install Dependencies

`pip install -r requirements.txt`

# 8. Setting Environment Variables

Create a file called .env in the project root and add your bot token:

`DISCORD_TOKEN=your_token`

In the same .env file, if you're creating specific commands for only the bot developer to use, add:

`DEV_ID=your_id`

Also, in the same .env file, if you're creating specific commands for using the bot's AI, add:

`API_KEY_OPEN_ROUTER=your_api_key`

These files should not be uploaded to Github, as they contain sensitive information. Therefore, they should be included in .gitignore.

# 9. Run the Project

- Bash

`cd src`

- Python

`python bot.py`

# 10. Run in Docker

- Building the Image.

`docker build -t bot-luamod .`

- Optional: Scan the docker image with trivy tool (false positives are expected).

`trivy image bot-luamod:latest`

- Running the Container.

`docker run -it --name container_bot_luamod bot-luamod`

# 11. Contribution

Feel free to open Issues or submit Pull Requests.

# 12. License

This project is licensed under the AGPL license.