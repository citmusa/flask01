from wtforms import (
    Form,
    StringField,
    TextField
)
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username = StringField('Username')
    email = EmailField('Correo')
    comment = TextField('Comentario')
