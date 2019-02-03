# coding: utf8
import Appartement
import Rent
import Credit
import Compte
import Salaire
import Pinel
import VideMicroFoncier
import xlwt

a = Appartement.Appartement(153000, 4434);
a.debugPrint()

c = Credit.Credit(a, 1.5, 0.4, 0, 2204, 264, 2019, 02)
c.debugPrint()

b = Compte.Compte(0, 2, 2021, 0)
b.debugPrint()

r = Rent.Rent(485, 485*0.17, 0.01, 2021, 02, 485)
r.debugPrint()

s = Salaire.Salaire(3800, 712, 30)
s.debugPrint();

p = Pinel.Pinel(Pinel.Pinel.TYPE_6_3_3, c, a);
p.debugPrint();

i = VideMicroFoncier.VideMicroFoncier(c, a, r, s);
i.debugPrint();

#print c.capitalRestantAnnee(2041)
#exit(0);

print ""
print "Annee\tCredit\tLoyer\tCharges\tBanque\tPinel\tc.cred\tCapital\tImpots"
print "\t+Assu\t\t+TxFonc\t\t\t\trestant"
print "----------------------------------------------------------------"
for annee in range(2018, 2050):
	rapportLine = str(annee) + "\t" 
	rapportLine += str(int(c.annuitePretAmortissable(annee) + c.annuiteAssurance(annee))) + "\t" 
	rapportLine += str(int(r.loyerBrutAnnuel(annee))) + "\t" 
	rapportLine += str(int(r.chargesAnnuelles(annee))) + "\t" 
	rapportLine += str(int(b.capitalMensuel(annee, 11, r, c, s))) + "\t" 
	rapportLine += str(int(p.reductionImpotsAnnuel(annee))) + "\t" 
	rapportLine += str(int(c.interetsEmpruntsAnnee(annee))) + "\t" 
	rapportLine += str(int(c.capitalRestantAnnee(annee))) + "\t" 
	rapportLine += str(int(i.impotsAnnuel(annee))) + "\t" 
	print rapportLine

workbook = xlwt.Workbook(encoding="UTF-8")
sheetScenarios = workbook.add_sheet('scenarios')

# print headers
line = 1
line = a.sheetPrintHeader(sheetScenarios, line, 0)
line = c.sheetPrintHeader(sheetScenarios, line, 0)
line = b.sheetPrintHeader(sheetScenarios, line, 0)
line = r.sheetPrintHeader(sheetScenarios, line, 0)
line = s.sheetPrintHeader(sheetScenarios, line, 0)
# print values
line = 1
line = a.sheetPrint(sheetScenarios, line, 1)
line = c.sheetPrint(sheetScenarios, line, 1)
line = b.sheetPrint(sheetScenarios, line, 1)
line = r.sheetPrint(sheetScenarios, line, 1)
line = s.sheetPrint(sheetScenarios, line, 1)

sheetAnnuites = workbook.add_sheet('Annuités')
sheetLoyers = workbook.add_sheet('Loyers Bruts')
sheetCharges = workbook.add_sheet('Charges')
sheetCapital = workbook.add_sheet('Capital')
sheetReduction = workbook.add_sheet('Réduction impots')
sheetInterets = workbook.add_sheet('Intérêts')
sheetCapitalRestant = workbook.add_sheet('Capital Restant')
sheetImpots = workbook.add_sheet('Impots Annuels')

line = 1
for annee in range(2018, 2050):
	sheetAnnuites.write(line, 0, annee)
	sheetAnnuites.write(line, 1, int(c.annuitePretAmortissable(annee) + c.annuiteAssurance(annee)))
	sheetLoyers.write(line, 0, annee)
	sheetLoyers.write(line, 1, r.loyerBrutAnnuel(annee))
	sheetCharges.write(line, 0, annee)
	sheetCharges.write(line, 1, r.chargesAnnuelles(annee))
	sheetCapital.write(line, 0, annee)
	sheetCapital.write(line, 1, b.capitalMensuel(annee, 11, r, c, s))
	sheetReduction.write(line, 0, annee)
	sheetReduction.write(line, 1, p.reductionImpotsAnnuel(annee))
	sheetInterets.write(line, 0, annee)
	sheetInterets.write(line, 1, c.interetsEmpruntsAnnee(annee))
	sheetCapitalRestant.write(line, 0, annee)
	sheetCapitalRestant.write(line, 1, c.capitalRestantAnnee(annee))
	sheetImpots.write(line, 0, annee)
	sheetImpots.write(line, 1, i.impotsAnnuel(annee))
	line = line + 1

workbook.save('rapport.xls')
