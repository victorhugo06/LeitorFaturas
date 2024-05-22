import os
from PyPDF2 import PdfReader
import psycopg2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def main():
    # Diretório onde os arquivos PDF estão localizados
    pdf_directory = 'D:/leitor_pdf/LeitorFaturas/Instalação_ 3004298116'
    
    # Conexão com o banco de dados
    connection = psycopg2.connect(
        dbname="uriboca",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

    try:
        cursor = connection.cursor()
        
        # Listar todos os arquivos PDF no diretório
        pdf_files = [os.path.join(pdf_directory, f) for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
        
        count = 0
        while count < 12 and count < len(pdf_files):
            file_path = pdf_files[count]
            text = extract_text_from_pdf(file_path)
            text_lines = text.split('\n')
            
            # Inserir texto no banco de dados
            insert_query = "INSERT INTO faturas (description) VALUES (%s);"
            cursor.execute(insert_query, (text_lines,))
            connection.commit()
            
            print(f"Texto do PDF {count + 1} inserido com sucesso no banco de dados.")
            count += 1

    except Exception as error:
        print("Erro ao executar a inserção no banco de dados:", error)
    finally:
        cursor.close()
        connection.close()
        print("A conexão com o PostgreSQL foi fechada.")

if __name__ == "__main__":
    main()
