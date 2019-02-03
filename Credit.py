from SheetOutput import SheetOutput

class Credit(SheetOutput):

    def __init__(self, appartement, tauxCredit, tauxADI, apport, frais, dureeMois, startAnnee, startMois):
        SheetOutput.__init__(self)
        self._appartement = appartement
        self._tauxCredit = float(tauxCredit)
        self._tauxADI = float(tauxADI)
        self._apport = float(apport)
        self._frais = float(frais)
        self._dureeMois = dureeMois
        self._startAnnee = startAnnee
        self._startMois = startMois

    def coutCredit(self):
        totalCout = 0.0
        for i in range(0, self._dureeMois):
            annee = self._startAnnee + (self._startMois + i) / 12
            mois = (self._startMois + i) % 12
            totalCout += self.mensualitePretAmortissable(annee, mois)
        return (totalCout - self.montant())

    def coutAssurance(self):
        totalCout = 0.0
        for i in range(0, self._dureeMois):
            annee = self._startAnnee + (self._startMois + i) / 12
            mois = (self._startMois + i) % 12
            totalCout += self.mensualiteAssurance(annee, mois)
        return totalCout

    def montant(self):
        return self._appartement._prixAcquisition + self._appartement._fraisAcquisition + self._frais - self._apport

    def debugPrint(self):
        print "Montant: " + str(self.montant())
        print "Taux credit: " + str(self._tauxCredit)
        print "Taux assurance: " + str(self._tauxADI)
        print "Apport: " + str(self._apport)
        print "Frais: " + str(self._frais)
        print "Duree (mois): " + str(self._dureeMois)
        print "Cout credit: " + str(self.coutCredit() + self.coutAssurance())
        print "Dont assurance: " + str(self.coutAssurance())

    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self.montant())
        self.writeXLS(sheet, self._tauxCredit)
        self.writeXLS(sheet, self._tauxADI)
        self.writeXLS(sheet, self._apport)
        self.writeXLS(sheet, self._frais)
        self.writeXLS(sheet, self._dureeMois)
        self.writeXLS(sheet, self.coutCredit() + self.coutAssurance())
        self.writeXLS(sheet, self.coutAssurance())
        return self._currentLine;

    def sheetPrintHeader(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, "Montant")
        self.writeXLS(sheet, "Taux credit")
        self.writeXLS(sheet, "Taux assurance")
        self.writeXLS(sheet, "Apport")
        self.writeXLS(sheet, "Frais")
        self.writeXLS(sheet, "Duree (mois)")
        self.writeXLS(sheet, "Cout credit")
        self.writeXLS(sheet, "Dont assurance")
        return self._currentLine;

    def mensualitePretAmortissable(self, annee, mois):
        # Mensualite
        if (annee<self._startAnnee):
        	return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
        	return 0
        elif ((((annee - self._startAnnee)*12 - self._startMois) + mois) <= self._dureeMois) :
            t = float((1.0 + ((self._tauxCredit)/100.0))**(1.0/12.0) -1.0) # annuel vers mensuel
            d = self._dureeMois 
            m = ((self.montant() * (t) )) / (1-(1/((1+t)**d)))
            return m
        else:
        	return 0

    def annuitePretAmortissable(self, annee):
        cumulMensualiteAnnee = 0.0
        for mois in range(0, 12):
            mensualite = self.mensualitePretAmortissable(annee,mois)
            cumulMensualiteAnnee += mensualite
        return cumulMensualiteAnnee

    def mensualiteAssurance(self, annee, mois):
        # Cela exprime le prix annuel de votre cotisation. 
        # Il sera egal a 0.6 du montant initial, c est a dire la somme totale empruntee, 
        # ou egal a 0.6 du -capital restant du- de votre credit immobilier. 
        # Le choix de formule depend du choix de l assurance 
        # ici on calcul 0.6 du montant initial
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
            return 0
        elif ((((annee - self._startAnnee)*12 - self._startMois) + mois) <= self._dureeMois) :
            t = float((self._tauxADI)/100.0)
            m = (self.montant() * (t) ) / 12.0
            return m
        else:
            return 0

    def annuiteAssurance(self, annee):
        cumulMensualiteAnnee = 0.0
        for mois in range(0, 12):
            mensualite = self.mensualiteAssurance(annee,mois)
            cumulMensualiteAnnee += mensualite
        return cumulMensualiteAnnee

    def interetsEmpruntsMois(self, annee, mois):
        debug = False;
#        if (annee == 2038):
#            debug = True;
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
            return 0
        else:
            currentAnnee = self._startAnnee
            currentMois = self._startMois
            cumulCapitalRestant = self.montant();
            coutEmprunt = 0.0
            while (not ((currentAnnee > annee) and (currentMois > mois))):
                if (currentMois==12):
                    currentMois=0
                coutEmprunt = cumulCapitalRestant * ((self._tauxCredit/100.0)/12.0)
                if (self.mensualitePretAmortissable(annee, mois) < coutEmprunt):
                    coutEmprunt = cumulCapitalRestant
                    cumulCapitalRestant = 0;
                else:
                    cumulCapitalRestant -= ((self.mensualitePretAmortissable(annee, mois) - coutEmprunt))
                    if (cumulCapitalRestant<0):
                        cumulCapitalRestant = 0;
                if debug:
                    print "-------------------------------------------"
                    print str(currentAnnee) + " " + str(annee)
                    print str(currentMois) + " " + str(mois)
                    print cumulCapitalRestant
                    print self.mensualitePretAmortissable(annee, mois)
                    print coutEmprunt
                    print self._tauxCredit/12.0
                currentMois+=1
                if (currentMois==12):
                    currentAnnee+=1
            # print str(currentAnnee) + " " + str(currentMois);
            return coutEmprunt;

    def interetsEmpruntsAnnee(self, annee):
        debug = False;
#        if (annee == 2038):
#            debug = True;
        cumulCoutEmprunt = 0.0
        for mois in range(0, 12):
            mensualite = self.interetsEmpruntsMois(annee,mois)
            if debug:
                print "******************************** " + str(mensualite) + " " + str(mois); 
            cumulCoutEmprunt += mensualite
        #if (annee == 2019):
        #    sys.exit(0)
        return cumulCoutEmprunt

    def capitalRestantMois(self, annee, mois):
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
            return 0
        else:
            currentAnnee = self._startAnnee
            currentMois = self._startMois
            cumulCapitalRestant = self.montant();
            coutEmprunt = 0.0
            # while (currentAnnee <= annee) and (currentMois <= mois):
            while (not ((currentAnnee > annee) and (currentMois > mois))):    
                if (currentMois==12):
                    currentMois=0
                if (cumulCapitalRestant<=0):
                    cumulCapitalRestant = 0
                else:
                    coutEmprunt = cumulCapitalRestant * ((self._tauxCredit/100)/12.0)
                    cumulCapitalRestant -= (self.mensualitePretAmortissable(currentAnnee, currentMois) - coutEmprunt)
#                    print "-------------------------------------------"
#                    print str(currentAnnee) + "/" + str(annee) + " " + str(currentMois) + "/" + str(mois) + " " + str(self.mensualitePretAmortissable(currentAnnee, currentMois)) + " " +str(cumulCapitalRestant)
                currentMois+=1
                if (currentMois==12):
                    currentAnnee+=1
            return cumulCapitalRestant;

    def capitalRestantAnnee(self, annee):
        return self.capitalRestantMois(annee,11)
