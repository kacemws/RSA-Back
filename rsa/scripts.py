from typing import Tuple

#tableau d'alphabet : globale
alpha  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha2 =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Prend une lettre et donne son indice (i) dans table d'alpha
def retourner_num_alpha (n : str) :
    i = 0
    while (i < len(alpha)) :
        #chercher dans alpha et alpha2 (masc/min) 
        if (alpha[i] == n) or (alpha2[i] == n):
            return i
        i += 1    
    return -1   #*pour faire les verification apre

#cas de cryptage: verification (si on a que des lettre ou pas)
def verifier_all_alpha(msg):
    for x in msg:
        if retourner_num_alpha(x) == -1: #si on n'a aucune lettre => false
            return False
    return True

#nombre premier
def isPrime(n):
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
 
    return True

#nombres premier entre eux
def comprime (a,b) :
    if pgcd(a,b) == 1:
        return True
    else: 
        return False

#pgcd
def pgcd(a,b) -> int:
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

#inverse modulo
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return 1

#choose e
def chooseE (n,p,q) -> int: 
    """ chercher e: 1<e<n & e comprime avec n qui est o = (p-1)*(q-1) """
    i = 2
    while i < n:
        if (comprime(i,n) and i != p and i != q):
            return i
        i += 1    
    return 0

#generation de cle
def keygeneration (p:int,q:int) -> Tuple [int,int]:
    n:int = p * q 
    o = (p-1)*(q-1)
    e:int = int (chooseE (o,p,q))
    publickey:tuple = (n,e)
    return publickey

#crypty le message
def crypter (message,p,q):
    #generation de cle
    publickey = keygeneration(p,q)
    n,e = publickey
    #o = (p-1)*(q-1)

    #parcourire le message (lettre par lettre)
    i : int = 0
    c = ''      #string pour afficher
    test = []   #tableau des chiffre :message crypter
    
    #processus de cryptage
    print('\ncryptage')
    while i < len(message) :
        

        #changer from alpha to num & appliquer la fonction
        s = retourner_num_alpha(message[i]) ** e % n
        c += str (alpha[(s%26)])    #message
        test.append(s)              #resultat
        print (retourner_num_alpha(message[i]),'->',s,'('+str(s%26)+')\t= ',message[i],'->',alpha[(s%26)],' ',c)    
        i += 1
    
    print('message = ',c,test ,'\n')
    return test

#decrypty le message
def decrypter (p,q,cry:[]):
    #generation du cle
    publickey = keygeneration(p,q)
    n,e = publickey
    o = (p-1)*(q-1)
    d = modInverse(e,o)

    #parcourir le message
    i : int = 0
    m = ''      #string pour l'affichage
    test = []   #tableau des lettre: decryptage de message

    print('\ndecryptage')
    while i < len(cry) :
        #processus de decryptage
        s = cry[i] ** d % n
        m += alpha[s%26]

        #le tableu decrypte les chiffres cryptées exact (sans %26)
        test.append(alpha[s])
        print (cry[i],'->',s,'\t= ',alpha[cry[i]%26],'->',alpha[s],' ',m)
        i += 1
        #processus de decryptage

    print ('message = ',m,test,'\n')
    return test

#affichage des element de l'algo
def affichage_element (p,q):
    publickey = keygeneration(p,q)
    n,e = publickey
    o = (p-1)*(q-1)
    d = modInverse(e,o)
    #print('p = ',p)
    #print('q = ',q)
    
    print('\no: ((p-1)*(q-1)) = ',o)
    print('n: (p * q) = ',n)
    print('e: (entier comprime avec o)= ',e)
    print('d: inverse modulo (e^-1 % \o)= ',d)

#verification d'input (int)
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 

#MAIN______________________________________________________________________________________________________________
def main() : 
    print('\n')
    print('introduire p et q (la cle private) : ')

    p = inputNumber ('p (premier > 2)= ')
    #verification
    while (not isPrime(p)) or (p <= 2):
        print ('Verifier vos information')
        p = inputNumber ('p = ')

    q = inputNumber ('q (premier > 2, different de p)= ')
    #verification
    while (not isPrime(q)) or (q <= 2) or (p == q): 
        print ('Verifier vos information')
        q = inputNumber ('q = ')

    #affichage les elements de l'algorithme
    affichage_element(p,q)

    #lire message
    message = input('\nintroduire votre message ')

    #lire choix
    choice = inputNumber('1 pour crypter | 2 pour decrypter')
    #verification
    while not (choice == 1 or choice == 2):
        print ('Verifier vos information (1 ou 2)')
        choice = inputNumber('1 pour crypter | 2 pour decrypter')
        
    #le message
    print ('\nVotre message : ',message)

    #crypter ou decrypter selon le choix
    if  choice == 1:
        #cryptage
        if verifier_all_alpha(message):
            test_cry = crypter (message,p,q)
        else:
            print ('Verifier vos informations  (il faut que les message soit des lettres pour le chiffrement)')

    elif choice == 2:
        #decryptage
        message += ',' #*ici pour evité l'utilsation du split avec un message sans ',' (evité l'echec)
        if True:
            tab = []
            for i in message.split(','):
                try:
                    tab.append(int(i))
                except:
                    print ('Verifier vos informations (il faut que les message soit des entier pour le dechiffrement)')
                    break
            decrypter (p,q,tab)
        else:
            print ('Verifier vos informations')    
    else:
        print('Verifier vos informations (choix) ')
    print('\n')