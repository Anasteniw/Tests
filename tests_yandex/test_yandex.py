from unittest import TestCase
from main_yandex import create_folder, delete_folder

class TestYSuccess(TestCase):
    def test_success_create_folder(self):
        res=create_folder('test')
        self.assertEqual(res, 201)

class TestYUnsuccess(TestCase):       
    def test_passed_create_folder(self):
        res=create_folder('test_passed')
        self.assertEqual(res, 409)

class TestYDelete(TestCase):       
    def test_success_delete_folder(self):
        res=delete_folder('test')
        self.assertEqual(res, 204)


