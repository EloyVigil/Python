# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('userscr').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , occupation , email,  created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , %(email)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('userscr').query_db( query, data )
    
    @classmethod
    def select(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        print("inside select")
        results =  connectToMySQL('userscr').query_db( query, data )
        return cls(results[0])

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        results =  connectToMySQL('userscr').query_db( query, data )
        return results
    
    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, occupation = %(occ)s, email = %(email)s WHERE id = %(id)s;"
        results =  connectToMySQL('userscr').query_db( query, data )
        print(results)
        return results
