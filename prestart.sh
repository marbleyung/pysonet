sleep 1;
python manage.py makemigrations
python manage.py migrate

sleep 1;
python manage.py runserver 0.0.0.0:8000