#!/bin/sh

until cd /app/server
do
    echo "Waiting for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

#python manage.py collectstatic --noinput
# for debug
python manage.py createadmin
echo "SuperUser created:: username - fabrique, password - 12345"
python manage.py runserver 0.0.0.0:8000
exec "$@"