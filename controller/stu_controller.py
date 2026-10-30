
from fastapi import HTTPException
from models.stu_model import Student, StudentCreate

students = []
student_id = 0


# Get all students
def get_students_all_controller():
    return students


# Create a student
def create_student_controller(student: StudentCreate):
    global student_id

    student_id += 1

    new_student = Student(
        id=student_id,
        **student.model_dump()
    )

    students.append(new_student)

    return new_student


# Get student by ID
def get_student_controller(studentid: int):
    for student in students:
        if student.id == studentid:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Update student
def update_student_controller(studentid: int, student: StudentCreate):

    for index in range(len(students)):

        if students[index].id == studentid:

            updated_student = Student(
                id=studentid,
                **student.model_dump()
            )

            students[index] = updated_student

            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Delete student
def delete_student_controller(studentid: int):

    for student in students:

        if student.id == studentid:

            students.remove(student)

            return {"message": "Student deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Search student by course
def search_student_controller(course: str):

    result = []

    for student in students:

        if course.lower() in student.course.lower():
            result.append(student)

    return result
