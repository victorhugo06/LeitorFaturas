import PyPDF2
from connection import create_connection

pdf = open('Boleto_CLAUDIA CAROLINE AVELINO LEAL_29_06_2024_698038984.pdf','rb')
reader = PyPDF2.PdfReader(pdf)
pagina = reader.pages[0]

text = pagina.extract_text()

text2 = text.split('\n')

text3 = text.split('\n')[2]

text4 = text3.split(': ')

string = ''
for elemento in text4:
    string += "'"+elemento + "',"

print(string)

# Defina as credenciais de conexão
host = "localhost"
dbname = "uriboca"
user = "postgres"
password = "123456"
port = "5432"  # Normalmente 5432 para PostgreSQL

# Estabeleça a conexão usando a função importada
connection = create_connection(host, dbname, user, password, port)

if connection:
    try:
        cursor = connection.cursor()

        # Defina a consulta SQL para inserir o texto no banco de dados
        insert_query = f"INSERT INTO faturas (name,value,save_at) VALUES ({string}'21/05/2024');"
        
        # Execute a consulta passando o texto extraído
        cursor.execute(insert_query, (string,))
        
        # Faça o commit das mudanças
        connection.commit()
        
        print("Texto inserido com sucesso no banco de dados.")
        
        # Feche o cursor
        cursor.close()
    except Exception as error:
        print("Erro ao executar a inserção no banco de dados:", error)
    finally:
        # Feche a conexão
        connection.close()
        print("A conexão com o PostgreSQL foi fechada.")
else:
    print("Não foi possível estabelecer uma conexão com o banco de dados.")