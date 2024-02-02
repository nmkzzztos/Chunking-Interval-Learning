# Backend

### Prerequisites

Before proceeding, ensure you have Python installed on your system. Python 3.8 or higher is recommended. You can download Python from the [official website](https://www.python.org/downloads/)

If `pip` isn’t already installed, then first try to bootstrap it from the standard library:
```sh
py -m ensurepip --default-pip
```

### Environment Setup
To set up a virtual environment, follow these steps:

Create vurtial environment
```sh
python -m venv env
```
    
Activate virtual evironment
```sh
venv/scripts/activate
```

### Dependencies
Once your virtual environment is active, you can install the required dependencies. The backend relies on Flask, Flask-Cors for handling Cross-Origin Resource Sharing (CORS), Flask-SQLAlchemy for ORM, and several other packages for various functionalities.

To install the required packages, ensure you have the `requirements.txt` file in your project directory with following dependencies:
```sh
blinker==1.6.3
click==8.1.7
colorama==0.4.6
Flask==3.0.0
Flask-Cors==4.0.0
Flask-SQLAlchemy==3.1.1
greenlet==3.0.1
itsdangerous==2.1.2
Jinja2==3.1.2
Mako==1.3.1
MarkupSafe==2.1.3
SQLAlchemy==2.0.23
typing_extensions==4.8.0
Werkzeug==3.0.1
```

### Installation of Dependencies
Install them by running:
```sh
pip install -r requirements.txt
```

### Running Backend
To run backend locally:

```sh
python app/app.py
```

### Contact

Anton Guliaev
[Mail](nmkzzztos@gmail.com)
[GitHub](https://github.com/nmkzzztos)
[LinkedIn](https://www.linkedin.com/in/nmkzzztos/)
