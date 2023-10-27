from ..connection import CURSOR

def execute_query(course_sis_id, student_sis_id, percent):
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
    CURSOR.execute(query)
    CURSOR.commit()
    