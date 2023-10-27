from ..queries.get_courses_by_year import execute_query


def get_courses_by_year(year: int):
    return execute_query(year)
