import unittest
from unittest.mock import patch
import accounting


class TestSecretary(unittest.TestCase):
    def setUp(self):
        print('Testing secretary functions..')

    def test_check_document_existance(self):
        self.assertEqual(accounting.check_document_existance('2207 876234'), True)
        self.assertEqual(accounting.check_document_existance('x'), False)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(accounting.get_doc_owner_name(), 'Геннадий Покемонов')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(accounting.get_all_doc_owners_names(),
                         {"Геннадий Покемонов", "Аристарх Павлов", "Василий Гупкин"})

    def test_remove_doc_from_shelf(self):
        accounting.remove_doc_from_shelf('10006')
        self.assertEqual(accounting.directories['2'], [])

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(accounting.delete_doc(), ('11-2', True))

    @patch('builtins.input')
    def test_move_doc_to_shelf(self, user_input):
        user_input.side_effect = ['11-2', '3']
        accounting.move_doc_to_shelf()
        self.assertEqual(accounting.directories['3'], ['11-2'])

    def test_show_document_info(self):
        self.assertEqual(accounting.show_document_info({'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}),
                         'passport "2207 876234" "Василий Гупкин"')

    def tearDown(self):
        print('Testing complete!')
