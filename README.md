# Tracker App

Tracker is a Python application with a Tkinter GUI designed for managing tasks, tracking progress, and sending email notifications. This app supports sending emails using the Mailtrap API, allowing you to test email functionalities in a safe, development-oriented environment.

## Features

- **Task Tracking**: Manage tasks and keep track of progress within the app.
- **Email Notifications**: Send task updates or notifications via email using Mailtrap.
- **User-Friendly GUI**: Built with Tkinter, providing a simple and interactive interface.

## Prerequisites

- Python 3.8+
- Mailtrap Account (for email testing)

## Installation

### Clone the Repository

```bash
git clone https://github.com/Hannesanity/TimeSpy
cd TimeSpy
'''

Install Dependencies
pip install -r requirements.txt

Configuration
To enable email sending capabilities, you’ll need to set up the Mailtrap API by providing sender and receiver email addresses and the API key.

Sign up at Mailtrap and create an API key.
Configure config.py:
Create a config.py file in the root directory and add the following details:
Python

# config.py
api = 'your_mailtrap_api_key'
send = 'your_sender_email@example.com'
rec = 'your_receiver_email@example.com'
Replace 'your_mailtrap_api_key', 'your_sender_email@example.com', and 'your_receiver_email@example.com' with your Mailtrap API key and email addresses.
Using the send_email Function
The send_email function in Tracker.py handles email sending. It uses the API key and emails configured in config.py.

If you do not wish to use the email sending feature, you can remove or comment out the send_email function in Tracker.py.

Running the App
Launch the Tracker App with the following command:

python tracker.py


# Future Improvements/Features that others can add:
Descriptive Analytics
Enhanced UI/UX
Mobile Compatibility
etc.
