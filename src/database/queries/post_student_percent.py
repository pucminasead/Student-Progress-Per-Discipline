# from ..connection import conn
import pyodbc
from decouple import config


def execute_query(course_sis_id, student_sis_id, percent):
    print(
        f"Updating student {student_sis_id} in course {course_sis_id} with {percent}%"
    )
    conn = pyodbc.connect(
        f"""DRIVER={config("DATABASE_DRIVER")};
    SERVER={config("DATABASE_HOST_SAL_EAD")}, {config("DATABASE_PORT_SAL_EAD")};
    DATABASE={config("DATABASE_NAME_SAL_EAD")};
    UID={config("DATABASE_USER_SAL_EAD")};
    PWD={config("DATABASE_PASS_SAL_EAD")};
    TrustServerCertificate=yes;"""
    )
    query = f"""
        update m set percentual_conclusao_disciplina = {percent}
        from SAL_EAD..matricula m
        join SAL_EAD..curriculo_oferta co on m.seq_curriculo_oferta = co.seq_curriculo_oferta and m.origem = co.origem
        join SAL_EAD..aluno a on m.cod_aluno = a.cod_aluno and m.origem = a.origem
        where 
        m.origem = 'EAD' 
        and a.dsc_login_cod_pessoa = {student_sis_id}
        and co.cod_disciplina_ead = '{course_sis_id}'
    """
    CURSOR = conn.cursor()
    CURSOR.execute(query)
    CURSOR.commit()
    CURSOR.close()
