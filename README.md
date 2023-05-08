# pysonet
in early development
prototype of mini social media using Python + DRF
_
git clone 
_ 
create .env.dev 
DEBUG=1
SECRET_KEY=YOUR_SECRET_KEY
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_pass
POSTGRES_HOST=db_host
POSTGRES_PORT=5432

DATABASE=postgres
_
docker-compose build
docker-compose up
_
run migrations if neccessary
'python manage.py makemigrations'
'python manage.py migrate'
_
create superuser:
docker ps -a
(copy the id of the container)
docker exec -it (id) bash
python manage.py createsuperuser
(type your data)
_
after successfull superuser creation
go to http://127.0.0.1:8000/swagger/
here will be a swagger documentation
