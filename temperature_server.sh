#!/bin/bash
LOGFILE=/home/deploy/www/temperature_server/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
USER=deploy
ADDRESS=sztosz.tk:9876
source /home/deploy/venv/temperature_server/bin/activate
cd /home/deploy/www/temperature_server
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w ${NUM_WORKERS} --bind=${ADDRESS} --user=${USER} \
        --log-level=error --log-file=${LOGFILE} 2>>${LOGFILE} temperature_server.wsgi:application
