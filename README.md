# logistics-app

App for support in the church logistics

## How to run the application for development
 1. Create virtual environment and activate
 ````
 virtualenv --python=python3 --always-copy venv
 . venv/bin/activate
 ````
 2. Install requirements
 ````
 pip install -r requirements
 ````
 3. Set debug env variable
 ````
 export FLASK_DEBUG=True
 ````
 4. Run
 ````
 python manage.py run
 ````