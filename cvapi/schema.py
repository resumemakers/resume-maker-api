from typing import NoReturn
from flask_marshmallow import Marshmallow, fields
from flask_marshmallow.fields import fields

ma = Marshmallow()


class ResumeSchema(ma.Schema):
    name = fields.Str(required=True)
    profession = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)
    portfolio = fields.Str(required=True)
    education = fields.List(fields.List(fields.Raw()), required=True)
    experience = fields.List(fields.List(fields.Raw()), required=True)
    skills = fields.List(fields.List(fields.Raw()), required=True)
    languages = fields.List(fields.List(fields.Raw()), required=True)

    class Meta:
        fields = (
            'name',
            'profession',
            'phone',
            'email',
            'address',
            'portfolio',
            'education',
            'experience',
            'skills',
            'languages',
        )


def configure_app(app) -> NoReturn:
    """Configurar o app para ter o schema."""
    ma.init_app(app)
