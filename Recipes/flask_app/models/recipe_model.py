from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models.user_model import User




class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.time_frame = data['time_frame']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']


    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, time_frame, created_at, updated_at, users_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(time_frame)s, NOW(), NOW(), %(users_id)s);"
        print(data)
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_all(cls): 
        query = 'SELECT * FROM recipes JOIN users ON users.id = users_id ORDER BY recipes.id;'
        results = connectToMySQL('recipes').query_db(query)
        print(results)
        x = []
        for recipe in results:
            info = cls(recipe)
            data = {
                **recipe,
                'id': recipe['users.id'],
                'created_at': recipe['users.created_at'],
                'updated_at': recipe['users.updated_at']
            }
            users=User(data)
            info.user = users
            x.append(info)
        return x

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL('recipes').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = 'UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, time_frame=%(time_frame)s, updated_at = NOW() WHERE id=%(id)s;'
        results = connectToMySQL('recipes').query_db(query, data)
        return results

    @classmethod
    def delete_recipe(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        results = connectToMySQL('recipes').query_db(query, data)
        return results

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name'])<3:
            flash('Name must be at least 3 characters')
            is_valid = False

        if len(data['description'])<3:
            flash('Description must be at least 3 characters')
            is_valid = False

        if len(data['instructions'])<3:
            flash('Instructions must be at least 3 characters')
            is_valid = False

        if 'date_made' not in data:
            flash('Please enter the date made for your recipe')
            is_valid = False

        return is_valid