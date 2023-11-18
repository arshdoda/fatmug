#!/bin/bash
nginx -t && nginx -s reload
sudo supervisorctl reread
sudo supervisorctl update
service supervisor restart