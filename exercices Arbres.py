#Les fonctions de base sur la manipulation des arbres binaires.
def creerArbre(val,gauche,droit):
    return [val,[gauche,[],[]],[droit,[],[]]]
    
def vide(a):
    return a==[]
    
def val(a):
    if a!=[]:
        return a[0]
    else:
        return None


    
    
def filsGauche(a):
    if not vide(a):
         return a[1]
    else:
        return []
    
def filsDroit(a):
    if not vide(a):
        return a[2]
    else:
        return []
    
def prefixe(a):
    if not vide(a): 
        print (val(a), end=' ')
        prefixe(filsGauche(a))
        prefixe(filsDroit(a))
    
def infixe(a):
    if not vide(a): 
        infixe(filsGauche(a))
        print (val(a), end=' ')
        infixe(filsDroit(a))
           
def postfixe(a):
    if not vide(a): 
        postfixe(filsGauche(a))
        postfixe(filsDroit(a))
        print (val(a), end=' ')



def prefixeIter(a):
    P=[]
    P.append(a)
    while not vide(P):
        n=P.pop()
        if n!=[]:
            print(val(n),end=' ')
            P.append(filsDroit(n))
            P.append(filsGauche(n))
    print()
    
def prefixeIter2(a):
    P=[]
    P.append(a)
    while not vide(P):
        n=P.pop()
        print(val(n),end=' ')
        if not vide(filsDroit(n)) : P.append(filsDroit(n))
        if not vide(filsGauche(n)): P.append(filsGauche(n))    
           
    print()
    
    
#parcourir un arbre en largeur
def parcourLargeur(a):
    F=[]                   #File FIFO
    F.append(a)            #enfiler a dans la file F
    while not vide(F):
        n=F[0] ; F=F[1:]    #défiler F
        if n!=[]:
            print(val(n),end=' ')
            F.append(filsGauche(n))
            F.append(filsDroit(n))
    print()
    
def parcourLargeur2(a):
    F=[]                   #File FIFO
    F.append(a)            #enfiler a dans la file F
    while not vide(F):
        n=F[0] ; F=F[1:]    #défiler F
        print(val(n),end=' ')
        if not vide(filsGauche(n)): F.append(filsGauche(n))
        if not vide(filsDroit(n)) : F.append(filsDroit(n))
    print()
            


#Algorithmes de base sur les arbres binaires
def hauteur(a):
    if vide(a) or estFeuille(a):
        return 0
    else:
        return 1 + max (hauteur(filsGauche(a)) , hauteur(filsDroit(a)))
        
        
def nombreNoeuds(a):
    if vide(a): 
        return 0
    else:
        return 1 + nombreNoeuds(filsGauche(a)) + nombreNoeuds(filsDroit(a))
        

def estFeuille(a):
    if vide(a) : return False 
    return a[1]==[] and a[2]==[]
    
def nombreFeuilles(a):
    if vide(a): 
        return 0
    elif estFeuille(a):
        return 1
    else:
        return nombreFeuilles(filsGauche(a)) + nombreFeuilles(filsDroit(a))
        

def estNoeudInterne(a):
    if a==[] : return False 
    return not estFeuille(a)
    
def nombreNoeudInternes(a):
    if vide(a): 
        return 0
    elif estFeuille(a):
        return 0
    else:
        return 1+ nombreNoeudInternes(filsGauche(a)) + nombreNoeudInternes(filsDroit(a))
    
#fonction de recherche dans un arbre binaire quelconque
def existe(a, x):
    if vide(a):
        return False
    else:
        if val(a) ==x:
            return True
        else:
            return existe(filsGauche(a),x ) or existe(filsDroit(a), x)

#Opérations sur un Arbre Binaire de Recherche (ABR)
A=[9, [4, [3, [1,[],[]], [2,[],[]]], [5, [], []]], [12, [], [19, [18, [], []], [20, [], []]]]]

def rechercheIter(v,a):
    while not vide(a) and v!=val(a):
        if v< val(a):
            a=filsGauche(a)
        else:
            a=filsDroit(a)
        
    if vide(a): return False
    return True
    

def rechercheRec(v,a):
    if vide(a):
        return False
    if v==val(a):
        return True
    if v<val(a):
        return rechercheRec(v,filsGauche(a))
    else:
        return rechercheRec(v,filsDroit(a))
        
def Maximum(a):
    if vide(a): return None
    while not vide(filsDroit(a)):
       a=filsDroit(a);
    
    return val(a)
    
def MaximumRec(a):
    if not vide(a):
        if vide(filsDroit(a)):
            return val(a)
        else:
            return MaximumRec(filsDroit(a))
        
    
def Minimum(a):
    if vide(a): return None
    while not vide(filsGauche(a)):
       a=filsGauche(a);
    
    return val(a)
    
    
def MinimumRec(a):
    if not vide(a):
        if vide(filsGauche(a)):
            return val(a)
        else:
            return MinimumRec(filsGauche(a))
        
    
#insertion d'une valeur V dnas un ABR
def insertion(v,a):
    if vide(a):
        a+= [v,[],[]]
    else:
        if v<=val(a):
             insertion(v,filsGauche(a))
        else:
             insertion(v,filsDroit(a))
    
#suppression
'''
def supprimer(v,a):
    if not vide(a):
        if v<val(a):
            supprimer(v,filsGauche(a))
        elif v>val(a):
            supprimer(v,filsDroit(a))
        else:
            if estFeuille(a):
                return []
            elif vide(filsDroit(a)):
                return filsGauche(a)
            elif vide(filsGauche(a)):
                return filsDroit(a)
  '''          
            
            
        
    
a=[8, [6, [4, [], []], [4, [], []]], [14, [], []]]
def somme(a):
    if vide(a):
        return 0
    else:
        return val(a)+somme(filsGauche(a))+somme(filsDroit(a))

def sommeEgaux(a):
    if vide(a):
        return True
            
    if somme(filsGauche(a)) != somme(filsDroit(a)):
            return False
        
    #return sommeEgaux(filsGauche(a)) and sommeEgaux(filsDroit(a))
    if sommeEgaux(filsGauche(a)):
        return sommeEgaux(filsDroit(a))
    else:
        return False
        

def sommeEgauxIter(a):
    P=[]
    P.append(a)     #Empiler
    while P!=[]:
        n=P.pop()   #dépiler
        if n!=[]:
            s1=somme(filsGauche(n))
            s2=somme(filsDroit(n))
            if s1!=s2:
                return False
            P.append(filsDroit(n))
            P.append(filsGauche(n))
    
    return True    
        


T=[20, [19, [15,[],[]] , [16,[],[]] ],[18,[10,[],[]],[17,[],[]]]]
#Verification d'un Tas
def estTas(a):
    if vide(a) or estFeuille(a):
        return True
    
    if not vide(filsGauche(a)) and val(a)<val(filsGauche(a)):
            return False
        
    if not vide(filsDroit(a)) and val(a)<val(filsDroit(a)):
            return False
        
    return estTas(filsDroit(a)) and estTas(filsGauche(a))
    
    
#Elément plus profond d'un ABR
def ElementPlusProfond(a):
    P=[]
    P.append(a)
    while P!=[]:
        n=P.pop()
        if n!=[]:
            print(val(n),end=' ')
            P.append(filsDroit(n))
            P.append(filsGauche(n))
        
            
    print()
    
    
    

    
def profondeurMAx(a):
    if vide(a) or estFeuille(a):
        return 0
    return 1+max(profondeurMAx(filsGauche(a)),profondeurMAx(filsDroit(a)))
    
    
""" 
Cette fonction doit chercher une feuille , pas uniquement un sous-arbre vide 
(pour éviter de s’arrêter au niveau d ’un noeud n ’ayant qu’un fils).
"""    
def profondeurMin ( a ) :
    if vide(a) or estFeuille(a):
        return 0
    else:
        return 1 + min(profondeurMin( filsGauche ( a ) ) , profondeurMin (filsDroit ( a ) ) )
        
def feuilleMoinsProfonde(a):
    if estFeuille(a):
        return val(a)
    
    if profondeurMin(filsGauche(a) )<= profondeurMin ( filsDroit(a) ):
            return feuilleMoinsProfonde(filsGauche(a))
    else:
            return feuilleMoinsProfonde(filsDroit(a))


def feuillePlusProfonde(a):
    if estFeuille(a):
        return val(a)
    
    if hauteur(filsGauche(a))>=hauteur(filsGauche(a)):
        return feuillePlusProfonde(filsGauche(a))
    else:
        return feuillePlusProfonde(filsDroit(a))

def valExpression(a):
    if vide(a): return 0
    if val(a)=='+': 
      return valExpression(filsGauche(a))+valExpression(filsDroit(a))
    elif val(a)=='*': 
      return valExpression(filsGauche(a))*valExpression(filsDroit(a))
    elif val(a)=='-': 
      return valExpression(filsGauche(a))-valExpression(filsDroit(a))
    elif val(a)=='/': 
      return valExpression(filsGauche(a))/valExpression(filsDroit(a))
    else:
        return val(a)
    
