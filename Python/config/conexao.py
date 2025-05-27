import psycopg2

def conexaoBD():
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = '67ju4p',
            host = 'localhost',
            port = '5432'
        )
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {repr(e)}")
        return None

conexaoBD()