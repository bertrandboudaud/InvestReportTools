from SheetOutput import SheetOutput

class Appartement(SheetOutput):

    def __init__(self, prixAcquisition, fraisAcquisition):
    	SheetOutput.__init__(self)
        self._prixAcquisition = prixAcquisition
        self._fraisAcquisition = fraisAcquisition

    def debugPrint(self):
        print "Prix d'acquition: " + str(self._prixAcquisition)
        print "Frais d'acquition: " + str(self._fraisAcquisition)

    def sheetPrint(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, self._prixAcquisition)
        self.writeXLS(sheet, self._fraisAcquisition)
        return self._currentLine;

    def sheetPrintHeader(self, sheet, line, col):
        self.startWriteXML(line, col)
        self.writeXLS(sheet, "Prix d'acquition")
        self.writeXLS(sheet, "Frais d'acquition")
        return self._currentLine;
