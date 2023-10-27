from .canvas import get_course, get_students, get_course_modules, get_module_items_total, get_completed_items, get_modules_student_details
from .calculator import Calculator
from .database import post_student_percent


def start(course_sis_id: str):
    course_canvas = get_course(course_sis_id)
    students = get_students(course_canvas)
    modules = get_course_modules(course_canvas)
    for student in students:
        student_modules = list(get_modules_student_details(course_canvas, modules, student.user_id))
        total_items = [
            get_module_items_total(module, student.user_id) for module in student_modules
        ]
        completed_itens = [get_completed_items(item) for item in total_items]
        export_dict = {
            "course_id": course_canvas.id,
            "sis_course_id": course_sis_id,
            "student_id": student.user_id,
            "student_cod_pessoa": int(student.sis_user_id.split('@')[0]),
            "items_total": sum(len(item) for item in total_items),
            "items_completed": sum(completed_itens)
        }
        calculator = Calculator(export_dict)
        export_dict["percent"] = calculator.get_percent()
        post_student_percent(export_dict)
        