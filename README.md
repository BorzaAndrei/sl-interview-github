# Sector Labs Home Assignment

## Task

Using the Github Gist API, I'm creating a single-app page using Django as my Web framework. 

The application will allow users to enter a username and get a full list of public Gists for that user.

Functionalities:
- [x] search - when a user enters an username, they will receive a full list of public Gists by that user

- [x] fileTypes - converts the filetypes of the files in the Gist into a tag/badge

- [x] forks - includes with the list of the Gists the username/avatar of the last 3 users who have forked it

- [x] Gist contents - when clicking one of the Gists, display the content of the file

- [x] styling with CSS (Flex or Grid recommended)

## How to run

Run `python github_gists/manage.py runserver` from the top-level folder

Navigate in browser to `http://127.0.0.1:8000/gists`
