class SheetOutput:

    def __init__(self):
        self._currentLine = 0
        self._currentColumn = 0

    def writeXLS(self, sheet, value):
        sheet.write(self._currentLine, self._currentColumn, value)
        self._currentLine = self._currentLine + 1

    def startWriteXML(self, line, col):
        self._currentLine = line
        self._currentColumn = col


