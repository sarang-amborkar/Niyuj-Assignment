import unittest
from app import app,conn

class StudentTestCase(unittest.TestCase):
    def test_createstud(self):
        data = {"name":"sarang", "backlog":3}
        tester = app.test_client(self)
        response = tester.post('/create_stu', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('User has been created', str(response.data))

    def test_fetch_user(self):
        tester = app.test_client(self)
        response = tester.get('/create_stu')
        self.assertEqual(response.status_code, 200)

    def test_fetch_user_by_id(self):
        tester = app.test_client(self)
        response = tester.get('/create_stu/1')
        self.assertEqual(response.status_code, 200)


