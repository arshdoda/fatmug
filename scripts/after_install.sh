#!/bin/bash



cd /home/ubuntu/app
python3.11 -m venv .venv
source .venv/bin/activate

pip install -r dev-requirements.txt
if [ "$DEPLOYMENT_GROUP_NAME" == "dev-api" ]; then
cp /home/ubuntu/app/server-config/dev-fatmug-gunicorn-supervisor.conf /etc/supervisor/conf.d
fi
if [ "$DEPLOYMENT_GROUP_NAME" == "prod-api" ]; then
cp /home/ubuntu/app/server-config/prod-fatmug-gunicorn-supervisor.conf /etc/supervisor/conf.d
fi

rm -r server-config scripts .github .vscode
rm appspec.yml .gitignore