# Over the fence
Inspired by whatsapp bbut in more of a community message board form. Users can send messages like they would in a texting application but instead of
sending  to a friend or group messages post for everyone to see.


## Set Up and Instalation
1. Fork and clone this repository
2. `cd` into your project directory
3. Enter a virtual environment by runing `pipenv shell`
4. Install dependencies by running `pipenv install`
5. Check out to a new branch
6. Run your server with `python3 manage.py runserver`

## Important Links
- [Client Repo](https://github.com/PatrickDohn/Overthefence-client)
- [Deployed API](https://git.heroku.com/overthefence.git)
- [Deployed Client]( https://patrickdohn.github.io/Overthefence-client/)

## Planning Story


## User Stories
As an unregistered user, I would like to sign up with email and password.
As a registered user, I would like to sign in with email and password.
As a signed in user, I would like to change password.
As a signed in user, I would like to sign out.
As a signed in user, I would like to create a message.
As a signed in user, I would like to update my messages.
As a signed in user, I would like to delete my messages.
As a signed in user, I would like to see all messages from every user.


## Back End Technologies Used
- Django (restframework)
- Python

## API Routes

### Authentication

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-up`             | `users#signup`    |
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-pw/` | `users#changepw`  |
| DELETE | `/sign-out/`        | `users#signout`   |

### Survey

| Verb   | URI Pattern            | Description |
|--------|------------------------|-------------------|
| GET    | `/chats/`             | `Get a list of all chats`    |
| POST   | `/chats`             | `Create a new chat`    |
| PATCH  | `/chats/:id` | `Edit a chat that you own`  |
| DELETE | `/chats/:id`        | `Delete your own chat`   |


## Unsolved Problems
I would like to encorporate sockets for a instant load
I would like to add the ability to add groups and contacts to only message certain people


## ERD
- [ERD](https://imgur.com/nK3KiyF)
