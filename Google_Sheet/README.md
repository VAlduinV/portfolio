# GoogleSheet

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Static Badge](https://img.shields.io/badge/gspread-violet)](https://docs.gspread.org/en/v5.12.0/)
[![Static Badge](https://img.shields.io/badge/oauth2client-red)](https://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html)


     ______   ______   ______   ______   __       ______   ______   __  __   ______   ______  ______  ______    
    /\  ___\ /\  __ \ /\  __ \ /\  ___\ /\ \     /\  ___\ /\  ___\ /\ \_\ \ /\  ___\ /\  ___\/\__  _\/\  ___\   
    \ \ \__ \\ \ \/\ \\ \ \/\ \\ \ \__ \\ \ \____\ \  __\ \ \___  \\ \  __ \\ \  __\ \ \  __\\/_/\ \/\ \___  \  
     \ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\ \_____\\/\_____\\ \_\ \_\\ \_____\\ \_____\ \ \_\ \/\_____\ 
      \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_____/ \/_/\/_/ \/_____/ \/_____/  \/_/  \/_____/ 

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=30&pause=1000&color=F70000&center=true&vCenter=true&width=500&height=90&lines=GoogleSheets)](https://git.io/typing-svg)

<div>
<h1>Google Sheets Python API Usage</h1>
<p>This Python script demonstrates basic usage of the Google Sheets API using the gspread library.
The script provides a GoogleSheet class to interact with Google Sheets.
This includes selecting a worksheet, reading and writing a cell, reading and writing a range of cells, adding and deleting rows, and sharing the worksheet with other users.</p>

<h1>Installation</h1>
<p>Before running the script, make sure you have installed the following dependencies:</p>
    
     pip install -r requirements.txt

<h1>Google Sheets API Settings</h1>
<p>You need to set up the Google Sheets API to get credentials to access your spreadsheet.</p>
<ul>
     <li>Go to the Google API Console (https://console.developers.google.com/)</li>
     <li>Create a new project.</li>
     <li>Enable the Google Sheets API for your project.</li>
     <li>Create API credentials.</li>
     <li>Choose JSON as the key type and upload a JSON file.</li>
     <li>Move this JSON file to your project directory.</li>
</ul>

<h1>Usage</h1>
<p>Create an instance of the GoogleSheet class with your Google Sheets credentials file and a spreadsheet ID.</p>
<p>Example:</p>

     google_sheet = GoogleSheet("your_credentials.json", "spreadsheet_id")

<p>This script provides methods to perform various operations with Google Sheet:</p>
<ul>
  <li>select_sheet(sheet_name): select a specific sheet from the spreadsheet.</li>
  <li>share(email, perm_type, role): Share a spreadsheet with someone.</li>
  <li>read_cell(cell): read the value from a specific cell.</li>
  <li>write_cell(cell, value): write the value in a certain cell.</li>
  <li>read_range(start_cell, end_cell): read values from a range of cells.</li>
  <li>write_range(start_cell, end_cell, values): write values to a range of cells.</li>
  <li>append_row(values): add a row to the worksheet.</li>
  <li>delete_rows(start, end): delete rows from the sheet.</li>
  <li>find_telegram_channels(start_cell, end_cell): find all links to Telegram channels in a range of cells.</li>
</ul>

<p>To run the script, use the following command:</p>

     python your_script_name.py "Sheet1" "A1" "A10"

<p>In the above command, "Sheet1" is the sheet name, "A1" is the starting cell, and "A10" is the ending cell.
The script will look for links to Telegram channels in the range "A1" to "A10" on "Sheet1"
and write the found links in the file "telegram_channels.txt".</p>

<h1>Logging</h1>
<p>The script uses the logging library to log activity.
You can configure the logging level in the script to control the granularity of the logs.</p>
</div>
