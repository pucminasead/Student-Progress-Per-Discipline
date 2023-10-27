from canvasapi.course import Course
from canvasapi.module import Module

def get_course_modules(course: Course):
    """
    Retrieves the modules for a given course and student.

    Args:
        course (Course): The course object.
        student_id (str): The ID of the student.

    Returns:
        PaginatedList with published modules

    """

    modules = course.get_modules(include={'items'})
    return [module for module in modules if module.published]

def get_modules_student_details(course: Course, modules: list, student_id: int):
    """
    Returns a list of module details for a specific student in a course.

    Args:
        course (Course): The course object.
        modules (list): A list of module objects.
        student_id (int): The ID of the student.

    Returns:
        list: A list of module details for the student.

    Raises:
        None.
    """

    return [
        course.get_module(module.id, student_id={f'{student_id}'})
        for module in modules
    ]

def get_module_items_total(module: Module, student_id):
    """
    Returns a list of module items with completion requirements for a specific student in a module.

    Args:
        module (Module): The module object.
        student_id (int): The ID of the student.

    Returns:
        list: A list of module items with completion requirements for the student.

    Raises:
        None.
    """

    items = module.get_module_items(student_id={f'{student_id}'})
    return [item for item in items if getattr(item, "completion_requirement", False)]

def get_completed_items(items):
    """
    Returns the number of completed items from a list of items.

    Args:
        items (list): A list of items.

    Returns:
        int: The number of completed items.

    Raises:
        None.
    """

    return sum(bool(item.completion_requirement['completed'])
           for item in items)
