# Django Debug tool Bar

- pipenv shell
- pipenv install django-debug-toolbar

- add the debug_toolbar the settings.py installed app
- map the '__debug__' toolbar in project urls.py 
- add the debug_toolbar in the middleware 
- add the below config 
```python
INTERNAL_IPS = {
    '127.0.0.1'
}
```
http://127.0.0.1:8000/api/books/