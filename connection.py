import psycopg2

# Informações de conexão
def create_connection(host, dbname, user, password, port):
    try:
        connection = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )

        print(connection)
        return connection
    #Estabelecendo a conexão
    except Exception as error:
        print("Erro ao conectar ao PostgreSQL:", error)
        return None