from wtforms import Form, FloatField, validators


class InputForm(Form):
    a = FloatField(validators=[validators.InputRequired()])
    b = FloatField(validators=[validators.InputRequired()])
