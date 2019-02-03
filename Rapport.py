# coding: utf8
import Appartement
import Rent
import Credit
import Compte
import Salaire
import Pinel
import VideMicroFoncier
import Scenario
import xlwt

scenario = Scenario.Scenario()
scenario._appartement = Appartement.Appartement(153000, 4434);
scenario._credit = Credit.Credit(scenario._appartement, 1.5, 0.4, 0, 2204, 264, 2019, 02)
scenario._bank = Compte.Compte(0, 2, 2021, 0)
scenario._rent = Rent.Rent(485, 485*0.17, 0.01, 2021, 02, 485)
scenario._salaire = Salaire.Salaire(3800, 712, 30)
scenario._pinel = Pinel.Pinel(Pinel.Pinel.TYPE_6_3_3, scenario._credit, scenario._appartement);
scenario._strategie = VideMicroFoncier.VideMicroFoncier(scenario._credit, scenario._appartement, scenario._rent, scenario._salaire);

# print ""
# print "Annee\tCredit\tLoyer\tCharges\tBanque\tPinel\tc.cred\tCapital\tImpots"
# print "\t+Assu\t\t+TxFonc\t\t\t\trestant"
# print "----------------------------------------------------------------"
# for annee in range(2018, 2050):
# 	rapportLine = str(annee) + "\t" 
# 	rapportLine += str(int(c.annuitePretAmortissable(annee) + c.annuiteAssurance(annee))) + "\t" 
# 	rapportLine += str(int(r.loyerBrutAnnuel(annee))) + "\t" 
# 	rapportLine += str(int(r.chargesAnnuelles(annee))) + "\t" 
# 	rapportLine += str(int(b.capitalMensuel(annee, 11, r, c, s))) + "\t" 
# 	rapportLine += str(int(p.reductionImpotsAnnuel(annee))) + "\t" 
# 	rapportLine += str(int(c.interetsEmpruntsAnnee(annee))) + "\t" 
# 	rapportLine += str(int(c.capitalRestantAnnee(annee))) + "\t" 
# 	rapportLine += str(int(i.impotsAnnuel(annee))) + "\t" 
# 	print rapportLine

workbook = xlwt.Workbook(encoding="UTF-8")
sheetScenarios = workbook.add_sheet('scenarios')

# print headers
line = 1
line = scenario._appartement.sheetPrintHeader(sheetScenarios, line, 0)
line = scenario._credit.sheetPrintHeader(sheetScenarios, line, 0)
line = scenario._bank.sheetPrintHeader(sheetScenarios, line, 0)
line = scenario._rent.sheetPrintHeader(sheetScenarios, line, 0)
line = scenario._salaire.sheetPrintHeader(sheetScenarios, line, 0)
# print values
line = 1
line = scenario._appartement.sheetPrint(sheetScenarios, line, 1)
line = scenario._credit.sheetPrint(sheetScenarios, line, 1)
line = scenario._bank.sheetPrint(sheetScenarios, line, 1)
line = scenario._rent.sheetPrint(sheetScenarios, line, 1)
line = scenario._salaire.sheetPrint(sheetScenarios, line, 1)

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
	sheetAnnuites.write(line, 1, int(scenario._credit.annuitePretAmortissable(annee) + scenario._credit.annuiteAssurance(annee)))
	sheetLoyers.write(line, 0, annee)
	sheetLoyers.write(line, 1, scenario._rent.loyerBrutAnnuel(annee))
	sheetCharges.write(line, 0, annee)
	sheetCharges.write(line, 1, scenario._rent.chargesAnnuelles(annee))
	sheetCapital.write(line, 0, annee)
	sheetCapital.write(line, 1, scenario._bank.capitalMensuel(annee, 11, scenario._rent, scenario._credit, scenario._salaire))
	sheetReduction.write(line, 0, annee)
	sheetReduction.write(line, 1, scenario._pinel.reductionImpotsAnnuel(annee))
	sheetInterets.write(line, 0, annee)
	sheetInterets.write(line, 1, scenario._credit.interetsEmpruntsAnnee(annee))
	sheetCapitalRestant.write(line, 0, annee)
	sheetCapitalRestant.write(line, 1, scenario._credit.capitalRestantAnnee(annee))
	sheetImpots.write(line, 0, annee)
	sheetImpots.write(line, 1, scenario._strategie.impotsAnnuel(annee))
	line = line + 1

workbook.save('rapport.xls')
