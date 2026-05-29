from typing import Optional


class UniversityCourse:
    def __init__(self, course_name: str, enrolled_students: Optional[list] = None):
        self.course_name = course_name
        # Evitar usar una lista mutables como valor por defecto compartido
        self.enrolled_students = enrolled_students if enrolled_students is not None else []

    def register_student(self, student_name: str):
        """Registra un nuevo alumno en este curso."""
        self.enrolled_students.append(student_name)
        return f"Alumno {student_name} anotado en {self.course_name}."

    def get_total_students(self) -> int:
        """Devuelve la cantidad de alumnos anotados."""
        return len(self.enrolled_students)
    

if __name__ == "__main__":
    course1 = UniversityCourse("Matemáticas")
    course2 = UniversityCourse("Física")

    print(course1.register_student("Alice"))

    print(f"Total estudiantes en {course1.course_name}: {course1.get_total_students()}")
    print(f"Total estudiantes en {course2.course_name}: {course2.get_total_students()}")