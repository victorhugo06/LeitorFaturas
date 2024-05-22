# LeitorFaturas

Sistema de leitura de arquivo pdf em pyhon utilizando a biblioteca PyPDF2

Sistema ler um arquivo e salva as informações específicas em um banco de dados postgresSQL.

#instalar as seguintes bibliotecas
##pypdf2
##flask_sqlalchemy
##flask
##psycopg2

#API

##TESTE DE API utilizando flask

Para subir a api, basta dar um "python app.py".

##DELETE
curl -X DELETE http://localhost:5000/faturas/1

##PUT
curl -X PUT http://localhost:5000/faturas/1 -H "Content-Type: application/json" -d '{"description": "Nova descrição da fatura"}'

##GET
curl http://localhost:5000/faturas/1

##GET ALL
curl http://localhost:5000/faturas

##POST
curl -X POST http://localhost:5000/faturas -H "Content-Type: application/json" -d '{"description": "Descrição da fatura"}'
