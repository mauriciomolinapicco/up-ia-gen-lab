class UniversityCourse:
    # BUG SUTIL: Usar un objeto mutable (una lista vacía `[]`) 
    # como valor por defecto en los argumentos de un método.
    def __init__(self, course_name: str, enrolled_students: list = []):
        self.course_name = course_name
        self.enrolled_students = enrolled_students

    def register_student(self, student_name: str):
        """Registra un nuevo alumno en este curso."""
        self.enrolled_students.append(student_name)
        return f"Alumno {student_name} anotado en {self.course_name}."

    def get_total_students(self) -> int:
        """Devuelve la cantidad de alumnos anotados."""
        return len(self.enrolled_students)