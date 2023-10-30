# SysBot

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Static Badge](https://img.shields.io/badge/aiogram-red)](https://docs.aiogram.dev/uk-ua/latest/)
[![Static Badge](https://img.shields.io/badge/Docker-yellow)](https://docs.docker.com/)
[![Static Badge](https://img.shields.io/badge/HTML_PYPI-green)](https://pypi.org/project/html/)

<div>
<h1>Description</h1>
<p>This is a simple Telegram bot designed to help system administrators. It allows users to select a department, enter their PC number, select a problem category and provide additional problem description if required. After receiving the information, the bot sends a message to the group chat for system administrators and saves the user's data to the database.</p>

<h1>Getting Started</h1>
<h2>Installation</h2>
<p>Clone the repository:</p>

     https://github.com/VAlduinV/SysBot.git

<p>Before running the script, make sure you have installed the following dependencies:</p>
    
     pip install -r requirements.txt

<h1Configuration</h1>
<p>The config.py file - define the following variables in it:</p>
<ul>
     <li>bot_token: Your bot's token, which you can get from @BotFather on Telegram.</li>
     <li>GROUP_CHAT_ID: ID of the group chat to which the bot will send messages.</li>
     <li>Run the data_base.py file to create the database and tables.</li>
</ul>

<h1>Usage</h1>
<p>Example:</p>
<ul>
  <li>Send the /start command to the bot. The bot will send a welcome message and prompt you to select a department.</li>
  <li>Select a department by clicking on the appropriate button. The bot will ask for your PC number.</li>
  <li>Enter your PC number. The bot will prompt you to select a problem category.</li>
  <li>Select a problem category. If you choose "Other", the bot will ask you to describe the problem. Otherwise, it will ask you to confirm sending the message.</li>
  <li>If you confirm sending the message, the bot will send it to the group chat and save your data in the database. If you refuse, the bot will cancel sending the message.</li>
</ul>

<h1>Startup</h1>
<p>Just run the file main.py:</p>
<p>To run the script, use the following command:</p>

     python main.py

<h1>Logging</h1>
<p>The script uses the logging library to log activity.
You can configure the logging level in the script to control the granularity of the logs.</p>
</div>