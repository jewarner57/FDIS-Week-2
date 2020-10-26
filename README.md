# Week 2 Varsity | Admin, Login & Authentication

### Check out the [resources](https://github.com/flask-django-independent-study/varsity/blob/master/Resources/Week-2.md) then complete the TODOs in the project

#### From the Flask-Admin Docs

> **Why Flask-Admin?** In a world of micro-services and APIs, Flask-Admin solves the boring problem of building an admin interface on top of an existing data model. With little effort, it lets you manage your web service’s data through a user-friendly interface.

> **How does it work?** The basic concept behind Flask-Admin, is that it lets you build complicated interfaces by grouping individual views together in classes: Each web page you see on the frontend, represents a method on a class that has explicitly been added to the interface.

#### From the Flask-Login Docs

> Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

> It will:
> * Store the active user’s ID in the session, and let you log them in and out easily.
> * Let you restrict views to logged-in (or logged-out) users.
> * Handle the normally-tricky “remember me” functionality.
> * Help protect your users’ sessions from being stolen by cookie thieves.
> * Possibly integrate with Flask-Principal or other authorization extensions later on.

> However, it does not:
> * Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
> * Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
> * Handle permissions beyond “logged in or not.”
> * Handle user registration or account recovery.

## Stretch Challenges

* Hash passwords using bcrypt
* Add other attributes to the User class
* Add a Secrets class
* A User can have many Secrets (db.Relationship)
* Display the secrets in the secrets template

If you you have any questions, feel free to contact Starlight or Sid via Slack.

If you find a typo, or other issue with the repository, please add an issue so that we can address it!

Thank you for your feedback!
