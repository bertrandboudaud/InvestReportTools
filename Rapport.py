# coding: utf8
import Appartement
import Rent
import Credit
import Compte
import Salaire
import Pinel
import VideMicroFoncier
import xlwt
#from xlwt import Workbook

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
sheet = workbook.add_sheet('scenarios')

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


line = 1
line = a.sheetPrint(sheet, line, 1)

line=line+1;
line = c.sheetPrint(sheet, line, 1)

line=line+1;
line = b.sheetPrint(sheet, line, 1)

line=line+1;
line = r.sheetPrint(sheet, line, 1)

line=line+1;
line = s.sheetPrint(sheet, line, 1)

workbook.save('rapport.xls')
