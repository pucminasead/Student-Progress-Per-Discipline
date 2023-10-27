

def get_students(course_canvas):
    """
    Returns a list of active student enrollments for a course.

    Args:
        course_canvas: The Canvas object for the course.

    Returns:
        list: A list of active student enrollments.

    Raises:
        None.
    """

    return course_canvas.get_enrollments(type={'StudentEnrollment'}, state={'active'})
