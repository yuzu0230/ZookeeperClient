# ZookeeperClient
This is a practice for zookeeper kafka docker server and client side with python function.
kazoo 2.8.0 for windows

python -m venv venv
venv/Scripts/Activate
python -m pip install -r requirements.txt
docker-compose up -d --remove-orphans

python -m pip freeze > requirements.txt
