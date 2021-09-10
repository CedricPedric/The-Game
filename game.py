print("""
Tijdens het bergbeklimmen keek je niet goed uit en struikelde je!
Je viel naar achter in een groot donker gat!
Naar boven klimmen is lijkt geen optie te zijn en als je om je heen kijkt ben je in een oude Ruïne!
""")

beginKeuze = input("""Je ziet maar twee paden die te nemen zijn. Een pad gaat de Ruïne in en het andere pad lijkt naar een begroeit pad tegaan. 
Je hebt de keuze uit |ruins en forest| welk pad kies je?: """)

if beginKeuze.lower().strip() == "ruins":
    print("Je besluit het pad wat veder in de Ruïne gaat tenemen!")
    ruinsKeuze1 = input("Het pad splitst in tweeën! Links hoor je geluid maar Rechts zie je daglicht! right or left: ") 
    if ruinsKeuze1.lower().strip() == "right":
        print("Je volgt het licht! Jammer genoeg was dit geen daglicht maar het Vuur van een DRAAK!")
        print("Je staat stokstijf stil van angst en voordat je kan rennen eet de DRAAK je op! ")
        print("You lose!")
    else:
        print("Je blijft het geluid volgen! Het blijkt een pratende deur te zijn!")
        print("De deur zegt beantwoord mijn vragen en je mag er langs zoniet sneuvel je waar je staat!")
        deurKeuze2 =  int(input("De eerste vraag die ik je vraag is! Welk getal is groter dan 3!: "))
        if deurKeuze2>3:
            print("Goed gedaan! Nu een nog moeilijkere vraag")
            deurKeuze3 = int(input("Van 1 tot 10 hoe knap ben ik? : "))
            if deurKeuze3 >= 6 and deurKeuze3 <=9:
                print("De deur zegt: Je bent aardig reiziger jij mag er langs!")
                print("Na het pad te volgen achter de deur kom je een klein winkeltje tegen wat het pad blokeert!")
                print("In de winkel zit een groene goblin met een hoedje op een hoge stoel en vraagt: WAT WIL JE KOPEN OF WIL JE ER LANGS!")
                goblinKeuze4 = input("Wat koop je van de goblin? doorgang of chocomelk: ")
            elif deurKeuze3 >= 10:
                print("De deur zegt: Als ik wangen had zou ik blozen! Je bent aardig reiziger jij mag er langs!")
                print("Na het pad te volgen achter de deur kom je een klein winkeltje tegen wat het pad blokeert!")
                print("In de winkel zit een groene goblin met een hoedje op een hoge stoel en vraagt: WAT WIL JE KOPEN!")
                goblinKeuze4 = input("Wat koop je van de goblin? doorgang of chocomelk (hidden ending kies friendship!): ") 
            else:
                print("De deur: Kijkt verdrietig en schiet een laser tussen je ogen in!")
                print("You lose!")
        
            if goblinKeuze4.lower().strip() == ("chocomelk"):
                print("Je hebt nu chocomelk! Het is lekker maar je geld is nu op!")
                print("You lose! (maar je hebt chocomelk!)")
            elif goblinKeuze4.lower().strip() == ("doorgang"):
                print("Je koopt een ticket om door te lopen. Na het lopen kom je bij de uitgang en zie je eindelijk weer het daglicht!")
                print("Je bent nu wel buiten maar welke andere avonturen waren te in de grot te vinden?")
                print("You Escaped!")
            elif goblinKeuze4.lower().strip() ==("friendship"):
                print("Mijn vriendschap is niet te koop! MAAR ik wil wel vrienden met je zijn...")
                print("De goblin helpt je naar buiten en jullie worden vrienden")
                print("Friendship ending!")
            else:
                print("Dat verkoop ik niet! Start maar opnieuw!")
        else:
            print("De deur schreeuwt: Ik wist dat dit te moeilijk voor je was!")
            print("De deur schiet een laser tussen je ogen in!")
            print("You lose!")


elif beginKeuze.lower().strip() == "forest":
    print("Je loopt weg van de Ruïne en je gaat naar het groenige deel van de grot")
    forestKeuze5 = input("Rechts hoor je water maar Links zie je lianen die naar boven gaan! Kies je right or left?: ")
    if forestKeuze5.lower().strip() == "left":
        print("Links! de lianen leiden inderdaad naar boven")
        print("Maar de lianen zijn niet stabiel en breken als je naar boven klimt! Helaas val je dood neer!")
        print("You lose!")

    elif forestKeuze5.lower().strip() == "right":
        print("Rechts! Je instict was juist en hier is een riviertje wat veder naar beneden gaat in de grot. Hier ligt ook een klein bootje")
        rivierKeuze6 = input("Ga je tegen de stroming in of met de stroming mee? tegen of mee: ")
        if rivierKeuze6.lower().strip() == "tegen":
            print("Je wordt erg snel uitgeput. Zo uitgeput zelfs dat je bijna opgeeft maar je ziet een touw naar beneden vallen!")
            touwKeuze7 = input("Pak je het touw? yes or no:")
            if touwKeuze7.lower().strip() == "yes":
                print("Op het nippertje pak je het touw!")
                print("Je wordt naar boven getrokken door je vrienden die je aan het zoeken waren. Je bent weer boven en veilig maar wat was er nog meer in de grot?")
                print("You Escaped")
            else:
                print("Het touw pakken lukte niet je de strooming was te sterk en het neemt je met tegen de rotsen aan")
                print("Je lanceerd door de stroming tegen een rots aan en drijft dood naar beneden!")
                print("You lose!")
        elif rivierKeuze6.lower().strip() == "mee":
            print("Net een achtbaan! Je hoeft niet eens te roeien en je bent al beneden")
            print("Beneden is het erg vochtig, donker en klein")
            print("Je hoort een stem komen van het donker")
            print("De stem vraagt: W A T  I S  J E  N A A M?!?:")
            grotKeuze8 = input("Vertel je de stem je naam?: yes or no: ")
            if grotKeuze8.lower().strip() == "yes":
                naam = input("Type de naam die je aan de stem verteld: ")
                print("H M M M M " + str(naam) + " W A T  E E N  A P A R T E  N A A M")
                grotKeuze9 = input("B E N  J E  H I E R  V O O R  M I J N  S C H A T ? yes or no: ")
                if grotKeuze9.lower().strip() == "yes":
                    print("Terwijl je je zin afprobeerd te maken verbrand de stem je levend!")
                    print("You lose!")
                else:
                    print("N I E T  H I E R  V O O R  M I J N  S C H A T ?")
                    grotKeuze10 = input("W A A R O M  B E N  J I J  I N  M I J N  K A S T E E L ? waarheid or lieg: ")
                    if grotKeuze10.lower().strip() == "lieg":
                        print("De stem heeft door dat je loog en verbrand je levend!")
                        print("You lose!")
                    elif grotKeuze10.lower().strip() == "waarheid":
                        print("HA HA HA HA HA HA")
                        print("WAT EEN LEUKE SITUATIE! GEEN PROBLEEM STAP OP ME RUG EN PAK WAT GOUD IK HELP JE OM WEER NAAR JE KAMP TE KOMEN!")
                        print("IK HEB IN TIJDEN NIET ZO GELACHEN HA HA HA")
                        print("De draak brengt je terug naar het kamp met een tas vol goud!")
                        print("You win!")
            else:
                print("In plaats van de stem te antwoorden ben je stil")
                print("Je hoort de stem niet meer maar je voelt wel iets heets naar je toe komen")
                print("Voordat je het weet wordt je levend verbrand door vuur")
                print("You lose!")
    else: 
        print("Invalid Option")


elif beginKeuze.lower().strip() == "naar huis":
    print("Je klimt naar boven en geniet thuis van de warme chocomelk")
    print("Hidden Ending!")

else:
    print("Invalid Option")