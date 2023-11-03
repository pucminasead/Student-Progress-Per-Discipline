import pyodbc
from decouple import config


conn = pyodbc.connect(
    f'''DRIVER={config("DATABASE_DRIVER")};
    SERVER={config("DATABASE_HOST_SAL_EAD")}, {config("DATABASE_PORT_SAL_EAD")};
    DATABASE={config("DATABASE_NAME_SAL_EAD")};
    UID={config("DATABASE_USER_SAL_EAD")};
    PWD={config("DATABASE_PASS_SAL_EAD")};
    TrustServerCertificate=yes;'''
)
# CURSOR = conn.cursor()
