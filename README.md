# AutoMailer
Send Templatized Dynamic Emails Automatically 

[![Generic badge](https://img.shields.io/badge/tests-passing-<COLOR>.svg)](https://aahnik.github.io/)
[![ MIT license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://aahnik.github.io/)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/aahnik/AutoMailer)

This is a simple program which does its work perfectly. Nothing more, nothing less

1. Send dynamic emails with unlimited variables pulling data from a database(csv file)
2. Supports Markdown Formatting & embed links or images
3. Supports Attaching any kind of files

[See ScreenShots](/screenshots.md)

---


### Step Wise Usage Guide

- Download or Clone the repo

- Open the `Automailer` Folder >> Read LICENCE >> open the folder **automailer**

- Write your email inside **`compose.md`** (supports markdown formatting)

- You can use **variables** , prefix them with `$` sign.

  > Hi $NAME , you have Bill Rs. $price due for $months

- Put your data inside **`data.csv`** file

*The line 1 ie headers must contain 'EMAIL' (uppercase) parameter*

![image of csv](csv_image.png)

*You can Export CSV file from Microsoft Office Excel, Libre Office, Google Sheets, SQL Database, or NoSQL Database*

- You you want to put any attachments , put them in the **`ATTACH` folder** inside the `autoMailerByAahnik` folder

- Open **`creds.py`** file to set DISPLAY_NAME ,SENDER_EMAIL, PASSWORD


---

Note:

**Do not use original email password.** 

Create a seperate Gmail Account then turn on 2 step Verification, and then set up an [App Password](https://support.google.com/accounts/answer/185833?hl=en)

---

  
- All set up 👍 you are now READY TO GO . RUN the `sender.py` file 

- You will be asked to confirm the attachments in `ATTACH` folder. Upon confirmation , the application will start sending Emails 

- You will recieve a full success report after emails are sent

**Having Issues?**

Errors while Running in your Computer ? Difficulty setting up ?
[Create an Issue](https://github.com/aahnik/AutoMailer/issues/new) in this GitHub repo describing your problem.
 