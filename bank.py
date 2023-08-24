class CompteBancaire:
    def init(self, t):
        self.titulaire = t
        self.solde = 0
    def deposer(self, amount):
        self.solde+= amount

    def retirer(self, amount):
        c = 0
        while amount > self.solde:
            c+=1 
            if c <= 2:
                amount = float(input("Insufficiant funds reneter an inferior amount: "))
            else:
                print("3eye9ti 3awej")
                break 
        else:
            self.solde-=amount
    def consulter_solde(self):
        print(self.solde)


account = CompteBancaire('Rihab')

while True:
    x= int(input("choisissez: \n 1) Pour consulter votre solde \n 2) pour deposer de l'argent \n 3) pour retirer\n 4)pour quitter \n"))
    while x < 1 or x > 4:
            x= int(input("choisissez: \n 1) Pour consulter votre solde \n 2) pour deposer de l'argent \n 3) pour retirer\n"))
    if x == 1:
        account.consulter_solde()
    elif x == 2:
        account.deposer(float(input("Saisir le montant: ")))
    elif x == 3: 
        account.retirer(float(input("Saisir le montant: ")))
    else:
        print("BYE\n")
        break
