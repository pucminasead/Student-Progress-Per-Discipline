# from ..connection import conn
import pyodbc
from decouple import config


def execute_query(year):
    conn = pyodbc.connect(
        f"""DRIVER={config("DATABASE_DRIVER")};
        SERVER={config("DATABASE_HOST_SAL_EAD")}, {config("DATABASE_PORT_SAL_EAD")};
        DATABASE={config("DATABASE_NAME_SAL_EAD")};
        UID={config("DATABASE_USER_SAL_EAD")};
        PWD={config("DATABASE_PASS_SAL_EAD")};
        TrustServerCertificate=yes;"""
    )
    
    query = f"""
        SELECT
                DISTINCT TRIM(o.cod_curso_EAD) AS cod_curso_ead,
                o.nom_curso,
                o.num_oferta,
                TRIM(co.cod_disciplina_ead) AS cod_disciplina_ead,
                TRIM(co.nom_disciplina) AS nom_disciplina,
                year(o.dat_inicio) as ano,
                o.cod_curso
        FROM
                SAL_EAD..oferta o
        JOIN SAL_EAD..curriculo_oferta co on
                o.seq_oferta = co.seq_oferta
                AND o.origem = co.origem
        JOIN SAL_EAD..matricula m on
                m.seq_curriculo_oferta = co.seq_curriculo_oferta
                and m.origem = co.origem
        WHERE
                o.origem = 'EAD'
                AND o.cod_tipo_curso = 1
                AND o.ind_excluido = 0
                AND o.dat_cancelamento is null
                AND co.ind_excluido = 0
                AND year(o.dat_inicio) >= 2020
                AND o.cod_curso_EAD is not null
                AND co.cod_disciplina_ead is not null
                -- AND m.cod_aluno = 1118751
        ORDER BY o.cod_curso, o.num_oferta;
    """
    CURSOR = conn.cursor()
    results = list(CURSOR.execute(query))
    CURSOR.close()
    cleaned_results = []

    for row in results:
        cleaned_row = [
            col.replace("\xa0", "") if isinstance(col, str) else col for col in row
        ]
        cleaned_results.append(cleaned_row)

    return cleaned_results
