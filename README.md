# JW_congregation_management


## Introduction

This is a secondary web page for JW members. I'm making the necessary functions.

Template is written with `python3.8` and `Django4.0`

![Default Home View](__screenshots/home.png?raw=true "Title")

### Main features

* Separated dev and production settings

* tailwind css

## Usage

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/JW_congregation_management.git
    $ cd JW_congregation_management
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver