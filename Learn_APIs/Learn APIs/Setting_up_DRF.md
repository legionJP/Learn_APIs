#
# Installing and Setting-UP DRF 

# 1. Using the pipenv 
```
1. pipenv (Python Packaging Tool)
pipenv install (will install Pipenv environment)
pipenv install <package>
pipenv shell

```
```markdown
# Key Differences:

# venv:
 Provides isolation by creating a new Python environment, but doesn't manage dependencies or virtual environments automatically.
 
# pipenv: 
Combines the features of pip and venv for easier management of Python environments and dependencies. It also includes a locking mechanism with the Pipfile and Pipfile.lock.

# pip: 
 The package manager used to install packages. It can be used within virtual environments (created by venv), but doesn't handle the creation of environments itself.
```

# 2 Install Django 
- pipenv install Django
- pipenv shell  (to activate)

- django-admin startproject BookLis
- python manage.py startapp BookListAPI

# Install Rest Framework : 
    - pipenv install djangorestframework
    # Or pip3 install djangorestframework

