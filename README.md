# Callback News API

Callback-News.com is an online technology newspaper that gets its news through external newspapers.


Callback-News.com has the news updated daily so you do not miss your dose of tech.


The newspaper is managed by an admin panel in Python, gets the news automatically and has its frontend in NextJs (React).

### 🚀 Links

 * **Website:** https://api.callback-news.com/
 * **Documentation:** https://www.notion.so/Callback-News-8f7835b5467b4ca89efe35607d9abad7
 * **Mockup:** https://www.notion.so/670629e5706d445f8fe08c876ba33d63?v=7ff2443196594df298333cfdcb746970

### 🛠 Installation

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

### 🖥 Execution

**Development Environment**
```
```

>This project runs on **http://localhost:8080**
**Production Environment**

```
```


### 🛠️ Technologies

  * Python
  * Django
  * PostgreSQL

### ✒️ Authors

* **Erik Sanchez** - [eriksape](https://github.com/eriksape)
* **David Behar** - [behagoras](https://github.com/behagoras)
* **Iraida Mercedes** - [iraida07](https://github.com/iraida07)
* **William Velazquez** - [WilliamVelazquez](https://github.com/WilliamVelazquez)
* **Gerardo Marquez** - [GerardoMarquezC](https://github.com/GerardoMarquezC)

If you want to know about the insights [click here!](https://github.com/callback-demons/callback-news-api/pulse/monthly)

### 🎁 Contribute

Feel free to contribute to the project!
