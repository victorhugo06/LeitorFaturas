import unittest
from app import app, db, User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Configuração do banco de dados de teste
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_user(self):
        response = self.app.post('/users', json={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User added successfully!', response.get_data(as_text=True))

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        self.app.post('/users', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

    def test_update_user(self):
        self.app.post('/users', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
        response = self.app.put('/users/1', json={'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('User updated successfully!', response.get_data(as_text=True))

    def test_delete_user(self):
        self.app.post('/users', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User deleted successfully!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
