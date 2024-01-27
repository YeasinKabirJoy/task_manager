
# Task Management

A task management app developed with Python-Django

# Project Setup
To run this app locally, you can clone the repository and do the following.

1. Create a virtual environment and activate it for install all the dependencies with the following command in the cloned directory.

```console
$ pip install virtualenv
$ virtualenv venv
$ venv\scripts\activate
```

2. Run the following to install the required dependencies:

```console
$ pip install -r requirements.txt
```

3. Create a .env file. To run this project, you will need to add the following environment variables to your .env file

  DB_NAME
  
  DB_USER
  
  DB_PASSWORD
  
  DB_HOST
  
  DB_PORT

These variables are for the Database connections. Prefered Database is postgreSQ/sqlite.


4. After that run the following commands:

```console
$ python manage.py makemigrations
$ python manage.py migrate
```

5. Then, run the server:

```console
$ python manage.py runserver
```




## API Reference

### API Endpoints

| Method | Endpoints | Action |
| --- | --- | --- |
| POST | /api/create_task | Create new task |
| GET | /api/all_task | To retrieve all the tasks |
| PUT | /api/update_task/:taskID | To update a single task |
| DELETE | /api/delete_task/:taskID | To delete a single task |

