from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_models
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.reapers=[]

    @classmethod
    def add_dojo(cls, data):
        query = 'INSERT INTO dojos (name, created_at) VALUES(%(name)s, NOW())'
        return connectToMySQL('dojo_and_ninjas').query_db(query, data)

    @classmethod
    def get_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results =  connectToMySQL('dojo_and_ninjas').query_db( query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_all(cls, data): 
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojo_and_ninjas').query_db(query, data)
        x = cls(results[0])
        for ninja in results:
            ninjas = {
                'id': ninja['ninjas.id'],
                'first_name': ninja['first_name'],
                'last_name': ninja['last_name'],
                'age': ninja['age'],
                'created_at': ninja['ninjas.created_at'],
                'updated_at': ninja['ninjas.updated_at'],
                'dojo_id' : ninja['dojo_id']
            }
            x.reapers.append(ninja_models.Ninja(ninjas))
        return x

