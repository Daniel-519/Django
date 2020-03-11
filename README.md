# DjangoT

To install Django, Python and Pip should be installed.

- Django Install

  $ pip install Django==3.0.4

- This command line can check Django version

  $ python -m django --version

- Creating first project with Django

  $ django-admin startproject <project-name>
  
    Above command will create your first project with follow structure
    
    <project-name>/
  
        manage.py
        
        <project-name>/
        
            __init__.py
            
            settings.py
            
            urls.py
            
            asgi.py
            
            wsgi.py
            

- Run first project

  $ python manage.py runserver
  

- Creating first APP

  $ python manage.py startapp <app-name>
  
  this will create follow file structure.
  
  <app-name>/
  
    __init__.py
    
    admin.py
    
    apps.py
    
    migrations/
    
        __init__.py
        
    models.py
    
    tests.py
    
    views.py
    
    
  To configure app url, need to add urls.py file in app directory.
  

- Database setup

  Now, open up mysite/settings.py. It’s a normal Python module with module-level variables representing Django settings.
  By default, the configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. When starting your first real project, however, you may want to use a more scalable database like PostgreSQL, to avoid database-switching headaches down the road.
  If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:
  ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'. Other backends are also available.
  NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.


