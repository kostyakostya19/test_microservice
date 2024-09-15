# __test_microservice__
---
How to run api_service:
```
cd api_service
source .venv/bin/activate
pip3 install requirements.txt
python3 src/main.py
```
---
## __RabbitMQ__
### set new user
```
sudo rabbitmqctl add_user myuser mypassword
sudo rabbitmqctl set_user_tags myuser administrator
sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
```
---
# future plan
- [ ] add k8s
- [ ] add uvicorn config
- [x] prepare ansible directory