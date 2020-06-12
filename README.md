# Illinois Computer Science Sail Website
Source code for Illinois CS Sail's new website, which will be deployed at the start of the fall semester, replacing [the current look](https://sail.cs.illinois.edu/). This website features a clean interface for teacher & student registration, creating and editing courses (for teachers), viewing and signing up for courses (for students), and more. The motivation for completely rebuilding the website is so that there is a simple and well-documented code base, so that future staff members can easily add/remove functionality to the website.

Setup
-----
First, make sure you have Python 3 (and pip) installed. Clone the repository and cd into the project directory. Then, run the following commands.

1. `pip install virtualenv` to install the [Virtualenv](https://virtualenv.pypa.io/en/latest/) package
2. `virtualenv venv` to create a virtual environment named venv
3. `source venv/bin/activate` (on Linux) or `./venv/Scripts/activate` (on Windows) to activate the virtual environment. To exit later, type `deactivate`
4. `pip install -r requirements.txt` to install all dependencies

Running the site
-----
Before running the site, remember to activate your virtual environment first (as described above). Then, to create an empty SQLite database that you can test on, run `python manage.py migrate`. To access [Django admin](https://localhost:8000/admin), you need to first create a superuser with `python manage.py createsuperuser`. After these steps, you can simply run `python manage.py runserver` and see the website at [https://localhost:8000](https://localhost:8000). To stop the server, press Ctrl + C. As you make changes, the Django server will reload automatically so you do not need to manually stop and start the server.
