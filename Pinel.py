from SheetOutput import SheetOutput

class Pinel(SheetOutput):

    TYPE_6     = 0
    TYPE_6_3   = 1
    TYPE_6_3_3 = 2
    TYPE_9     = 3
    TYPE_9_3   = 4

    def __init__(self, type, credit, appartement):
        SheetOutput.__init__(self)
        self._credit = credit
        self._appartement = appartement
        self._type = type
        self._typeNames = [ "6 Ans", 
                            "6+3 Ans",
                            "6+3+3 Ans",
                            "9 Ans",
                            "9+3 Ans" ]

    def debugPrint(self):
        print "Dispositif: Pinel " + str(self._typeNames[self._type])

    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self._typeNames[self._type])
        return self._currentLine;

    def reductionImpotsMensuel(self, annee, mois):
        # Mensualite
        if (annee<self._credit._startAnnee):
            return 0
        elif (annee == self._credit._startAnnee) and (mois < self._credit._startMois):
            return 0
        else:
            nbmois = (((annee - self._credit._startAnnee)*12)-self._credit._startMois) + mois
            pourcentageAnnuel = 0.0
            # 
            if (self._type == Pinel.TYPE_6):
                if (nbmois<6*12):
                    pourcentageAnnuel = 2.0
            # 
            if (self._type == Pinel.TYPE_6_3):
                if (nbmois<6*12):
                    pourcentageAnnuel = 2.0
                elif (nbmois<(6+3)*12):
                    pourcentageAnnuel = 2.0
            # 
            if (self._type == Pinel.TYPE_6_3_3):
                if (nbmois<6*12):
                    pourcentageAnnuel = 2.0
                elif (nbmois<(6+3)*12):
                    pourcentageAnnuel = 2.0
                elif (nbmois<(6+3+3)*12):
                    pourcentageAnnuel = 1.0
            # 
            if (self._type == Pinel.TYPE_9):
                if (nbmois<9*12):
                    pourcentageAnnuel = 2.0
            # 
            if (self._type == Pinel.TYPE_9_3):
                if (nbmois<9*12):
                    pourcentageAnnuel = 2.0
                elif (nbmois<(9+3)*12):
                    pourcentageAnnuel = 1.0
            pourcentageMensuel = pourcentageAnnuel / 12.0
            # print pourcentageMensuel

            reductionImpotCredit = (self._appartement._prixAcquisition * (pourcentageMensuel/100.0))
            return reductionImpotCredit

    def reductionImpotsAnnuel(self, annee):
        reductionImpotCredit = 0.0
        for mois in range(0, 12):
            reductionImpotCreditMois = self.reductionImpotsMensuel(annee,mois)
            reductionImpotCredit += reductionImpotCreditMois
        return reductionImpotCredit

