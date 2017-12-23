#!/bin/bash
res=0
while [ $res -ne 52 ]
do
	sleep 1
	curl -s $WEBSITE_DATABASE_HOST:5432
	res=$?
done

res=6
while [ $res -eq 6 -o $res -eq 7 ]
do
	sleep 1
	curl -s $DATA_DATABASE_HOST:3306
	res=$?
done

cd Product/APIManager &&
python manage.py makemigrations &&
python manage.py migrate &&
echo "yes" | python manage.py collectstatic &&
python manage.py create_user &&

if [ ${PRODUCTION:-0} -eq 1 ]; then
	gunicorn project_config.wsgi --access-logfile '-' -b 0.0.0.0:8000
else
	gunicorn project_config.wsgi --reload --access-logfile '-' -b 0.0.0.0:8000
fi
