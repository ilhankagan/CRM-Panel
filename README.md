1️⃣ Installation & Launch
This project is a CRM (Customer Relationship Management) system developed in Python. It includes integrations with Google Sheets and Google Calendar.

🛠 Installing Required Dependencies
To run the project, follow these steps to install necessary Python packages:

Ensure Python is installed on your system (Recommended version: 3.9+).

Open your terminal or command prompt and navigate to the project folder.

Run the following command to install dependencies:

bash
Kopyala
Düzenle
pip install -r requirements.txt
🚀 Launching the Application
Once the dependencies are installed, launch the application using the following command:

bash
Kopyala
Düzenle
python main.py
The CRM interface will start automatically.

2️⃣ Usage Guide
When you launch the application, the Login Screen will appear. You can enter your username and password to access different menus.

🔹 Login Screen
You can use predefined credentials to log in.

If incorrect login information is entered, a warning message will appear.

🔹 Preferences Menu
After logging in, the Preferences Menu will display the following buttons:

Applications → Navigates to the application overview

Interviews → Opens the interview management screen

Mentor Meeting → Opens the mentor meeting screen

Main Menu → Returns to the login screen

Exit → Closes the application

You can navigate through these options to perform actions.

🔹 Admin Preferences Menu
This is an extended version of the Preferences Menu with admin access. It includes:

Admin Menu → Navigates to the calendar-integrated admin panel

🔹 Admin Panel
This panel integrates with Google Calendar. You can:

ETKİNLİK KONTROL (Event Check) → Fetch events from Google Calendar

MAIL GÖNDER (Send Mail) → Send emails to event participants

TERCİH-ADMIN MENU → Return to the Admin Preferences Menu

EXIT → Exit the admin panel

🔹 Applications Menu
In the Applications Menu, users can view and search application data.

🔸 Special Filter Options:
Mentor Assigned → Shows users who have a mentor meeting assigned (marked “OK”)

Mentor Not Assigned → Shows users without an assigned mentor (marked “ATANMADI”)

Clicking these buttons filters applications based on mentor assignment status.

🔹 Interviews & Mentor Meeting Screens
These screens allow you to view, search, and filter relevant data:

Interviews Screen → Displays candidates' interview progress

Mentor Meeting Screen → Tracks mentor meeting status

Both screens include a Preferences button to return to the main menu.

3️⃣ Additional Information
All data is synchronized with Google Sheets.

Google Calendar API is used for event management.

SMTP or Mailgun integration is used for sending emails.

4️⃣ Exiting the Application
You can exit the application by:

Clicking the Exit button on the login or menu screens

Using CTRL + C in the terminal

