# Follower Tracker for Instagram

A simple Python script that identifies the Instagram users you follow who don't follow you back.

## Requirements
- Python 3.6+

## Setup

Create a new Python file on your local machine and copy the content of the `main.py` file from this repository.

## Usage

To use the script, you need to have two JSON files: `followers.json` and `following.json`. These files should contain the list of your Instagram followers and the users you're following, respectively.

To obtain these JSON files, you can request a download of your data directly from Instagram:

1. Go to your Instagram profile and click on 'Settings'.
2. Click 'Privacy and Security'.
3. Scroll down to 'Data Download' and click 'Request Download'.
4. Enter the email where you'd like to receive a link to your data and click 'Next'.
5. Enter your Instagram password and click 'Request Download'.

You'll receive an email from Instagram with a link to download your data. This might take up to 48 hours. The downloaded data will be in JSON format.

After obtaining and extracting your Instagram data:

Rename the followers file to `followers.json` and place it in the same directory as your Python script.
Rename the following file to `following.json` and also place it in the same directory as your Python script.

To run the script, navigate to the directory containing your script and JSON files, and use the following command:

```bash
python main.py
```

The script will then print a list of usernames that you're following but who aren't following you back.
