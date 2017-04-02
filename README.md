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
* https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
* https://www.fullstackpython.com/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html
* Interminal type: sudo apt-get install virtualenv python-pip python3-dev
* make a new Directory for the virtualenv: mkdir venv
* specify the system python3 installation: virtualenv --python=/usr/bin/python3 venv/webapp
* to activate the virtualenv: source venv/webapp/bin/activate
* to deactivate the virtualenv: deactivate
* now install flask and Green Unicorn: pip3 install flask gunicorn
* To test that flask works, create a new folder in your main directory and add a file called (i've called mine webApp): __init__.py
* navigate to the main directory.
* Then use gunicorn to run the file (you can also type python3 __init__.py): gunicorn webapp:app
* make a new directory inside the webApp folder, call it "templates"
* in the templates folder add the index.html file

## Installing mySQL
* website: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
* Then install mySQL by typing in the terminal: sudo apt-get install mysql-server
* To set the security on mysql type in the terminal: sudo mysql_secure_installation
* note: you might need to initialise the database (it will abort if you didn't need to) type in terminal: mysqld --initialize
* To test the MySQL is working, type in terminal: systemctl status mysql.service
* If it didn't start on it's own, type in terminal (I used the commmand above): sudo /etc/init.d/mysql start
* you can also test it by connecting to the db by using the admin tool(-u = root and -p = password): mysqladmin -p -u root version
* to stop MySQL, type in terminal(I just hit ctrl+c in the terminal): sudo /etc/init.d/mysql stop
* to uninstall MySQL: sudo apt-get purge mysql*
* then: sudo apt-get autoremove
* then: sudo apt-get autoclean

## using mySQL
* start it up: sudo /etc/init.d/mysql start
* to make go to MySQL interface: sudo mysql -u root -p
* to get help file type in terminal: 'help;' or '\h' for help. Type '\c' to clear current input statement
* to quit type: \q
* to create a database type in terminal(it shoud show mysql> I've called the database listDB): CREATE DATABASE ;
* To select or switch to an existing database type: USE ;
* To show all databases type: SHOW DATABASES;
* To show all tables type: SHOW TABLES;
* To show the columns of a table type: SHOW COLUMNS FROM ;
* To delete a database type: DROP DATABASE IF EXISTS ;
* To delete a table type: DROP TABLE IF EXISTS ;

CREATE TABLE `listDB`.`tbl_user` (
  `user_id` BIGINT UNIQUE AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));
