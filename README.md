## Walmart Sales Prediction

### 1. Prerequisite
- Python
- Pip

Commands

    py -m pip --version

#### if not install pip
    py -m pip install --upgrade pip

### 2. Install and Activate Environment

    py -m venv venv
    venv\Scripts\activate

To deactivate the environment use
    
    deactivate

### 4. Install flask server to run the application
    pip install flask

### 5. Install required packages
    pip install sklearn
    pip install pandas
    pip install numpy

Note: Refer to app.py for more which package to install.

### 6. Run Application
    flask run

### 7. Access the project at
    http://127.0.0.1:5000/

Note: If you want to run the project via flask environment 

### Install python-dotenv for using enviroment (optional)
    pip install python-dotenv

#### Then set the Environment 
    set FLASK_APP=app.py

## Deployment guide

    pip install gunicorn
    pip freeze > requirements.txt

## Deployment to heroku guide

    heroku login
    git commit -m "herokyu deployment-test added files" -a // Note: only if required to commit
    heroku git:remote -a sales-prediction-walmart
    
    git push heroku dev:main

## Useful Heroku commands
    heroku run bash -a sales-prediction-walmart // to view all folder structures