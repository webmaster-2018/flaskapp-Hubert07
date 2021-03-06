#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'uczniowie.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy


# MODELE #
class BazaModel(Model):
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField(max_length=3)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)


class Uczen(BazaModel):
    imie = CharField(max_length=18)
    nazwisko = CharField(max_length=18)
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name="uczniowie")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
