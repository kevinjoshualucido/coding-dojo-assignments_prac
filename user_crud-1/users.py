from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        all_users = []
        for user in results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def show_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL("users_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW());"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)
        return results

    @classmethod
    def delete_user(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": id}
        results = connectToMySQL("users_schema").query_db(query, data)
        return results
