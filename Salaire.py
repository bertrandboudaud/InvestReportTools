from SheetOutput import SheetOutput

class Salaire(SheetOutput):

    def __init__(self, salaireNetMensuel, impotsMensuel, tranche):
        SheetOutput.__init__(self)
        self._salaireNetMensuel = salaireNetMensuel
        self._impotsMensuel = impotsMensuel
        self._tranche = tranche

    def debugPrint(self):
        print "Salaire net mensuel: " + str(self._salaireNetMensuel)
        print "Impots mensuels: " + str(self._impotsMensuel)
        print "Tranche: " + str(self._tranche) + "%"

    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self._salaireNetMensuel)
        self.writeXLS(sheet, self._impotsMensuel)
        self.writeXLS(sheet, self._tranche)
        return self._currentLine;

    def sheetPrintHeader(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, "Salaire net mensuel")
        self.writeXLS(sheet, "Impots mensuels")
        self.writeXLS(sheet, "Tranche")
        return self._currentLine;

    def salaireNetMensuel(self, annee, mois):
        return self._salaireNetMensuel

    def salaireNetAnnuel(self, annee):
        cumulSalaireAnnee = 0.0
        for mois in range(0, 12):
            salaireMois = self.salaireNetMensuel(annee,mois)
            salaireNetAnnuel += salaireMois
        return salaireNetAnnuel

    def impotsMensuel(self, annee, mois):
        return self._impotsMensuel

    def impotsNetAnnuel(self, annee):
        cumulImpotAnnee = 0.0
        for mois in range(0, 12):
            impotMois = self.impotsMensuel(annee,mois)
            cumulImpotAnnee += impotMois
        return cumulImpotAnnee



