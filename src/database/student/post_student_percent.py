from ..queries.post_student_percent import execute_query

def post_student_percent(infos: dict):
    execute_query(
        course_sis_id=infos['sis_course_id'],
        student_sis_id=infos['student_cod_pessoa'],
        percent=infos['percent']
    )
