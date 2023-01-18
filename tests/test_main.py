from unittest import TestCase
import pytest
from main import rus_logs, uniq_ids, max_fol

class TestRusLogs(TestCase):
    def test_just_rus(self):
        res=rus_logs()
        self.assertEqual(res, 'Россия')

def test_just_rus():
    res=rus_logs()
    assert res == 'Россия'

class TestUniqIds(TestCase):
    def test_uniq_res(self):
        res =uniq_ids()
        self.assertIsInstance(res, list)
        
def test_uniq_res():
    res =uniq_ids()
    assert 213 in res
   
class TestMaxFol(TestCase):
    def test_max_fol(self):
        res = max_fol()
        self.assertIn(res, 'yandex')

    
