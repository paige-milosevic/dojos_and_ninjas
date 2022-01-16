
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos_and_ninjas.ninjas;'
        ninjas_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for i in ninjas_db:
            ninjas.append(cls(i))
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
