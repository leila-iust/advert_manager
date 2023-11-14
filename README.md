# advert_manager

# Cryptocurrency Exchange App

This is a Django Rest Framework (DRF) app that allows users to add comments to advertisements but there is a restriction that each user can only comment on an advertisment once.
What's more users can edit and delete their own comments and also all users can see all advertisements and comments without being authenticated
The app is built using the DRF framework and leverages Django's built-in user authentication system for managing user accounts and login sessions. 
It uses PostgreSQL as its database backend to store user and transaction data.

## key features:

- User authentication and registration
- Getting the list of all adverts and ther associated comments
- Insert/ update/ delete comments on adverts

## Requirements:

| Requirement | Specification          |
| ----------- |------------------------|
| OS          | Ubuntu 18.04 or higher |
| Language    | Python                 |
| Interpreter | Python 3.10+           |

## Local Development QuickStart:


### - Running locally

- Dependencies:

  - Linux system
  - Python 3.8+
  - virtualenv
  - PostgreSQL

- Installation

  ```bash
  # install
  $ git clone git@github.com:leila-iust/advert_manager.git
  $ cd advert_manager
  $ virtualenv -p /path/to/python3 venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

  # run db migrations
  $ python manage.py migrate

  # backend dev server:
  $ python manage.py runserver
  ```
