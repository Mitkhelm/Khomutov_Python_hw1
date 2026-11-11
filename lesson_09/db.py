from sqlalchemy import create_engine, text


class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.scripts = {
            "clean_test_teacher":
                "DELETE FROM teacher WHERE email LIKE '%@example.com'",
            "insert_teacher":
                "INSERT INTO teacher(teacher_id, email) "
                "VALUES (:teacher_id, :email)",
            "select_teacher_by_email":
                "SELECT * FROM teacher WHERE email = :email",
            "update_teacher_by_email":
                "UPDATE teacher SET teacher_id = :teacher_id "
                "WHERE email = :email",
            "delete_teacher_by_email":
                "DELETE FROM teacher WHERE email = :email"
        }

    def execute_script(self, script_name, params=None):
        if params is None:
            params = {}
        with self.engine.connect() as conn:
            with conn.begin():
                return conn.execute(text(self.scripts[script_name]), params)

    def select_script(self, script_name, params=None):
        if params is None:
            params = {}
        with self.engine.connect() as conn:
            result = conn.execute(text(self.scripts[script_name]), params)
            return result.mappings().all()
