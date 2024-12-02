from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb+srv://<seu_usuario>:<sua_senha>@<seu_cluster>.mongodb.net/task_manager"
    client = MongoClient(CONNECTION_STRING)
    return client["task_manager"]
