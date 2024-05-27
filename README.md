# LeitorFaturas

Sistema de leitura de arquivo pdf em pyhon utilizando a biblioteca PyPDF2

Sistema ler um arquivo e salva as informações específicas em um banco de dados postgresSQL.

Para executar a aplicação de extrator de texto em arquivo PDF, basta rodar o arquivo main.py

Obs.: deve-se colocar o caminho local da pasta das faturas utilizadas como base para o teste, pois o programa irá buscar o diretório local na máquina.

```bash
python main.py
```

Importante salientar que deve ser configurado o banco de dados de acordo com o banco utilizado como teste
```bash
    dbname="uriboca",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
```


criar a tabela "faturas"

```bash
create table faturas (
  id serial not null,
  description text not null
)
```

#instalar as seguintes bibliotecas
##pypdf2
##psycopg2
