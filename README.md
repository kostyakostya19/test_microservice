# __test_microservice__
---
How to run api_service:
```
cd api_service
source .venv/bin/activate
pip3 install requirements.txt
gunicorn -c gunicorn_conf.py src.main:app
```
---
## __RabbitMQ__
### set new user
```
sudo rabbitmqctl add_user myuser mypassword
sudo rabbitmqctl set_user_tags myuser administrator
sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
```
