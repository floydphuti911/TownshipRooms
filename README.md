# TownshipRooms
Find and Compare rooms to rent

[ ![Codeship Status for floydflava/TownshipRooms](https://app.codeship.com/projects/edafe3f0-f749-0135-594b-7af7195f2991/status?branch=master)](https://app.codeship.com/projects/275358)
Installation
==

To get started, first install the [Heroku Toolbelt](https://toolbelt.heroku.com/).
This will provide access to the necessary command-line tools.

Prepare the virtualenv you'll be using with the following commands:

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt

Then copy `env.sample` to `.env`.
Foreman uses this file to set environment variables when running commands.
Create a new PostgreSQL database and set the access information.

Issue the following commands to create the database and apply any migrations.

    heroku local:run python manage.py migrate

You're now all set for local development, to start the development server, simply run

    heroku local:run python manage.py runserver

You can then access the local development server at [`http://localhost:8000/`](http://localhost:8000/).


Deployment
==

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The project is already set up for easy deployment with Heroku by clicking the button above.
Note that you will be warned if your account will be charged for the addons installed.
While I make no guarantees, I have attempted to select only free addons which leave room to upgrade.
You are still responsible for verifying any fees associated with any addons which will be installed.

For the first deploy, and each new deploy, simply run `git push heroku master`.
Initially, and when the schema changes, run `migrate`.

    heroku run python manage.py migrate

You can view your new deployment in your browser via `heroku open`.
Static file serving can be modified to use Google Console Storage.
Create a bucket on GC and add the configuration to your Heroku installation.

    heroku config:add GOOGLE_APPLICATION_CREDENTIALS="$( cat <GCS CREDENTIALS JSON>)"

If using S3, you will find `collectstatic` takes a long time to run on every deploy.
To disable running automatically, simply set `DISABLE_COLLECTSTATIC=1`.
You can then manually run `collectstatic` via

    heroku run python manage.py collectstatic --noinput


Dependency management
==

To add a new dependency to your project, simply install via `pip install` after activating the virtualenv.
To track newly installed packages, run `pip freeze -l > requirements.txt` to update the requirements file.
Note that you should manually remove `setuptools` or `distribute` if they appear in this file as this can cause slug compilation to fail.
