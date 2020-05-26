# Callback News API

## About the backend demons team.

:robot: ### Erik Sánchez- Scrapper Master.

The supreme architect of the universe inside the news scrapper. 

:martial_arts_uniform: ### Iraida Barreto - Django developer ninja.

Mastering the ancient python kung-fu technique to create a Django service hat transcends the time.

:sparkles: ### Gerardo Márquez - Deployment wizard.

Infrastructure and devops superpowers combined to structure the app in defferents services.

## How I deploy this project?

1. First, clone this repo with `git clone`.

2. Create enviroment file .env.dev hat satifies the emty values below:
   
```bash
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=callback_news
SQL_USER=<setuser>
SQL_PASSWORD=<setpasword>
SQL_HOST=postgres
SQL_PORT=5432
```
if you want to set your own values for pgadmin, change them in the docker.compose.yml, in the pgadmin section.

3. Build the container with `docker-compose build` (Make sure you have docker and docker compose installed in you machine)
4. Once docker image is installed, turn it on with `docker-compose up`.
5. Run migration of the models set with `docker-compose exec django python manage.py makemigrations`.
6. Then run `docker-compose exec django python manage.py migrate` to complete the migration process.
7. Set you user in django administration IDE with `docker-compose exec django python manage.py createsuperuser`
8. Set values and the go to [localhost/8080/admin](localhost/8000/admin) to access.
9. To sing in the pgadmin IDE go to [localhost/8000/admin](localhost/8000/admin) and join with your credentials..


