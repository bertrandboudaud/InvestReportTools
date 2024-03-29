from SheetOutput import SheetOutput

class Rent(SheetOutput):

    def __init__(self, loyerMensuel, chargesMensuel, revalorisationCharges, startAnnee, startMois, taxeFonciere):
        SheetOutput.__init__(self)
        self._loyerMensuel = loyerMensuel
        self._chargesMensuel = chargesMensuel
        self._revalorisationCharges = revalorisationCharges
        self._startAnnee = startAnnee
        self._startMois = startMois
        self._taxeFonciere = taxeFonciere

    def debugPrint(self):
        print "Loyer mensuel: " + str(self._loyerMensuel)
        print "Charges mensuelles: " + str(self._chargesMensuel)
        print "revalorisationCharges (%/an): " + str(self._revalorisationCharges)
        print "Taxe Fonciere: " + str(self._taxeFonciere)

    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self._loyerMensuel)
        self.writeXLS(sheet, self._chargesMensuel)
        self.writeXLS(sheet, self._revalorisationCharges)
        self.writeXLS(sheet, self._taxeFonciere)
        return self._currentLine;

    def sheetPrintHeader(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, "Loyer mensuel")
        self.writeXLS(sheet, "Charges mensuelles")
        self.writeXLS(sheet, "revalorisationCharges (%/an)")
        self.writeXLS(sheet, "Taxe Fonciere")
        return self._currentLine;

    def loyerBrutMensuel(self, annee, mois):
        # Mensualite
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
            return 0
        else:
            return self._loyerMensuel

    def loyerBrutAnnuel(self, annee):
        cumulLoyerAnnee = 0.0
        for mois in range(0, 12):
            loyerMois = self.loyerBrutMensuel(annee,mois)
            cumulLoyerAnnee += loyerMois
        return cumulLoyerAnnee

    def chargesMensuelles(self, annee, mois):
        # Mensualite
        if (annee<self._startAnnee):
            return 0
        elif (annee == self._startAnnee) and (mois < self._startMois):
            return 0
        else:
            # TODO revalirisation charges
            return self._chargesMensuel + (self._taxeFonciere/12)

    def chargesAnnuelles(self, annee):
        cumulChargesAnnee = 0.0
        for mois in range(0, 12):
            chargesMois = self.chargesMensuelles(annee,mois)
            cumulChargesAnnee += chargesMois
        return cumulChargesAnnee

