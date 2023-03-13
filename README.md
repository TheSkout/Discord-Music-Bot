# IF YOU DON'T UNDERSTAND WHAT ARE YOU DOING, DON'T JUST COPY-PASTE THE CODE

# Discord-Music-Bot
Self-Hosted Discord bot that can play music from youtube


# Creating Application
You need to create your app on [Discord Developer Portal](https://discord.com/developers/applications) 

Click on **New Application** button, enter your application's name, click on checkbox and click **Create**

# Creating Bot User
Click on **Bot** button on the left section

And now click **Add Bot** button

# Getting Bot Token

Under **Bot Username** field, there's 2 buttons **Copy** And **View Token**, you can just click the **Copy** button

You will have to paste this Token to **config.py** file, in TOKEN section, just replace the **PUT YOUR BOT TOKEN HERE** with your Token, and don't forget `'` around it
It should look like this: `'MTA4NDgyNDQ0MjcxMjEwMDkyNQ.Ggx0aw.ksqkqrJ3d6iLOPXxMRB8MGjmqMB5SZCBiq1Pkk'` 	<sub> Don't paste this token, you have to create and paste you own </sub>	

By the way, you can change other bot settings in that file, like bot name, bot id, etc.

#


Make sure not to show this Token to anybody, as the person you share this token with (unless they don't know how to program discord bot) can take over the control of your bot

On **Bot Page** on Discord Developer Portal

**"For security purposes, tokens can only be viewed once, when created. If you forgot or lost access to your token, please regenerate a new one."**

# Required Python Packages
To install packages open command prompt (if you don't know how to open the command promot - just google it)

Required package names are listed below

For Windows: `py -3 -m pip install <package-name>`

For UNIX/MacOS: `python3 -m pip install <package-name>`

Required Packages:

Yes, you can just copy-paste these into `<package-name>`, make sure you remove the `< >`

`discord.py[voice]`

`yt-dlp`

`ffmpeg`

# Adding bot to the server

Go to [Discord Developer Portal](https://discord.com/developers/applications), choose your application

Click on **OAuth2**, then on URL Generator

Choose **bot** scope, choose **Administrator** in permissions section

And at the page bottom you need to copy generated URL, and paste it in you browser

Select your server, pass the captcha challenge, and you are ready to go

# Running your bot

Now you can run the **bot.py** file, just click it (or select **Run with Python**, etc), and your bot should be up

# Commands
Bot default Prefix is `;`, however, you can change that in **config.py** file, prefix section. Command below are listed with the default prefix

`;join` - bot joins in channel (bot does not join automaticaly at `;play` command (will be fixed in future updates))

`;leave` - bot leaves the channel (bot does not leave the channel automaticaly (will be fixed in future updates))

`;play` <youtube video link>` - plays the video (the sound of it of course)

`;pause` - pauses the playback

`;resume` - resumes the playback

`;stop` - stops the playback

# It is highly unrecommended to paste links to playlist, because bot starts to download all tracks in the playlist (will be fixed in the future updates)  
