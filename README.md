# ZookeeperClient
This is a practice for zookeeper kafka docker server and client side with python function.
kazoo 2.8.0 for windows

- **deploy**:
    - `git clone https://github.com/yuzu0230/ZookeeperClient.git`
    - `cd ZookeeperClient`
    - `pip install virtualenv`
    - `virtualenv venv`  
        - macOS - `source venv/bin/activate`  
        - Windows - `.\\venv\Scripts\activate`
    - `pip install -r requirements.txt`
    
- **run**:
    - `docker-compose up -d --remove-orphans`

- **freeze requirements**
    - `python -m pip freeze > requirements.txt` or
    - `pip freeze > requirements.txt`

- **create topic**
    - `KafkaClient2.py`
    - should run at first time

- **data resource**
    - [eCommerce behavior data from multi category store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
    - random sample 10,000