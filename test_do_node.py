import unittest
from unittest.mock import patch, MagicMock
from your_module_name import CommandLine

class TestCommandLine(unittest.TestCase):
    def setUp(self):
        self.command_line = CommandLine('http://localhost:8000')  # Замените URL на адрес вашего демона

    @patch('builtins.print')
    def test_do_node(self, mock_print):
        # Создаем макет объекта серверного прокси
        mock_proxy = MagicMock()
        mock_proxy.node.return_value = {'answer': [{'key1': 'value1', 'key2': 'value2'}]}
        self.command_line.daemon_proxy = mock_proxy

        # Вызываем метод do_node
        self.command_line.do_node('arg1 arg2')

        # Проверяем, что метод server_proxy был вызван с правильными аргументами
        mock_proxy.node.assert_called_once_with('arg1', 'arg2')

        # Проверяем, что print был вызван с результатом ответа
        mock_print.assert_called_once_with("Received result:", {'answer': [{'key1': 'value1', 'key2': 'value2'}]})
