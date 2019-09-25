from unittest import TestCase
from typing import List
from flask import url_for, Flask
from cvapi import create_app

json_valido = {
  "name": "George the Martian",
  "profession": "Youtube senior analyst",
  "phone": "+55 287298121",
  "email": "George@martian.com",
  "address": "73 N. Oak Drive - Dyersburg, TN 38024",
  "portfolio": "github.com/g_martian",
  "education": [
    [
      "PhD in the streets - Harvard",
      "2001",
      "phd in doing absolutelly nothing 24/7"
    ]
  ],
  "experience": [
    [
      "Garbage collector",
      "Jan 2000 - Mai 2003",
      "Collecting garbage in other codes"
    ]
  ],
  "skills": [
    [
      "Python",
      5
    ]
  ],
  "languages": [
    [
      "Pirate English",
      "Native"
    ]
  ]
}

def app_endpoint(app: Flask) -> List[str]:
    """Retornar todos os endpoints do `app`."""
    return [e.endpoint for e in app.url_map.iter_rules()]


class FlaskBaseTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()


class TestRouteValidateJson(FlaskBaseTestCase):
    def test_app_deve_conter_a_rota_validate_json(self):
        endpoints = app_endpoint(create_app())
        self.assertIn(
            'validate_json',
            endpoints,
            'o endpoint validade-json não existe no APP'
        )

    def test_deve_retornar_um_requisicao_valida(self):
        response = self.client.post(
            url_for('validate_json')
        )
        self.assertIn(
            response.status_code,
            list(range(100, 511))
        )

    def test_deve_receber_um_objeto_json(self):
        response = self.client.post(
            url_for('validate_json'),
            json={}
        )

        self.assertIsInstance(response.json, dict)

    def test_deve_receber_um_vazio_e_retornar_o_schema(self):
        response = self.client.post(
            url_for('validate_json'),
            json={}
        )
        schema_esperado = {
          "address": [
            "Missing data for required field."
          ],
          "education": [
            "Missing data for required field."
          ],
          "email": [
            "Missing data for required field."
          ],
          "experience": [
            "Missing data for required field."
          ],
          "languages": [
            "Missing data for required field."
          ],
          "name": [
            "Missing data for required field."
          ],
          "phone": [
            "Missing data for required field."
          ],
          "portfolio": [
            "Missing data for required field."
          ],
          "profession": [
            "Missing data for required field."
          ],
          "skills": [
            "Missing data for required field."
          ]
        }
        self.assertEqual(response.json, schema_esperado)

    def test_deve_retornar_dados_validos_com_json_correto(self):
        response = self.client.post(
            url_for('validate_json'),
            json=json_valido
        )
        self.assertEqual(response.json, {'ok': 'Dados válidos'})
