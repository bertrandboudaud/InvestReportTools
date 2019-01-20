# -*- coding: utf-8 -*-
# Le micro-foncier est le plus simple des deux. 
# Concrètement, vous aurez juste à déclarer les loyers perçus. 
# Avant de calculer l’impôt, le fisc va appliquer un abattement de 30%. 
# Autrement dit, les loyers imposés seront de 70% des loyers perçus. 
# Exemple : 
# Mr Corrigetonimpot loue un bien vide et perçoit 10 000 € de loyers en 2017. 
# Il opte pour le régime micro-foncier lors de la déclaration d’impôt 2018 sur les revenus 2017. 
# Les impôts vont procéder à un abattement de 30% soit 10000*30% = 3 000 €. 
# Mr sera donc imposé sur une base de 10 000 – 3 000 = 7 000 €. 

class VideMicroFoncier:

    def __init__(self, credit, appartement, rent, salaire):
        self._credit = credit
        self._appartement = appartement
        self._rent = rent
        self._salaire = salaire

    def debugPrint(self):
        print "Dispositif: Vide - Micro Foncier"

    def impotsMensuel(self, annee, mois):
        return _self.impotsAnnuel(annee)/12

    def impotsAnnuel(self, annee):
        rentAnneePrecedente = self._rent.loyerBrutAnnuel(annee-1);
        abattement = 30.0
        imposable = ((rentAnneePrecedente*(100.0-abattement))/100.0)
        impotsRevenus = (imposable * self._salaire._tranche) / 100.0
        impotsPrelevementSociaux = (imposable * 17.2) / 100.0
        return impotsRevenus+impotsPrelevementSociaux

