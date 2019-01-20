class Appartement:

    def __init__(self, prixAcquisition, fraisAcquisition):
        self._prixAcquisition = prixAcquisition
        self._fraisAcquisition = fraisAcquisition

    def debugPrint(self):
        print "Prix d'acquition: " + str(self._prixAcquisition)
        print "Frais d'acquition: " + str(self._prixAcquisition)
