from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM dojos_and_ninjas.dojos;'
        dojos_db = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for i in dojos_db:
            dojos.append(cls(i))
        return dojos

    @classmethod
    def getAllNinjas(cls,data):
        query = 'SELECT * FROM dojos_and_ninjas.dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db['ninjas.id'],
                "first_name": row_from_db['first_name'],
                "last_name": row_from_db['last_name'],
                "age": row_from_db['age'],
                "created_at": row_from_db['ninjas.created_at'],
                "updated_at": row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos_and_ninjas.dojos (name) VALUE (%(name)s);'
        dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return dojo_id