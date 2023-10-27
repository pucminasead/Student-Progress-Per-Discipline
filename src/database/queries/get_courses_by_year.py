from ..connection import CURSOR


def execute_query(year):
    query = f"""
        SELECT  TRIM(o.cod_curso_EAD) AS cod_curso_ead,
                o.nom_curso, o.num_oferta, 
                TRIM(co.cod_disciplina_ead) AS cod_disciplina_ead, 
                TRIM(co.nom_disciplina) AS nom_disciplina, year(o.dat_inicio) as ano
        FROM    SAL_EAD..oferta o
        JOIN    SAL_EAD..curriculo_oferta co on o.seq_oferta = co.seq_oferta 
                AND o.origem = co.origem
        WHERE   o.origem = 'EAD' 
                AND o.cod_tipo_curso = 1
                AND o.ind_excluido = 0
                AND o.dat_cancelamento is null
                AND co.ind_excluido = 0
                AND year(o.dat_inicio) >= 2020
                AND o.cod_curso_EAD is not null
                AND co.cod_disciplina_ead is not null
                AND o.seq_oferta in (1020, 1338, 1440, 1470, 1642, 1683, 1697, 1702, 1858, 1878, 1928)
    """
    results = list(CURSOR.execute(query))
    cleaned_results = []

    for row in results:
        cleaned_row = [col.replace('\xa0', '') if isinstance(col, str) else col for col in row]
        cleaned_results.append(cleaned_row)

    return cleaned_results
