print("""
Tijdens het bergbeklimmen keek je niet goed uit en struikelde je!
Je viel naar achter in een groot donker gat!
Naar boven klimmen is lijkt geen optie te zijn en als je om je heen kijkt ben je in een oude Ruïne!
""")

def YesOrNokeuze(vraag):
    antwoord = input(vraag)
    if antwoord == 'ja':
        return True
    elif antwoord == 'nee':
        return False
    else:
        print('Invalid Option Try Again')
        return YesOrNokeuze(vraag)

def LeftOrRightKeuze(vraag):
    antwoord = input(vraag)
    if antwoord == 'left':
        return True
    elif antwoord == 'right':
        return False
    else:
        print('Invalid Option Try Again')
        return LeftOrRightKeuze(vraag)

def beginKeuze(vraag):
    antwoord = input(vraag)
    if antwoord == 'ruins':
        return True
    elif antwoord == 'forest':
        return False
    else:
        print('Invalid Option Try Again')
        return beginKeuze(vraag)

def deurKeuze(vraag):
    antwoord = int(input(vraag))
    if antwoord > 3:
        return True
    else:
        return False

def deurconditie1(nummer):
    if nummer >= 10:
        return True
    else:
        return False

def deurconditie2(nummer):
    if nummer >=6 and nummer <=9:
        return True
    else:
        return False
def deurconditie3(nummer):
    if nummer < 6:
        return True

def goblinConditie(vraag):
    antwoord = input(vraag)
    if antwoord == 'chocomelk':
        print('You lose! maar je hebt chocomelk')
    elif antwoord == 'doorgang':
        print("Je koopt een ticket om door te lopen. Na het lopen kom je bij de uitgang en zie je eindelijk weer het daglicht!")
        print("Je bent nu wel buiten maar welke andere avonturen waren te in de grot te vinden?")
        print("You Escaped!")
    elif antwoord == 'friendship':
        print("Mijn vriendschap is niet te koop! MAAR ik wil wel vrienden met je zijn...")
        print("De goblin helpt je naar buiten en jullie worden vrienden")
        print("Friendship ending!")
    else:
        print('Dat verkoop ik niet ik verkoop chocomelk en doorgang!')
        return goblinConditie(vraag)


def bootKeuze(vraag):
    antwoord = input(vraag)
    if antwoord == 'tegen':
        return True
    elif antwoord == 'mee':
        return False
    else:
        print('Invalid Option')
        return bootKeuze(vraag)

def draakNaam():
    naam = input("Type de naam die je aan de stem verteld: ")
    print("H M M M M " + str(naam) + " W A T  E E N  A P A R T E  N A A M")

def draakKeuze(vraag):
    antwoord = input(vraag)
    if antwoord == 'lieg':
        print("De stem heeft door dat je loog en verbrand je levend!")
        print("You lose!")
    elif antwoord == 'waarheid':
        print("HA HA HA HA HA HA")
        print("WAT EEN LEUKE SITUATIE! GEEN PROBLEEM STAP OP ME RUG EN PAK WAT GOUD IK HELP JE OM WEER NAAR JE KAMP TE KOMEN!")
        print("IK HEB IN TIJDEN NIET ZO GELACHEN HA HA HA")
        print("De draak brengt je terug naar het kamp met een tas vol goud!")
        print("You win!")
    
    

if beginKeuze("""Je ziet maar twee paden die te nemen zijn. Een pad gaat de Ruïne in en het andere pad lijkt naar een begroeit pad tegaan. 
Je hebt de keuze uit |ruins en forest| welk pad kies je?: """):
     print("Je besluit het pad wat veder in de Ruïne gaat tenemen!")
     if LeftOrRightKeuze("Het pad splitst in tweeën! Links hoor je geluid maar Rechts zie je daglicht! right or left: "):
         print("Je blijft het geluid volgen! Het blijkt een pratende deur te zijn!")
         print("De deur zegt beantwoord mijn vragen en je mag er langs zoniet sneuvel je waar je staat!")
         if deurKeuze('Welk getal is groter dan 3: '):
             print("Goed gedaan! Nu een nog moeilijkere vraag")
             deurFlirt = int(input('Hoe knap ben ik: '))
             if deurconditie1(deurFlirt):
                 print("De deur zegt: Als ik wangen had zou ik blozen! Je bent aardig reiziger jij mag er langs!")
                 print("De goblin accepteerd ook 'friendship'")
                 print("Na het pad te volgen achter de deur kom je een klein winkeltje tegen wat het pad blokeert!")
                 print("In de winkel zit een groene goblin met een hoedje op een hoge stoel en vraagt: WAT WIL JE KOPEN!")
                 goblinConditie('ik verkoop chocomelk en doorgang|hidden ending = friendship: ')
             if deurconditie2(deurFlirt):
                 print("De deur zegt: Je bent aardig reiziger jij mag er langs!")
                 print("Na het pad te volgen achter de deur kom je een klein winkeltje tegen wat het pad blokeert!")
                 print("In de winkel zit een groene goblin met een hoedje op een hoge stoel en vraagt: WAT WIL JE KOPEN OF WIL JE ER LANGS!")
                 goblinConditie('ik verkoop chocomelk en doorgang: ')
             if deurconditie3(deurFlirt):
                 print("De deur: Kijkt verdrietig en schiet een laser tussen je ogen in!")
                 print("You lose!") 
         else:
             print("De deur: Kijkt verdrietig en schiet een laser tussen je ogen in!")
             print("You lose!")
     else:
         print("Je volgt het licht! Jammer genoeg was dit geen daglicht maar het Vuur van een DRAAK!")
         print("Je staat stokstijf stil van angst en voordat je kan rennen eet de DRAAK je op! ")
         print("You lose!")
else:
    print("Je loopt weg van de Ruïne en je gaat naar het groenige deel van de grot")
    if LeftOrRightKeuze('Rechts hoor je water maar Links zie je lianen die naar boven gaan! Kies je right or left?:'):
        print("Links! de lianen leiden inderdaad naar boven")
        print("Maar de lianen zijn niet stabiel en breken als je naar boven klimt! Helaas val je dood neer!")
        print("You lose!")
    else:
        print("Rechts! Je instict was juist en hier is een riviertje wat veder naar beneden gaat in de grot. Hier ligt ook een klein bootje")
        if bootKeuze('Ga je tegen de stroming in of met de stroming mee? tegen of mee: '):
            print("Je wordt erg snel uitgeput. Zo uitgeput zelfs dat je bijna opgeeft maar je ziet een touw naar beneden vallen!")
            if YesOrNokeuze('Pak je het touw? yes or no:"'):
                print("Op het nippertje pak je het touw!")
                print("Je wordt naar boven getrokken door je vrienden die je aan het zoeken waren. Je bent weer boven en veilig maar wat was er nog meer in de grot?")
                print("You Escaped")
            else:
                print("Het touw pakken lukte niet je de strooming was te sterk en het neemt je met tegen de rotsen aan")
                print("Je lanceerd door de stroming tegen een rots aan en drijft dood naar beneden!")
                print("You lose!")
        else:
            print("Net een achtbaan! Je hoeft niet eens te roeien en je bent al beneden")
            print("Beneden is het erg vochtig, donker en klein")
            print("Je hoort een stem komen van het donker")
            print("De stem vraagt: W A T  I S  J E  N A A M?!?:")
            if YesOrNokeuze('Vertel je je naam yes or no: '):
                draakNaam()
                if YesOrNokeuze("B E N  J E  H I E R  V O O R  M I J N  S C H A T ? yes or no: "):
                    print("Terwijl je je zin afprobeerd te maken verbrand de stem je levend!")
                    print("You lose!")
                else:
                    print("N I E T  H I E R  V O O R  M I J N  S C H A T ?")
                    draakKeuze("W A A R O M  B E N  J I J  I N  M I J N  K A S T E E L ? waarheid or lieg: ")
                   

            else:
                print('Draak verbrand je')


