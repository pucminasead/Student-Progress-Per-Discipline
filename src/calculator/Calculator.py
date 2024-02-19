
class Calculator:
    """
    Represents a calculator.

    Args:
        student_data (dict): A dictionary containing student data.

    Attributes:
        course_id (str): The ID of the course.
        student_id (str): The ID of the student.
        items_total (int): The total number of items.
        completed_items (int): The number of completed items.

    Methods:
        get_percent: Calculates and returns the percentage of completed items.

    """

    def __init__(self, student_data: dict):
        """
        Initializes a Calculator instance.

        Args:
            student_data (dict): A dictionary containing student data.

        """
        self.course_id = student_data['course_id']
        self.student_id = student_data['student_id']
        self.items_total = student_data['items_total']
        self.completed_items = student_data['items_completed']

    def get_percent(self) -> str:
        """
        Calculates and returns the percentage of completed items.

        Returns:
            str: The percentage of completed items formatted as a string with two decimal places.

        """
        if self.items_total == 0:
            return None
        percentual = (self.completed_items / self.items_total) * 100
        return round(percentual, 2)
