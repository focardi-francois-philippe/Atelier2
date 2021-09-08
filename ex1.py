def calculImc(poids:int):
    """Fonction premettant de determiner l'imc en fonction d'un poids entrez """
    
    INTERPRETATIONIMCTEXT = ("denutrition ou famine","maigreur","corpulence normale","surpoids","obeisite modere","obeisite severe","obesite morbide")
    INTERPRETATIONIMCVALEURS = (16.5,18.5,25,30,35,40,41)
    resultat = ""
    x = 0
    if(poids<INTERPRETATIONIMCVALEURS[x]):
        resultat = INTERPRETATIONIMCTEXT[x]
          
    while(x<len(INTERPRETATIONIMCVALEURS)):
        if(poids>=INTERPRETATIONIMCVALEURS[x]):
            resultat = INTERPRETATIONIMCTEXT[x]
        x+=1
    return resultat
        
def test():
    print(calculImc(18))
    print(calculImc(25))


test()
    