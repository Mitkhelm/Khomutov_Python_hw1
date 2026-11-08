import uuid
import settings
from db import Database


db = Database(settings.DB_CONNECTION)


def create_test_email():
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def test_add_user():
    #Тест добавления пользователя
    email = create_test_email()
    db.execute_script("insert_teacher", {
        "email": email,
        "teacher_id": 1
    })
    rows = db.select_script("select_teacher_by_email", {"email": email})

    assert len(rows) == 1
    assert rows[0]["email"] == email

    db.execute_script("delete_teacher_by_email", {"email": email})


def test_update_user_subject():
    #Тест изменения предмета пользователя
    email = create_test_email()
    db.execute_script("insert_teacher", {
        "email": email,
        "teacher_id": 1
    })

    db.execute_script("update_teacher_by_email", {
        "email": email,
        "teacher_id": 2
    })

    rows = db.select_script("select_teacher_by_email", {"email": email})

    assert rows[0]["teacher_id"] == 2

    db.execute_script("delete_teacher_by_email", {"email": email})


def test_delete_user():
    #Тест удаления пользователя
    email = create_test_email()

    db.execute_script("insert_teacher", {
        "email": email,
        "teacher_id": 1
    })

    rows_before = db.select_script("select_teacher_by_email", {"email": email})
    assert len(rows_before) == 1

    db.execute_script("delete_teacher_by_email", {"email": email})
    rows_after = db.select_script("select_teacher_by_email", {"email": email})
    assert len(rows_after) == 0
