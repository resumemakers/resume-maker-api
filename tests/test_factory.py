from unittest import TestCase
from flask import Flask
import cvapi


class TestFlaskApp(TestCase):
    def test_create_app_deve_existir(self):
        self.assertEqual(
            hasattr(cvapi, 'create_app'),
            True,
            'app factory não existe'
        )

    def test_create_app_deve_ser_invocavel(self):
        self.assertEqual(
            hasattr(cvapi.create_app, '__call__'),
            True,
            'create_app não é invocável'
        )

    def test_create_app_deve_retornar_um_flask_app(self):
        self.assertIsInstance(
            cvapi.create_app(),
            Flask,
            'create_app não retornar um app Flask'
        )
