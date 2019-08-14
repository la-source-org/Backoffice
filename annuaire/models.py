
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


#   Remove all explicits id ?
#   ManyToManyField
#   TODO : mettre les models a jour

################################################################################
class Fournisseur(models.Model):

    id_fournisseur = models.CharField(primary_key=True, max_length=45)
    type_fournisseur = models.CharField(max_length=45)
    statut = models.CharField(max_length=45)
    adresse = models.CharField(max_length=45)
    code_postal = models.CharField(max_length=45)
    ville = models.CharField(max_length=45)
    pays = models.CharField(max_length=45)
    mode_livraison = models.CharField(max_length=45)
    siret = models.CharField(max_length=45)
    commentaires = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id_adherents)


################################################################################
class Lieu(models.Model):

    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=32)
    adresse = models.CharField(max_length=32)
    code_postal = models.CharField(max_length=32)
    ville = models.CharField(max_length=20)
    pays = models.CharField(max_length=64)
    telephone  = models.CharField(max_length=8)
    telephone_portable = models.CharField(max_length=32)
    commentaires = models.CharField(max_length=32)

    def __str__(self):
        return str(self.id) + " " + self.type

################################################################################
class Relais(models.Model):

    id = models.IntegerField(primary_key=True)
    type_public = models.CharField(max_length=45)
    nom_structure = models.CharField(max_length=45)
    notes = models.CharField(max_length=45)

    def __str__(self):
        return str(self.id) + " " + self.nom_structure + " " + self.type_public







################################################################################
class Categorie(models.Model):

    nom = models.CharField(primary_key=True, max_length=45)

    def __str__(self):
        return str(self.nom)

################################################################################
class Sous_categorie(models.Model):

    nom = models.CharField(primary_key=True, max_length=45)
    categorie_nom = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom)

################################################################################
class Produits_possibles(models.Model):

    uid = models.CharField(primary_key=True, max_length=45)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    sous_categorie = models.ForeignKey(Sous_categorie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uid)



################################################################################
class Label(models.Model):

    id_label = models.IntegerField(primary_key=True)
    AOC = models.IntegerField()
    AOP = models.IntegerField()
    BIO = models.IntegerField()
    NP = models.IntegerField()
    Demeter = models.IntegerField()
    label_rouge = models.IntegerField()
    fair_trade = models.IntegerField()

    def __str__(self):
        return str(self.id_label)


################################################################################
class Produit_references(models.Model):

    nom = models.CharField(primary_key=True, max_length=45)
    type = models.CharField(max_length=45)
    description = models.IntegerField()
    prix = models.CharField(max_length=45)
    mode_conditionnement = models.CharField(max_length=45)

    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    id_label = models.ForeignKey(Label, on_delete=models.CASCADE)
    nom_categorie = models.ForeignKey(Sous_categorie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_adherents)



################################################################################
class Contact(models.Model):

    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    telephone = models.CharField(max_length=20)
    addresse = models.CharField(max_length=64)
    code_postal  = models.CharField(max_length=8)
    ville = models.CharField(max_length=32)
    pays = models.CharField(max_length=32)
    telephone_portable = models.CharField(max_length=20)
    origine_du_contact = models.CharField(max_length=32)
    commentaires = models.CharField(max_length=32)
    id_fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    id_relais = models.ForeignKey(Relais, on_delete=models.CASCADE)
    id_lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.nom + " " + self.prenom


################################################################################
class Adherents(models.Model):

    id_adherents = models.IntegerField(primary_key=True)
    date_naissance = models.CharField(max_length=45)
    rgpd = models.IntegerField()
    date_questionnaire = models.CharField(max_length=45)
    message_questionnaire = models.CharField(max_length=45)
    date_reunion_information = models.CharField(max_length=45)
    date_formation_communication = models.CharField(max_length=45)
    date_formation_logicielle = models.CharField(max_length=45)
    date_formation_distribution = models.CharField(max_length=45)
    niveau_implication = models.IntegerField()
    commentaires = models.CharField(max_length=45)
    date_adhesion = models.CharField(max_length=45)
    type_disponibilite = models.CharField(max_length=45)
    mode_contact_privilegie = models.CharField(max_length=45)
    type_disponibilite = models.CharField(max_length=45)
    id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_adherents)


################################################################################
class Competences_possibles(models.Model):

    nom = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return str(self.nom)


################################################################################
class Competences(models.Model):

    commentaires = models.CharField(max_length=45, primary_key=True)
    niveau_competences = models.CharField(max_length=45)
    id_adherents = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    nom = models.ForeignKey(Competences_possibles, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_adherents) + " " + str(self.nom)

################################################################################
class Groupes_possibles(models.Model):

    nom = models.CharField(max_length=45, primary_key=True)

    def __str__(self):
        return str(self.nom)


################################################################################
class Groupes(models.Model):

    id = models.CharField(max_length=45, primary_key=True)
    role = models.CharField(max_length=45)
    id_adherents = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    groupes_possibles = models.ForeignKey(Groupes_possibles, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_adherents) + " " + str(self.role)








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

# ################################################################################
# class Fournisseur2(models.Model):
#
#     id = models.IntegerField(primary_key=True)
#     id_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
#
#     FOURNISSEUR_TYPE = (("A", "Adherent"), ("M", "Membre"), ("D", "Donateur"))
#     type = models.CharField(max_length=1,choices=FOURNISSEUR_TYPE,default="F")
#     status = models.CharField(max_length=20)
#
#     def __str__(self):
#         return str(self.id) + " " + self.get_fournisseur_type_display()


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
