from conftest import Student


def test_add_student(db_session):
    new_student = Student(name="John Doe", age=25)
    db_session.add(new_student)
    db_session.commit()

    assert new_student.id is not None


def test_update_student(db_session):
    student = db_session.query(Student).filter_by(name="John Doe").first()
    student.age = 26
    db_session.commit()

    updated_student = db_session.query(
        Student).filter_by(name="John Doe").first()
    assert updated_student.age == 26


def test_delete_student(db_session):
    student = db_session.query(Student).filter_by(name="John Doe").first()
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(
        Student).filter_by(name="John Doe").first()
    assert deleted_student is None
