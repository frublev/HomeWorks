import unittest
from unittest.mock import patch
from HW5 import get_doc_owner_name, get_all_doc_owners_names, delete_doc, add_new_doc
from create_folder import check_path


class TestHW5(unittest.TestCase):

    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, m):
        result = get_doc_owner_name()
        self.assertEqual('Аристарх Павлов', result)

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        self.assertEqual({'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}, result)

    @patch('builtins.input', return_value='10006')
    def test_delete_doc_true(self, m):
        result = delete_doc()
        self.assertTrue(result[1])

    @patch('builtins.input', return_value='10006')
    def test_delete_doc_number(self, m):
        result = delete_doc()
        self.assertEqual('10006', result[0])

    @patch('builtins.input', side_effect=['10007', 'insurance', 'Лорд Кабанчиков', '3'])
    def test_add_new_doc(self, m):
        result = add_new_doc()
        self.assertEqual('3', result)


if __name__ == '__main__':
    unittest.main()
