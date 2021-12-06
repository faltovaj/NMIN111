#!/usr/bin/env python3
# Trida zamestnancu

class Zamestnanec:
    """ Trida k evidenci zamestnancu """
    def __init__(self, jmeno, prijmeni, pracoviste):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.pracoviste = pracoviste

    def vrat_email(self):
        """ Funkce vrati pracovni email zamestnance """
        return self.jmeno + '.' + self.prijmeni + '@mff.cuni.cz'

