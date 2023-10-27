from src import start
from src.database import get_courses_by_year


course_years = [
    2020,
    2021,
    2022,
    2023
]
for year in course_years:
    for course in get_courses_by_year(year):
        start(course[3])
