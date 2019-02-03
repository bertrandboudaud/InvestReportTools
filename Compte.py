import Rent
import Credit
from SheetOutput import SheetOutput

class Compte(SheetOutput):

    def __init__(self, capital, interetAnnuel, startAnnee, startMois):
        SheetOutput.__init__(self)
        self._capital = float(capital)
        self._interetAnnuel = float(interetAnnuel)
        self._startAnnee = startAnnee
        self._startMois = startMois

    def debugPrint(self):
        print "Capital de depart: " + str(self._capital)
        print "Interets (%/an): " + str(self._interetAnnuel)


    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self._capital)
        self.writeXLS(sheet, self._interetAnnuel)
        return self._currentLine;

    def sheetPrintHeader(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, "Capital de depart")
        self.writeXLS(sheet, "Interets (%/an):")
        return self._currentLine;

    # capital a la fin du mois
    def capitalMensuel(self, annee, mois, rent, credit, salaire):
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
        	return 0
        else:
        	currentAnnee = self._startAnnee
        	currentMois = self._startMois
        	currentCapital = self._capital
        	while (currentAnnee <= annee) and (currentMois <= mois):
        		# print "*** " + str(currentCapital) + " " +str(currentAnnee) + "/" + str(currentMois)
        		# ajout de la location
        		currentCapital += rent.loyerBrutMensuel(currentAnnee, currentMois)
        		# charges
        		currentCapital -= rent.chargesMensuelles(currentAnnee, currentMois)
        		# charges
        		currentCapital -= (credit.mensualitePretAmortissable(currentAnnee, currentMois) + credit.mensualiteAssurance(currentAnnee, currentMois))
        		# salaire
        		currentCapital += salaire.salaireNetMensuel(currentAnnee, currentMois)
        		# impots
        		currentCapital -= salaire.impotsMensuel(currentAnnee, currentMois)
        		# interets en decembre
        		if ((currentMois==11) and (currentCapital>0)):
        			currentCapital += (currentCapital*self._interetAnnuel)/100.0
        		# Next month
        		currentMois+=1
        		if (currentMois==12):
        			currentAnnee+=1
        			currentMois=0
        	return currentCapital


