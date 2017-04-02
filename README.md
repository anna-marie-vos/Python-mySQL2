# Python-mySQL2
A new Python serverside webpage with mySQL

# Python Installation:
* On linux, python is already installed, to check the version type: python3 --version
* or(for python 2): python --version
* to find out which python to use type(in the terminal, this will output '/usr/bin/python3'): which python3

* If your not using a virtual environment install pip and flask like this:
* to install pip (It's like npm) type in terminal: sudo apt-get install python3-pip
* to install flask type: sudo pip3 install flask

# The virtualenvironment
* Virtualenv allows you to easily package your application for production
* because you can install only the packages you need and you've got an automatic package isolation.
* Generating a requirements.txt is then as simple as pip freeze > requirements.txt.
* Remeber that if you end using a virtualenv, you must not use sudo to install packages as they will be installed outside the virtualenv

# Tutorial
* this a really great website: https://www.fullstackpython.com/table-of-contents.html
* https://www.fullstackpython.com/wsgi-servers.html

## Install a virtualenv:
* https://www.fullstackpython.com/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html
* Interminal type: sudo apt-get install virtualenv python-pip python3-dev
* make a new Directory for the virtualenv: mkdir venv
* specify the system python3 installation: virtualenv --python=/usr/bin/python3 venv/webapp
* to activate the virtualenv: source venv/webapp/bin/activate
* to deactivate the virtualenv: deactivate
* now install flask and Green Unicorn: pip3 install flask gunicorn
* To test that flask works, create a new folder in your main directory and add a file called (i've called mine webApp): __init__.py
* navigate to the main directory.
* Then use gunicorn to run the file (you can also type python __init__.py): gunicorn webApp:app
* It will run on localhost:8000/
