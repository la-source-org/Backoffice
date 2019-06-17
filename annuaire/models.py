
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


#   Remove all explicits id ?
#   ManyToManyField
#   TODO : mettre les models a jour

################################################################################
class Contact(models.Model):

    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    addresse = models.CharField(max_length=64)
    code_postal  = models.CharField(max_length=8)
    ville = models.CharField(max_length=32)
    pays = models.CharField(max_length=32)
    telephone = models.CharField(max_length=20)
    telephone_portable = models.CharField(max_length=20)

    CONTACT_TYPE = (("P", "Partenaire"), ("F", "Fournisseur"), ("A", "Abonné"), ("B", "Bénévole"))
    type = models.CharField(max_length=1,choices=CONTACT_TYPE,default="F")

    def __str__(self):
        return str(self.id) + " " + self.nom + " " + self.prenom + " " + self.get_type_display()

################################################################################
class Membre(models.Model):

    id = models.IntegerField(primary_key=True)
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    CONTACT_SOUS_TYPE = (("A", "Adherent"), ("M", "Membre"), ("D", "Donateur"))
    sous_type = models.CharField(max_length=1,choices=CONTACT_SOUS_TYPE,default="A")

    date_naissance = models.CharField(max_length=20)
    rgpd = models.IntegerField()
    date_questionnaire= models.CharField(max_length=20)
    message_questionnaire = models.CharField(max_length=64)
    reunion_information = models.CharField(max_length=20)
    formation_communication = models.CharField(max_length=20)
    formation_logicielle = models.CharField(max_length=20)
    formation_distribution = models.CharField(max_length=20)
    niveau_implication = models.IntegerField()
    commentaires = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) + " " + self.date_naissance + " " + self.get_sous_type_display()

################################################################################
class Fournisseur(models.Model):

    id = models.IntegerField(primary_key=True)
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    FOURNISSEUR_TYPE = (("A", "Adherent"), ("M", "Membre"), ("D", "Donateur"))
    type = models.CharField(max_length=1,choices=FOURNISSEUR_TYPE,default="F")
    status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + " " + self.get_fournisseur_type_display()


################################################################################
class Certification(models.Model):

    id = models.IntegerField(primary_key=True)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    AOC = models.IntegerField()
    AOP = models.IntegerField()
    BIO = models.IntegerField()
    N_and_P = models.IntegerField()
    demeter = models.IntegerField()
    label_rouge = models.IntegerField()
    fair_trade = models.IntegerField()

    def __str__(self):
        return str(self.id_fournisseur) + " " +  str(self.id)

################################################################################
class Produit(models.Model):

    id = models.IntegerField(primary_key=True)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    type = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    prix = models.IntegerField()
    mode_livraison = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id_fournisseur) + " " +  str(self.id) + " " + nom + " " + description
