Project Seva
===

## Installation

This installation guide assumes that the application is being installed on the latest version of [Ubuntu](http://www.ubuntu.com/ubuntu).


### Prerequisites

1. Install [Python pip](https://pypi.python.org/pypi/pip) using `sudo apt-get install python-pip`
2. Install [virtualenv](https://pypi.python.org/pypi/virtualenv) using `sudo pip install virtualenv`
3. In the project root, run `virtualenv venv`
4. Activate the virtual environment using `. venv/bin/activate`
5. Once the virtual environment is active, run `pip install -r src/requirements.txt`
6. To deactivate the virtual environment, type `deactivate` and hit ENTER.


### Configuration

All the project configurations are done in the file `settings.py` located at `src/core/settings.py.sample`. Rename it to `settings.py` before adding any configurations or modifying them.  

Some Ideal configurations for development are listed below.


```

DEVELOPMENT = True
DEBUG = True

```


### Setting up the Database

1. Create a `database` with any name you wish.
2. Then change directory to `src/core` using `cd src/core`
3. Run the following command to update the schema from alembic version files using the command, `alembic upgrade head`
4. When you edit the schema and want to sync it to the database, go to `src/core` and run the command `alembic revision --autogenerate -m "<revision_message_here>"`. Here the revision message is a simple short line telling what was changed just like a git commit message. Then run, `alembic upgrade head`


## Development Workflow

1. Rename the `settings.py.sample` using the command, `mv settings.py.sample setting.py`
2. Make appropriate settings in `settings.py`
3. Run the migrations as mentioned in the previous section.
4. Go to `src/scripts` and run `source dev.sh`.
5. Go to `src/` and run the application using, `python run.py` and point your browser to the url that gets displayed.


## Contributing

We love contributors! Clone the repository and start sending us pull requests...  
For a list of things that we'd need help are in the [issues](https://github.com/pesos/ngo-portal/issues) section. That would be your starting point if you are looking to contribute to this project! If you need help in getting started, ping us on #pes-os on IRC (freenode). Look at the Getting Started section for some tutorials and resources to get you started quickly.

Happy hacking!


## Bug Reporting

If you find any bugs, feel free to report it by raising an [issue here](https://github.com/pesos/ngo-portal/issues).


## Authors

The PES OpenSource Team.

List of Contributors (In alphabetical order)

1. [Akshay MS](https://github.com/akshayms)
2. [Sandeep Raju P](https://github.com/sandeepraju)


## License

This project is licensed under the [MIT License](https://github.com/pesos/ngo-portal/blob/seva-flask/LICENSE.txt).


## Getting Started

1. Flask Tutorial - http://flask.pocoo.org/docs/quickstart/
2. Flask Mega Tutorial - http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
