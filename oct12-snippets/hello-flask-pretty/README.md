# Sample MovieDB app

## Description
This is a sample Flask web app which connects to the MySQL database on a remote server and exposes two APIs - 
one to add new movies to the database and the other to show all movies in the database.

## Requirements
Before setting up and running this sample app, you should have completed the following steps.
1. Create a user on the remote azure server.
2. Log in to the azure server and create a user on th MySQL server.
3. Create a database for this sample project on the MySQL server. Or use any existing database if you have already 
created one.

## Setup
1. `ssh <linux-username>@20.88.14.242`
2. `wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh` This will install Miniconda. 
You will be able to create virtual conda environments and isolate your project dependencies from the global packages.
3. Log in to the MySQL server using your MySQL credentials and create a sample table.
   1. `mysql -u <mysql-username> -p`
   2. `use <database-name>`
   3. `CREATE TABLE MyMovies(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(256) NOT NULL, genre VARCHAR(64) NOT NULL, length INT NOT NULL);`
   4. `exit`
4. `git clone git@github.com:uiuc-fa21-cs411/hello-world.git`
5. `cd hello-world`
6. `conda env create --file conda_env.yaml` This will create a new conda environment for this sample app and install 
the exact dependencies mentioned in `conda_env.yaml`.
7. Edit line 6 in `app.py` to add your own MySQL credentials and database name. The database should be the same as the
one used in step 3.2.
8. `conda activate cs411-sample-moviedb` Run this command before installing any other dependencies. It will ensure that
all your packages are isolated from server-wide updates/installations.
9. `flask run --host=0.0.0.0 --port=10001` Run the app at port 10001. You can change it to any other available port in case 10001 is occupied.
10. Add some movies at 20.88.14.242:10001. They should show up in a list at 20.88.14.242:10001/showall. Happy hacking!


conda activate cs411-hello-flask

FLASK_APP=app.py FLASK_DEBUG=1 flask run
 