from canvasapi.course import Course
from src.canvas import CANVAS

def get_course(course_sis_id: str) -> Course:
    """
    Returns the course with the given course ID.

    Args:
        course_sis_id (str): The ID of the course.

    Returns:
        Course: The course object.

    Raises:
        ValueError: If the course ID is invalid.
    """

    return CANVAS.get_course(course_sis_id, True)
