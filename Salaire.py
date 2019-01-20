class Salaire:

    def __init__(self, salaireNetMensuel, impotsMensuel, tranche):
        self._salaireNetMensuel = salaireNetMensuel
        self._impotsMensuel = impotsMensuel
        self._tranche = tranche

    def debugPrint(self):
        print "Salaire net mensuel: " + str(self._salaireNetMensuel)
        print "Impots mensuels: " + str(self._impotsMensuel)
        print "Tranche: " + str(self._tranche) + "%"

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



