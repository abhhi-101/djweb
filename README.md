# DjWeb 
**Intentionally vulnerable Django Web application**

- **Web Framework**: Django - Python-based web framework
- **Database**: MongoDB
- **Platform (developed on)**: Ubuntu 20.04

## How to Install

### Build & start Docker

```bash
git clone https://github.com/abhhi-101/djweb.git     # Clone this repository locally
cd djweb/                                            # Move to the application directory
docker-compose up -d                                 # Run the application in a docker container
```

## Stop the running container:
```bash
docker-compose down
```

### Manually
```bash

git clone https://github.com/abhhi-101/djweb.git     # Clone this repository locally
cd djweb/                                            # Move to the application directory
pip install -r requirements.txt                      # Install python libraries
```
Manually install `mongosh` via https://www.mongodb.com/atlas/database

## Run the application
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver                           # Run server
```

## Features
1. User register
2. User login
3. Admin login
4. Search uses in org
5. Download images via URL
6. Test user login
7. Change user password

## Vulnerabilities
1. Horizontal user account takeover using misconfigured password-reset functionality
2. Reflected Cross site scripting(XSS) in the user search functionality
3. Server-side request forgery(SSRF) in download image via URL functionality
4. Authenication bypass via NoSQL in test user login functionality
5. Werkzeug debugger enabled by default
6. DEBUG=True by default leads to sensitive data exposure

## Refer
https://owasp.org/www-project-top-ten/

https://owasp.org/www-project-pygoat/

