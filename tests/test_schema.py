from unittest import TestCase
from cvapi import schema


class TestSchema(TestCase):
    def test_deve_ter_configure_app(self):
        self.assertEqual(
            hasattr(schema, 'configure_app'),
            True,
            'schema não tem função de configuração'
        )

    def test_deve_ter_ma(self):
        self.assertEqual(
            hasattr(schema, 'ma'),
            True,
            'schema não tem class Marshmallow definida'
        )

    def test_configure_app_deve_ser_invocavel(self):
        self.assertEqual(
            hasattr(schema.configure_app, '__call__'),
            True,
            'configure_app não é invocável'
        )

    def test_configure_app_deve_receber_app(self):
        self.assertEqual(
            schema.configure_app.__code__.co_argcount,
            1,
            'configure_app não recebe app'
        )
