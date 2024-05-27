# LeitorFaturas

Sistema de leitura de arquivo pdf em pyhon utilizando a biblioteca PyPDF2

Sistema ler um arquivo e salva as informações específicas em um banco de dados postgresSQL.

Para executar a aplicação de extrator de texto em arquivo PDF, basta rodar o arquivo main.py

python main.py

Importante salientar que deve ser configurado o banco de dados de acordo com o banco utilizado como teste

criar a tabela "faturas"

create table faturas (
  id serial not null,
  description text not null
)

#instalar as seguintes bibliotecas
##pypdf2
##psycopg2
