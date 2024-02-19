from src import start
from src.database import get_courses_by_year
import concurrent.futures


courses = get_courses_by_year(1)

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    results = {
        executor.submit(start, course[3]): course[3] for course in courses
    }

    for f in concurrent.futures.as_completed(results):
        course = results[f]
        try:
            data = f.result()
        except Exception as e:
            print(f"{course} generated an exception: {e}")
        else:
            print(course, data) if data else print(course, "FINALIZADO")
