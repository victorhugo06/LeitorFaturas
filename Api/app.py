from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Faturas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Faturas {self.id}>'

# Teste de conexão com o banco de dados
Config.test_database_connection()

# Método para verificar se a conexão com o banco de dados foi bem-sucedida
def check_database_connection():
    Config.test_database_connection()

@app.route('/faturas', methods=['POST'])
def add_fatura():
    data = request.get_json()
    new_fatura = Faturas(description=data['description'])
    db.session.add(new_fatura)
    db.session.commit()
    return jsonify({'message': 'Fatura added successfully!'}), 201

@app.route('/faturas', methods=['GET'])
def get_faturas():
    query = Faturas.query
    sql = str(query)
    print("SQL gerada para consulta de faturas:")
    print(sql)
    
    faturas = query.all()
    return jsonify([{'id': fatura.id, 'description': fatura.description} for fatura in faturas])

@app.route('/faturas/<int:id>', methods=['GET'])
def get_fatura(id):
    fatura = Faturas.query.filter_by(id=id).first()
    if fatura:
        return jsonify({'id': fatura.id, 'description': fatura.description})
    return jsonify({'message': 'Fatura not found'}), 404

@app.route('/faturas/<int:id>', methods=['PUT'])
def update_fatura(id):
    data = request.get_json()
    fatura = Faturas.query.filter_by(id=id).first()
    if fatura:
        fatura.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Fatura updated successfully!'})
    return jsonify({'message': 'Fatura not found'}), 404

@app.route('/faturas/<int:id>', methods=['DELETE'])
def delete_fatura(id):
    fatura = Faturas.query.filter_by(id=fatura_id).first()
    if fatura:
        db.session.delete(fatura)
        db.session.commit()
        return jsonify({'message': 'Fatura deleted successfully!'})
    return jsonify({'message': 'Fatura not found'}), 404

if __name__ == '__main__':
    # Verificar a conexão com o banco de dados antes de iniciar o aplicativo Flask
    check_database_connection()
    app.run(debug=True)
