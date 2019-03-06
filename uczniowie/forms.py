# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import DataRequired

blad1 = 'To pole jest wymagane'



class KlasaForm(FlaskForm):
    id = HiddenField("klasa id")
    klasa = StringField("numer klasy: ",
                        validators=[DataRequired(message=blad1)])
    rok_naboru = StringField("rok naboru")
    rok_matury = StringField("rok_matury")


class UczenForm(FlaskForm):
    id = HiddenField("")
    imie = StringField("imię")
    nazwisko = StringField("nazwisko")
    plec = BooleanField("płeć")
    klasa = FieldList(FormField(KlasaForm))
