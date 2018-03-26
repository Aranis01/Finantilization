from tkinter import *
from random import  *
from math import *
from pygame import *
import time

'''
--------------------------- 	Changements de périodes 	----------------------------
'''

#Quand on passe au Moyen-Age
def AntiquitéFini():
	global Acheter1, Acheter2, Acheter3,Acheter4,Acheter5,Acheter6,Acheter7,Acheter8,Bouton1,Bouton2,Bouton3,Bouton4,Bouton5,Bouton6,Bouton7,Bouton8,benefice1,benefice2,benefice3,benefice4,benefice5,benefice6,benefice7,benefice8
	global action, A_action,B_action,C_action,A_x,B_x,C_x,A_y,B_y,C_y,Money,Ben1,Ben2,Ben3,Ben4,Ben5,Ben6,Ben7,Ben8,MoyenAge
	Ben1 = 5
	Ben2 = 10
	Ben3 = 50
	Ben4 = 100 
	Ben5 = 250
	Ben6 = 500
	Ben7 = 1000
	Ben8 = 0
	benefice1 = False
	benefice2 = False
	benefice3 = False
	benefice4 = False
	benefice5 = False
	benefice6 = False
	benefice7 = False
	benefice8 = False
	Ben1division = 2
	Ben2division = 8
	Ben3division = 25
	Ben4ivision = 83
	Ben5division = 250
	Ben6division = 833
	Ben7division = 1666
	MoyenAge = True
	Acheter1.config(text="Acheter un Cerf pour 120 écus"+ ": +" + str(Ben1) + " / tour", state=NORMAL, command= lambda prix=120, benefice=Ben1:acheter(prix,benefice))
	Acheter2.config(text="Acheter les terres d'un paysant pour 500 écus"+ ": +" + str(Ben2) + " / tour", state=NORMAL,command= lambda prix=500, benefice=Ben2:acheter(prix,benefice))
	Acheter3.config(text="Acheter une Forge pour 1 500 écus"+ ": +" + str(Ben3) + " / tour",state=NORMAL, command= lambda prix=1500, benefice=Ben3:acheter(prix,benefice))
	Acheter4.config(text="Acheter une Orfèvrerie pour 5 000 écus"+ ": +" + str(Ben4) + " / tour",state=NORMAL, command= lambda prix=5000, benefice=Ben4:acheter(prix,benefice))
	Acheter5.config(text="Acheter la demeure d'un seigneur pour 15 000 écus"+ ": +" + str(Ben5) + " / tour",state=NORMAL, command= lambda prix=15000, benefice=Ben5:acheter(prix,benefice))
	Acheter6.config(text="Acheter la demeure d'un roi pour 50 000 écus"+ ": +" + str(Ben6) + " / tour", state=NORMAL,command= lambda prix=50000, benefice=Ben6:acheter(prix,benefice))
	Acheter7.config(text="Acheter le Royaume des francs pour 100 000 écus"+ ": +" + str(Ben7) + " / tour",state=NORMAL, command= lambda prix=100000, benefice=Ben7:acheter(prix,benefice))
	Acheter8.config(text="Acheter l'Europe Occidentale pour 1 000 000 écus",state=NORMAL,command= lambda prix=1000000, benefice= Ben8:acheter(prix,benefice))
	Monnait = "écus"
	Monnaient.title(Monnait)
	Entreprise.title("Foire")
	x=10
	y=100 
	A_x = x
	B_x = x
	C_x = x
	A_y = y
	B_y = y
	C_y = y
	xmodif = 20
	ymodif = 30
	A_xmodif = 20
	A_ymodif = 30
	B_xmodif = 20
	B_ymodif = 30
	C_xmodif = 20
	C_ymodif = 30
	action = randint(x,y)
	A_action = randint(x,y)
	B_action = randint(x,y)
	C_action = randint(x,y)
	Fenetre.title("Blé")
	Fenetre2.title("Pierre")
	Fenetre3.title("Viande")
	Fenetre4.title("Bois")
	Marché.config(text= "Blé")
	A_Marché.config(text= "Pierre")
	B_Marché.config(text= "Viande")
	C_Marché.config(text= "Bois")
	Money = 50
	argentLabel.config(text=Money)
	InvestirScale.config(to=Money)

#Quand on passe à la colonisation
def MoyenAgeFini():
	global Acheter1, Acheter2, Acheter3,Acheter4,Acheter5,Acheter6,Acheter7,Acheter8,Bouton1,Bouton2,Bouton3,Bouton4,Bouton5,Bouton6,Bouton7,Bouton8,benefice1,benefice2,benefice3,benefice4,benefice5,benefice6,benefice7,benefice8
	global action, A_action,B_action,C_action,A_x,B_x,C_x,A_y,B_y,C_y,Money,Ben1,Ben2,Ben3,Ben4,Ben5,Ben6,Ben7,Ben8,colonisation
	Ben1 = 20
	Ben2 = 80
	Ben3 = 500
	Ben4 = 1500 
	Ben5 = 4000
	Ben6 = 15000
	Ben7 = 40000
	Ben8 = 0
	benefice1 = False
	benefice2 = False
	benefice3 = False
	benefice4 = False
	benefice5 = False
	benefice6 = False
	benefice7 = False
	benefice8 = False
	Ben1division = 2
	Ben2division = 8
	Ben3division = 40
	Ben4ivision = 300
	Ben5division = 1000
	Ben6division = 4000
	Ben7division = 20000
	colonisation = True
	Acheter1.config(text="Acheter une barque pour 500 écus"+ ": +" + str(Ben1) + " / tour", state=NORMAL, command= lambda prix=500, benefice=Ben1:acheter(prix,benefice))
	Acheter2.config(text="Acheter un trois mats d'un paysant pour 2000 écus"+ ": +" + str(Ben2) + " / tour", state=NORMAL,command= lambda prix=2000, benefice=Ben2:acheter(prix,benefice))
	Acheter3.config(text="Acheter un bateau négrier pour 10 000 écus"+ ": +" + str(Ben3) + " / tour",state=NORMAL, command= lambda prix=10000, benefice=Ben3:acheter(prix,benefice))
	Acheter4.config(text="Acheter une plantation pour 75 000 écus"+ ": +" + str(Ben4) + " / tour",state=NORMAL, command= lambda prix=75000, benefice=Ben4:acheter(prix,benefice))
	Acheter5.config(text="Acheter Liverpool d'un seigneur pour 250 000 écus"+ ": +" + str(Ben5) + " / tour",state=NORMAL, command= lambda prix=250000, benefice=Ben5:acheter(prix,benefice))
	Acheter6.config(text="Acheter une île d'un roi pour 1 000 000 écus"+ ": +" + str(Ben6) + " / tour", state=NORMAL,command= lambda prix=1000000, benefice=Ben6:acheter(prix,benefice))
	Acheter7.config(text="Acheter l'Eldorado pour 5 000 000 écus"+ ": +" + str(Ben7) + " / tour",state=NORMAL, command= lambda prix=5000000, benefice=Ben7:acheter(prix,benefice))
	Acheter8.config(text="Acheter l'Amérique pour 30 000 000 écus",state=NORMAL,command= lambda prix=30000000, benefice= Ben8:acheter(prix,benefice))
	Monnait = "écus"
	Monnaient.title(Monnait)
	Entreprise.title("Commerce triangulaire")
	x=50
	y=200 
	A_x = x
	B_x = x
	C_x = x
	A_y = y
	B_y = y
	C_y = y
	xmodif = 45
	ymodif = 65
	A_xmodif = 45
	A_ymodif = 65
	B_xmodif = 45
	B_ymodif = 65
	C_xmodif = 45
	C_ymodif = 65
	action = randint(x,y)
	A_action = randint(x,y)
	B_action = randint(x,y)
	C_action = randint(x,y)
	Fenetre.title("Sucre")
	Fenetre2.title("Banane")
	Fenetre3.title("Cacao")
	Fenetre4.title("Esclaves Noirs")
	Marché.config(text= "Sucre")
	A_Marché.config(text= "Banane")
	B_Marché.config(text= "Cacao")
	C_Marché.config(text= "Esclaves")
	Money = 250
	argentLabel.config(text=Money)
	InvestirScale.config(to=Money)

#Quand on passe à la révolution industrielle
def ColonisationFini():
	global Acheter1, Acheter2, Acheter3,Acheter4,Acheter5,Acheter6,Acheter7,Acheter8,Bouton1,Bouton2,Bouton3,Bouton4,Bouton5,Bouton6,Bouton7,Bouton8,benefice1,benefice2,benefice3,benefice4,benefice5,benefice6,benefice7,benefice8
	global action, A_action,B_action,C_action,A_x,B_x,C_x,A_y,B_y,C_y,Money,Ben1,Ben2,Ben3,Ben4,Ben5,Ben6,Ben7,Ben8,industriel
	Ben1 = 15
	Ben2 = 75
	Ben3 = 300
	Ben4 = 1000 
	Ben5 = 7500
	Ben6 = 50000
	Ben7 = 150000
	Ben8 = 0
	benefice1 = False
	benefice2 = False
	benefice3 = False
	benefice4 = False
	benefice5 = False
	benefice6 = False
	benefice7 = False
	benefice8 = False
	Ben1division = 2
	Ben2division = 7
	Ben3division = 36
	Ben4ivision = 253
	Ben5division = 1600
	Ben6division = 8000
	Ben7division = 400000
	industriel = True
	Acheter1.config(text="Acheter un gamin des rues pour 750 écus"+ ": +" + str(Ben1) + " / tour", state=NORMAL, command= lambda prix=750, benefice=Ben1:acheter(prix,benefice))
	Acheter2.config(text="Acheter un bar à tabac d'un paysant pour 2500 écus"+ ": +" + str(Ben2) + " / tour", state=NORMAL,command= lambda prix=2500, benefice=Ben2:acheter(prix,benefice))
	Acheter3.config(text="Acheter une mine de charbon pour 13 000 écus"+ ": +" + str(Ben3) + " / tour",state=NORMAL, command= lambda prix=13000, benefice=Ben3:acheter(prix,benefice))
	Acheter4.config(text="Acheter une usine pour 95 000 écus"+ ": +" + str(Ben4) + " / tour",state=NORMAL, command= lambda prix=95000, benefice=Ben4:acheter(prix,benefice))
	Acheter5.config(text="Acheter le métro pour 600 000 écus"+ ": +" + str(Ben5) + " / tour",state=NORMAL, command= lambda prix=600000, benefice=Ben5:acheter(prix,benefice))
	Acheter6.config(text="Acheter le réseau de chemin de fer pour 3 000 000 écus"+ ": +" + str(Ben6) + " / tour", state=NORMAL,command= lambda prix=3000000, benefice=Ben6:acheter(prix,benefice))
	Acheter7.config(text="Acheter Londres pour 150 000 000 écus"+ ": +" + str(Ben7) + " / tour",state=NORMAL, command= lambda prix=150000000, benefice=Ben7:acheter(prix,benefice))
	Acheter8.config(text="Acheter le monde industriel pour 1 000 000 000 écus",state=NORMAL,command= lambda prix=1000000000, benefice= Ben8:acheter(prix,benefice))
	Monnait = "écus"
	Monnaient.title(Monnait)
	Entreprise.title("Marché Noir")
	x=75
	y=250
	A_x = x
	B_x = x
	C_x = x
	A_y = y
	B_y = y
	C_y = y
	xmodif = 90
	ymodif = 130
	A_xmodif = 90
	A_ymodif = 130
	B_xmodif = 90
	B_ymodif = 130
	C_xmodif = 90
	C_ymodif = 130
	action = randint(x,y)
	A_action = randint(x,y)
	B_action = randint(x,y)
	C_action = randint(x,y)
	Fenetre.title("Pétrole")
	Fenetre2.title("Charbon")
	Fenetre3.title("Acier")
	Fenetre4.title("Papier")
	Marché.config(text= "Pétrole")
	A_Marché.config(text= "Charbon")
	B_Marché.config(text= "Acier")
	C_Marché.config(text= "Papier")
	Money = 500
	argentLabel.config(text=Money)
	InvestirScale.config(to=Money)

#Quand on passe aux temps modernes
def RévolutionIndustrielleFini():
	global Acheter1, Acheter2, Acheter3,Acheter4,Acheter5,Acheter6,Acheter7,Acheter8,Bouton1,Bouton2,Bouton3,Bouton4,Bouton5,Bouton6,Bouton7,Bouton8,benefice1,benefice2,benefice3,benefice4,benefice5,benefice6,benefice7,benefice8
	global action, A_action,B_action,C_action,A_x,B_x,C_x,A_y,B_y,C_y,Money,Ben1,Ben2,Ben3,Ben4,Ben5,Ben6,Ben7,Ben8,moderne
	Ben1 = 5
	Ben2 = 20
	Ben3 = 100
	Ben4 = 500 
	Ben5 = 10000
	Ben6 = 1000000
	Ben7 = 10000000
	Ben8 = 0
	benefice1 = False
	benefice2 = False
	benefice3 = False
	benefice4 = False
	benefice5 = False
	benefice6 = False
	benefice7 = False
	benefice8 = False
	Ben1division = 2
	Ben2division = 8
	Ben3division = 25
	Ben4ivision = 167
	Ben5division = 13500
	Ben6division = 166667
	Ben7division = 30000000000
	moderne = True
	Acheter1.config(text="Acheter le kebab du coin pour 1200$"+ ": +" + str(Ben1) + " / tour", state=NORMAL, command= lambda prix=1200, benefice=Ben1:acheter(prix,benefice))
	Acheter2.config(text="Acheter Franprix pour 5000$"+ ": +" + str(Ben2) + " / tour", state=NORMAL,command= lambda prix=5000, benefice=Ben2:acheter(prix,benefice))
	Acheter3.config(text="Acheter Avis Immobilier pour 15000$"+ ": +" + str(Ben3) + " / tour",state=NORMAL, command= lambda prix=15000, benefice=Ben3:acheter(prix,benefice))
	Acheter4.config(text="Acheter LCL pour 100000$"+ ": +" + str(Ben4) + " / tour",state=NORMAL, command= lambda prix=50000, benefice=Ben4:acheter(prix,benefice))
	Acheter5.config(text="Acheter Total pour 8 100 000$"+ ": +" + str(Ben5) + " / tour",state=NORMAL, command= lambda prix=8100000, benefice=Ben5:acheter(prix,benefice))
	Acheter6.config(text="Acheter Apple pour 1 000 000 000$"+ ": +" + str(Ben6) + " / tour", state=NORMAL,command= lambda prix=1000000000, benefice=Ben6:acheter(prix,benefice))
	Acheter7.config(text="Acheter les Etat Unis pour 18 000 000 000 000$"+ ": +" + str(Ben7) + " / tour",state=NORMAL, command= lambda prix=18000000000000, benefice=Ben7:acheter(prix,benefice))
	Acheter8.config(text="Acheter le MONDE pour 102 000 000 000 000$",state=NORMAL,command= lambda prix=102000000000000, benefice= Ben8:acheter(prix,benefice))
	Monnait = "$"
	Monnaient.title(Monnait)
	Entreprise.title("CAC 40")
	x=100
	y=300 
	A_x = x
	B_x = x
	C_x = x
	A_y = y
	B_y = y
	C_y = y
	xmodif = 90
	ymodif = 130
	A_xmodif = 90
	A_ymodif = 130
	B_xmodif = 90
	B_ymodif = 130
	C_xmodif = 90
	C_ymodif = 130
	action = randint(x,y)
	A_action = randint(x,y)
	B_action = randint(x,y)
	C_action = randint(x,y)
	Fenetre.title("Bitcoin")
	Fenetre2.title("Pizza")
	Fenetre3.title("Téléphone")
	Fenetre4.title("Cassettes")
	Marché.config(text= "Bitcoin")
	A_Marché.config(text= "Pizza")
	B_Marché.config(text= "Téléphone")
	C_Marché.config(text= "Cassettes")
	Money = 1000
	argentLabel.config(text=Money)
	InvestirScale.config(to=Money)

# Achats 

def acheter(prix,benefice):
	global Money, Serviteur, Moulin, Villa, Trière, Légion, Grèce, EmpireRomain, AntiquitéFini, Ben1, Ben2, Ben3, Ben4,Ben5,Ben6,Ben7,Ben8,benefice1,benefice2,benefice3,benefice4,benefice5,benefice6,benefice7,benefice8,Antiquité,MoyenAge,Colonisation,RévolutionIndustrielle,TempsModernes
	if Money < prix : 
		return
	Money -= prix
	sonAchat.play()
	argentLabel.config(text=Money)
	InvestirScale.config(to=Money)
	if benefice == Ben1:
		Acheter1.config(state=DISABLED)
		benefice1 = True
	elif benefice == Ben2:
		Acheter2.config(state=DISABLED)
		benefice2 = True
	elif benefice == Ben3:
		Acheter3.config(state=DISABLED)
		benefice3 = True
	elif benefice == Ben4:
		Acheter4.config(state=DISABLED)
		benefice4 = True
	elif benefice == Ben5:
		Acheter5.config(state=DISABLED)
		benefice5 = True
	elif benefice == Ben6:
		Acheter6.config(state=DISABLED)
		benefice6 = True
	elif benefice == Ben7:
		Acheter7.config(state=DISABLED)
		benefice7 = True
	elif benefice == Ben8:
		Acheter8.config(state=DISABLED)
		if Antiquité == True:
			Antiquité = False
			MoyenAge = True
			benefice = 0
			AntiquitéFini()
		elif MoyenAge == True:
			MoyenAge = False
			Colonisation = True
			MoyenAgeFini()
		elif Colonisation == True:
			Colonisation = False
			RévolutionIndustrielle = True
			ColonisationFini()
		elif RévolutionIndustrielle == True:
			RévolutionIndustrielle = False
			TempsModernes = True
			RévolutionIndustrielleFini()
		elif TempsModernes == True:
			TempsModernes = False
			print("fini")



'''
---------------------------- 	 Fonction 1er Marché 	 --------------------------------
'''

def tick():
	global compteur, curtime, Firstsecond, action, Valeur_action, x, y, Money, xmodif, ymodif, Ben1, Ben2, Ben3, Ben4,Ben5,Ben6,Ben7,Ben8,benefice1,benefice2,benefice3,benefice4,Text1,benefice5,benefice6,benefice7,benefice8,division
	global event1,ListeInfo, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, A_action,B_action,C_action,A_actions_joueur,B_actions_joueur,C_actions_joueur
	global MoyenAge, colonisation, industriel,moderne,ListeEvent,Changement,randi
	newtime = time.strftime('%H:%M:%S')
	calculTime = time.strftime('%H%M%S')
	argentLabel.config(text=Money)
	if newtime != curtime:
		curtime = newtime
		clock.config(text=curtime)
		seconde = int(calculTime) - int(startedTime)
		if seconde - Firstsecond != 0:
			argentLabel.config(text=Money)
			InvestirScale.config(to=Money)
			A_InvestirScale.config(to=Money)
			B_InvestirScale.config(to=Money)
			C_InvestirScale.config(to=Money)
			if benefice1 == True:
				Money += Ben1
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben1division
			if benefice2 == True:
				Money += Ben2
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben2division
			if benefice3 == True:
				Money += Ben3
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben3division
			if benefice4 == True:
				Money += Ben4
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben4division
			if benefice5 == True:
				Money += Ben5
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben5division
			if benefice6 == True:
				Money += Ben6
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben6division
			if benefice7 == True:
				Money += Ben7
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
				division = Ben7division
			if benefice8==True:
				Money += 1
				argentLabel.config(text=Money)
				InvestirScale.config(to=Money)
			compteur += 1 
			if compteur%3 == 0:
				z = action
				A_z = A_action
				B_z = B_action
				C_z = C_action
				x = action - xmodif - actions_joueur/division - actions_joueur/division
				y = action + ymodif + actions_joueur/division
				A_x = A_action - A_xmodif - A_actions_joueur/division - A_actions_joueur/division
				A_y = A_action + A_ymodif + A_actions_joueur/division
				B_x = B_action - B_xmodif - B_actions_joueur/division - B_actions_joueur/division
				B_y = B_action + B_ymodif + B_actions_joueur/division
				C_x = C_action - C_xmodif - C_actions_joueur/division - C_actions_joueur/division
				C_y = C_action + C_ymodif + C_actions_joueur/division
				action = round(uniform(x,y))
				A_action = round(uniform(A_x,A_y))
				B_action = round(uniform(B_x,B_y))
				C_action = round(uniform(C_x,C_y))
				if action < 1:
					action = 1
				if A_action < 1:
					A_action = 1
				if B_action < 1:
					B_action = 1
				if C_action < 1:
					C_action = 1
				if action > z or action == z:
					Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")
					Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="limegreen")
				else :
					Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
					Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="crimson")
				if A_action > A_z or A_action == A_z:
					A_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")
					A_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="limegreen")
				else :
					A_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
					A_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="crimson")
				if B_action > B_z or B_action == B_z:
					B_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")
					B_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="limegreen")
				else :
					B_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
					B_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="crimson")
				if C_action > C_z or C_action == C_z:
					C_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")
					C_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="limegreen")
				else :
					C_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
					C_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="crimson")
				calcul_vente = round(actions_joueur*action)
				message_vente = "+"+str(calcul_vente)
				A_calcul_vente = round(A_actions_joueur*A_action)
				A_message_vente = "+"+str(A_calcul_vente)
				B_calcul_vente = round(B_actions_joueur*B_action)
				B_message_vente = "+"+str(B_calcul_vente)
				C_calcul_vente = round(C_actions_joueur*C_action)
				C_message_vente = "+"+str(C_calcul_vente)
				Vente.config(text=message_vente)
				A_Vente.config(text=A_message_vente)
				B_Vente.config(text=B_message_vente)
				C_Vente.config(text=C_message_vente)
				Valeur_action.config(text=action)
				A_Valeur_action.config(text=A_action)
				B_Valeur_action.config(text=B_action)
				C_Valeur_action.config(text=C_action)
			if compteur%4==0:
				if Changement == True:
					Changement = False
					for i in range(16):
						if randi == i :
							if len(ListeEvent[i-1]) < 3:
								if ListeEvent[i-1][0] == Fenetre.title() : 
									action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre2.title() :
									A_action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre3.title() :
									B_action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre4.title() :
									C_action += ListeEvent[i-1][1]
							else :
								if ListeEvent[i-1][0] == Fenetre.title() : 
									action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre2.title() :
									A_action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre3.title() :
									B_action += ListeEvent[i-1][1]
								if ListeEvent[i-1][0] == Fenetre4.title() :
									C_action += ListeEvent[i-1][1]
								if ListeEvent[i-1][2] == Fenetre.title() : 
									action += ListeEvent[i-1][3]
								if ListeEvent[i-1][2] == Fenetre2.title() :
									A_action += ListeEvent[i-1][3]
								if ListeEvent[i-1][2] == Fenetre3.title() :
									B_action += ListeEvent[i-1][3]
								if ListeEvent[i-1][2] == Fenetre4.title() :
									C_action += ListeEvent[i-1][3]
					if action < 1 :
						action = 1
					if A_action < 1 :
						A_action = 1
					if B_action < 1 :
						B_action = 1
					if C_action < 1 :
						C_action = 1
					# modif des variables 
					calcul_vente = round(A_actions_joueur*A_action)
					A_message_vente = "+"+str(calcul_vente)
					A_Vente.config(text=A_message_vente)
					A_Valeur_action.config(text=A_action)
					calcul_vente = round(actions_joueur*action)
					message_vente = "+"+str(calcul_vente)
					Vente.config(text=message_vente)
					Valeur_action.config(text=action)
					calcul_vente = round(B_actions_joueur*B_action)
					B_message_vente = "+"+str(calcul_vente)
					B_Vente.config(text=B_message_vente)
					B_Valeur_action.config(text=B_action)
					calcul_vente = round(C_actions_joueur*C_action)
					C_message_vente = "+"+str(calcul_vente)
					C_Vente.config(text=C_message_vente)
					C_Valeur_action.config(text=C_action)
			if compteur%10==0:
				Changement = True 
				# Choix des bons events de la période
				if MoyenAge == True :
					A_info1 = "Un château du roi Dagobert s'est construit"
					A_info2 = "Un château du roi Dagobert s'est détruit"
					A_info3 = "La bête du Gévaudan est revenue pour se venger"
					A_info4 = "Charlemagne est couronné Empereur"
					A_info5 = "Les Ottomans grattent du territoire"
					A_info6 = "Le Pape souhaite punir les protestants via la confiscation de tous leurs biens"
					A_info7 = "Chute de Constantinople"
					ListeInfo = [A_info1,A_info2,A_info3,A_info4,A_info5,A_info6,A_info7]
					event1 = ["Pierre", -30]
					event2 = ["Pierre", 35]
					event3 = ["Viande", -35]
					event4 = ["Pierre", -20, "Viande", -20, "Bois", -20, "Blé", -20]
					event5 = ["Blé", 45, "Viande", 45]
					event6 = ["Bois", -35, "Pierre", -35]
					event7 = ["Pierre", 50, "Viande", 50, "Bois", 50, "Blé", 50]
					ListeEvent = [event1,event2,event3,event4,event5,event6,event7]
				elif colonisation == True:
					B_info1 = "Découverte de l'Amérique"
					B_info2 = "Naufrage de navires marchands"
					B_info3 = "Des Gorilles se sont échappés du zoo"
					B_info4 = "Importation de bananes"
					B_info5 = "Importation de bananes"
					B_info6 = "Démocratisation du café"
					B_info7 = "Trop de Noirs produisent du cacao"
					B_info8 = "Christophe Colom fait de la pub pour l'Amérique"
					B_info9 = "Boycott de l'Amérique"
					ListeInfo = [B_info1,B_info2,B_info3,B_info4,B_info5,B_info6,B_info7,B_info8,B_info9]
					event1 = ["Esclaves Noirs", -35]
					event2 = ["Esclaves Noirs", 35]
					event3 = ["Bananes", 20]
					event4 = ["Bananes", -25]
					event5 = ["Sucre", -35]
					event6 = ["Cacao", 20, "Sucre", 15]
					event7 = ["Cacao", -25]
					event8 = ["Sucre", 15, "Cacao", 15, "Bananes", 15, "Esclaves Noirs", 15]
					event9 = ["Sucre", -15, "Cacao", -15, "Bananes", -15, "Esclaves Noirs", -15]
					ListeEvent = [event1,event2,event3,event4,event5,event6,event7,event8,event9]
				elif industriel == True:
					C_info1 = "Découverte de l'or Noir"
					C_info2 = "Taxation du pétrole"
					C_info3 = "Utilisation du pétrole dans tous les domaines, histoire de bien polluer"
					C_info4 = "Construction de la tour Eiffel"
					C_info5 = "Arrivé de Karl Marx, sentiment de se faire niquer"
					C_info6 = "Nouvelle réforme mathématiques, impression de nouveaux manuels"
					C_info7 = "Invention des origami"
					C_info8 = "Démocratisation du train à vapeur"
					C_info9 = "Le pétrole, c'est mieux"
					C_info10 = "L'ancêtre de Donald Trump fait une réforme" 
					C_info11 = "Armement militaire"
					C_info12 = "Le Baron Haussmann fait des travaux à Paris"
					C_info13 = "En certain Pasteur trouve le vaccin contre la rage"
					ListeInfo = [C_info1,C_info2,C_info3,C_info4,C_info5,C_info6,C_info7,C_info8,C_info9,C_info10,C_info11,C_info12,C_info13]
					event1 = ["Pétrole", -15]
					event2 = ["Pétrole", -15] 
					event3 = ["Pétrole", 30]
					event4 = ["Acier", 20]
					event5 = ["Acier", -40]
					event6 = ["Papier", 25]
					event7 = ["Papier", -10] 
					event8 = ["Charbon", 25]
					event9 = ["Charbon", -30]
					event10 = ["Pétrole", -20, "Charbon", -30]
					event11 = ["Pétrole", 25, "Acier", 20]
					event12 = ["Acier", 35, "Charbon", 35]
					event13 = ["Papier", (-10*100)/C_actions]
					ListeEvent = [event1,event2,event3,event4,event5,event6,event7,event8,event9,event10,event11,event12,event13]
				elif moderne == True:
					D_info1 = "Aujourd'hui c'est le 16 décembre"
					D_info2 = "On dirai la chute de Empire Romain"
					D_info3 = "Les Italiens ne sont pas qualifiés à la coupe du monde de foot"
					D_info4 = "Sortie de l'IPhone XII"
					D_info5 = "Huawei casse les prix"
					D_info6 = "Apparition des CD"
					D_info7 = "Création d'une association pour grands-mères"
					D_info8 = "Samsung sort un téléphone mangeable"
					D_info9 = "Hacking du réseau international de communication par les Russes"
					D_info10 = "Coupe du monde 2018"
					D_info11 = "Snapchat sort une nouvelle MAJ"
					D_info12 = "Fortnite, PUBG, CS-GO et LOL ont reçu une MAJ"
					D_info13 = "Johnny Hallyday est mort, sentiment de nostalgie"
					D_info14 = "Donald Trump a Twitté"
					D_info15 = "Kim Jong Un mange un Domino’s Pizza"
					D_info16 = "Fornite et PUBG ont maintenant leur version mobile, en cross-play avec les joueurs pc, histoire de bien leur mettre la misère"
					ListeInfo = [D_info1,D_info2,D_info3,D_info4,D_info5,D_info6,D_info7,D_info8,D_info9,D_info10,D_info11,D_info12,D_info13,D_info14,D_info15,D_info16]
					event1 = ["Bitcoin", 50]
					event2 = ["Bitcoin", -50]
					event3 = ["Pizza", -30]
					event4 = ["Téléphone", 30]
					event5 = ["Téléphone", 20]
					event6 = ["Cassette", -30]
					event7 = ["Cassette", 10]
					event8 = ["Pizza", -25, "Téléphone", -15]
					event9 = ["Bitcoin", 40, "Téléphone", 40]
					event10 = ["Pizza", 35]
					event11 = ["Téléphone", -15]
					event12 = ["Téléphone", -25]
					event13 = ["Cassette", 35]
					event14 = ["Téléphone", 55]
					event15 = ["Pizza", -35]
					event16 = ["Téléphone", 35]
					ListeEvent = [event1,event2,event3,event4,event5,event6,event7,event8,event9,event10,event11,event12,event13,event14,event15,event16]
				# Choix de l'event 
				randi = randint(0,len(ListeInfo)-1)
				choix = ListeInfo[randi]
				Text1.config(text=choix)	
	clock.after(200,tick)

def vendre():
	global actions_joueur, Money, Vente, message_vente, action, Valeur_action,sonVente
	Money += round(actions_joueur*action)
	if actions_joueur != 0 :
		sonVente.play()
	actions_joueur = 0
	argentLabel.config(text=Money)
	actionLabel.config(text=actions_joueur)
	InvestirScale.config(to=Money)

def investir():
	global actions_joueur, Money, action
	investissement = InvestirScale.get()
	if investissement != 0:
		sonInvestissement.play()
	Money -= investissement
	action_plus = investissement/action
	actions_joueur += round(action_plus)
	argentLabel.config(text=Money)
	actionLabel.config(text=actions_joueur)
	InvestirScale.config(to=Money)

'''
---------------------------- 	 Fonction 2eme Marché 	 --------------------------------
'''


def A_vendre():
	global A_actions_joueur, Money, A_Vente, A_message_vente, A_action, A_Valeur_action,sonVente
	Money += round(A_actions_joueur*A_action)
	if A_actions_joueur != 0 :
		sonVente.play()
	A_actions_joueur = 0
	argentLabel.config(text=Money)
	A_actionLabel.config(text=A_actions_joueur)
	A_InvestirScale.config(to=Money)

def A_investir():
	global A_actions_joueur, Money, A_action
	A_investissement = A_InvestirScale.get()
	if A_investissement != 0:
		sonInvestissement.play()
	Money -= A_investissement
	action_plus = A_investissement/A_action
	A_actions_joueur += round(action_plus)
	argentLabel.config(text=Money)
	A_actionLabel.config(text=A_actions_joueur)
	A_InvestirScale.config(to=Money)

'''
---------------------------- 	 Fonction 3eme Marché 	 --------------------------------
'''

def B_vendre():
	global B_actions_joueur, Money, B_Vente, B_message_vente, B_action, B_Valeur_action,sonVente
	Money += round(B_actions_joueur*B_action)
	if B_actions_joueur != 0 :
		sonVente.play()
	B_actions_joueur = 0
	argentLabel.config(text=Money)
	B_actionLabel.config(text=B_actions_joueur)
	B_InvestirScale.config(to=Money)

def B_investir():
	global B_actions_joueur, Money, B_action
	B_investissement = B_InvestirScale.get()
	if B_investissement != 0:
		sonInvestissement.play()
	Money -= B_investissement
	action_plus = B_investissement/B_action
	B_actions_joueur += round(action_plus)
	argentLabel.config(text=Money)
	B_actionLabel.config(text=B_actions_joueur)
	B_InvestirScale.config(to=Money)

'''
---------------------------- 	 Fonction 4eme Marché 	 --------------------------------
'''

def C_vendre():
	global C_actions_joueur, Money, C_Vente, C_message_vente, C_action, C_Valeur_action,sonVente
	Money += round(C_actions_joueur*C_action)
	if C_actions_joueur != 0 :
		sonVente.play()
	C_actions_joueur = 0
	argentLabel.config(text=Money)
	C_actionLabel.config(text=C_actions_joueur)
	C_InvestirScale.config(to=Money)

def C_investir():
	global C_actions_joueur, Money, C_action
	C_investissement = C_InvestirScale.get()
	if C_investissement != 0:
		sonInvestissement.play()
	Money -= C_investissement
	action_plus = C_investissement/C_action
	C_actions_joueur += round(action_plus)
	argentLabel.config(text=Money)
	C_actionLabel.config(text=C_actions_joueur)
	C_InvestirScale.config(to=Money)


'''
--------------------------- 	Variables et Widgets 	---------------------------------
'''

# Initialisation
mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
init() #turn all of pygame on.
font = "-family {Utopia} -size 17"
fontTitre = "-family {Utopia} -size 25"
Monnait = " deniers"
division = 2
Money = 10
benefice = 0
Ben1 = 3
Ben2 = 10
Ben3 = 20
Ben4 = 60 
Ben5 = 150
Ben6 = 250
Ben7 = 5000
Ben8 = 0
MoyenAge = False
colonisation = False
industriel = False
moderne = False
Ben1division = 6
Ben2division = 40
Ben3division = 100
Ben4division = 300
Ben5division = 800
Ben6division = 2000
Ben7division = 4800
info1 = "Une statue en marbre a été construite par les Grecs"
info2 = "Découverte de nouvelles mines de marbres" 
info3 = "Tous les loups ont été abattu"
info4 = "Manteau de fourrure pour tous les proches de Jules César"
info5 = "Héphaïstos fait une visite sur Terre"
info6 = "La guerre entraîne la production d'armes en bronze"
info7 = "Tonte massive de mouton"
info8 = "Pénurie de rideau"
info9 = "Chute de l'Empire Romain"
ListeInfo = [info1,info2,info3,info4,info5,info6,info7,info8,info9]
event1 = ["Marbre", 35]
event2 = ["Marbre", -20]
event3 = ["Fourrure", -10]
event4 = ["Fourrure", 25]
event5 = ["Bronze", -25]
event6 = ["Bronze", -40]
event7 = ["Tissu", -15]
event8 = ["Tissu", -20]
event9 = ["Marbre", 50, "Fourrure", 50, "Tissu", 50, "Bronze", 50]
ListeEvent = [event1,event2,event3,event4,event5,event6,event7,event8,event9]
Changement = False
randi = 0
actions_joueur = 0
A_actions_joueur = 0
B_actions_joueur = 0
C_actions_joueur = 0
x = 1
A_x = 1
B_x = 1
C_x = 1
y = 30
A_y = 30
B_y = 30
C_y = 30
xmodif = 15
ymodif = 20
A_xmodif = 15
A_ymodif = 20
B_xmodif = 15
B_ymodif = 20
C_xmodif = 15
C_ymodif = 20
action = randint(x,y)
A_action = randint(x,y)
B_action = randint(x,y)
C_action = randint(x,y)
sonAchat = mixer.Sound("Achat.wav")
sonVente = mixer.Sound("Vente.wav")
sonInvestissement = mixer.Sound("Investissement.wav")
Loop = mixer.Sound("loop.wav")
Loop.play(loops=1000000000, maxtime=0, fade_ms=0)

'''
------------------------------ 		1er Marché 		---------------------------
'''

Fenetre = Tk()
Fenetre.geometry("450x200+900+0")
Monnaient = Tk()
Monnaient.title(Monnait)
Monnaient.geometry("450x170+900+460")
Fenetre.title("Fourrure")


# Canvas et triangles
Canvas1 = Canvas(Fenetre,width=30,  height=30)
Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
Canvas2 = Canvas(Fenetre,width=30,  height=40)
Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")


# Variables simples 

curtime = ''
startedTime = time.strftime('%H%M%S')
Firstsecond = 1
compteur = 0

# calculs 
calcul_vente = round(actions_joueur*action)
message_vente = "+"+str(calcul_vente)

# Labels et scale
InvestirScale = Scale(Fenetre, orient='horizontal', from_=0, to=Money,resolution=10, length=100,sliderrelief="flat", bd = 1)
Marché = Label(Fenetre,text="Fourrure",font=font)
argentLabel = Label(Monnaient,text=Money,font=fontTitre)
actionLabel = Label(Fenetre,text=actions_joueur,font=font)
Valeur_action = Label(Fenetre,text=action,font=font)
Vente = Label(Fenetre,text=message_vente,font=font)
clock = Label()
ModifEvent = Label(Fenetre,text="",font=font)
ModifEvent.grid(column=2,row=4)


# Boutons
Investir = Button(Fenetre,text="Invest",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=investir)
Cut = Button(Fenetre,text="Cut",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=vendre)

# Les .grid()
Canvas2.grid(column=3,row=2)
Canvas1.grid(column=1,row=2,sticky=S)
Marché.grid(column = 2 ,row = 1)
Valeur_action.grid(column=2,row=2)
Investir.grid(column = 1,row = 4)
Cut.grid(column = 3,row = 4)
Vente.grid(column=3,row=5)
InvestirScale.grid(column = 1, row= 5)
actionLabel.grid(column = 6,row=8)



'''
------------------------------ 		2eme Marché 		---------------------------
'''


Fenetre2 = Tk()
Fenetre2.title("Tissu")
Fenetre2.geometry("450x200+900+230")

# Canvas et triangles
A_Canvas1 = Canvas(Fenetre2,width=30,  height=30)
A_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
A_Canvas2 = Canvas(Fenetre2,width=30,  height=40)
A_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")



# calculs 
A_calcul_vente = round(A_actions_joueur*A_action)
A_message_vente = "+"+str(A_calcul_vente)

# Labels et scale
A_InvestirScale = Scale(Fenetre2, orient='horizontal', from_=0, to=Money,resolution=10, length=100,sliderrelief="flat", bd = 1)
A_Marché = Label(Fenetre2,text="Tissu",font=font)
A_actionLabel = Label(Fenetre2,text=A_actions_joueur,font=font)
A_Valeur_action = Label(Fenetre2,text=A_action,font=font)
A_Vente = Label(Fenetre2,text=A_message_vente,font=font)
A_clock = Label()


# Boutons
A_Investir = Button(Fenetre2,text="Invest",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=A_investir)
A_Cut = Button(Fenetre2,text="Cut",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=A_vendre)

# Les .grid()

A_Canvas2.grid(column=3,row=3)
A_Canvas1.grid(column=1,row=3,sticky=S)
A_Marché.grid(column = 2 ,row = 2)
A_Valeur_action.grid(column=2,row=3)
A_Investir.grid(column = 1,row = 5)
A_Cut.grid(column = 3,row = 5)
A_Vente.grid(column=3,row=6)
A_actionLabel.grid(column = 6,row=8)
A_InvestirScale.grid(column = 1, row= 6)




'''
------------------------------ 		3eme Marché 		---------------------------
'''



# Les classiques
Fenetre3 = Tk()
Fenetre3.title("Marbre")
Fenetre3.geometry("450x200+0+430")

# Canvas et triangles
B_Canvas1 = Canvas(Fenetre3,width=30,  height=30)
B_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
B_Canvas2 = Canvas(Fenetre3,width=30,  height=40)
B_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")



# calculs 
B_calcul_vente = round(B_actions_joueur*B_action)
B_message_vente = "+"+str(B_calcul_vente)

# Labels et scale
B_InvestirScale = Scale(Fenetre3, orient='horizontal', from_=0, to=Money,resolution=10, length=100,sliderrelief="flat", bd = 1)
B_Marché = Label(Fenetre3,text="Marbre",font=font)
B_actionLabel = Label(Fenetre3,text=B_actions_joueur,font=font)
B_Valeur_action = Label(Fenetre3,text=B_action,font=font)
B_Vente = Label(Fenetre3,text=B_message_vente,font=font)
B_clock = Label()


# Boutons
B_Investir = Button(Fenetre3,text="Invest",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=B_investir)
B_Cut = Button(Fenetre3,text="Cut",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=B_vendre)

# Les .grid()

B_Canvas2.grid(column=3,row=3)
B_Canvas1.grid(column=1,row=3,sticky=S)
B_Marché.grid(column = 2 ,row = 2)
B_Valeur_action.grid(column=2,row=3)
B_Investir.grid(column = 1,row = 5)
B_Cut.grid(column = 3,row = 5)
B_Vente.grid(column=3,row=6)
B_actionLabel.grid(column = 6,row=8)
B_InvestirScale.grid(column = 1, row= 6)




'''
------------------------------ 		4eme Marché 		---------------------------
'''



Fenetre4 = Tk()
Fenetre4.title("Bronze")
Fenetre4.geometry("450x200+450+430")

# Canvas et triangles
C_Canvas1 = Canvas(Fenetre4,width=30,  height=30)
C_Canvas1.create_polygon((10, 30, 20, 10, 30, 30), fill="grey")
C_Canvas2 = Canvas(Fenetre4,width=30,  height=40)
C_Canvas2.create_polygon((2, 22, 12, 42, 22, 22), fill="grey")

# calculs 
C_calcul_vente = round(C_actions_joueur*C_action)
C_message_vente = "+"+str(C_calcul_vente)

# Labels et scale
C_InvestirScale = Scale(Fenetre4, orient='horizontal', from_=0, to=Money,resolution=10, length=100,sliderrelief="flat", bd = 1)
C_Marché = Label(Fenetre4,text="Bronze",font=font)
C_actionLabel = Label(Fenetre4,text=C_actions_joueur,font=font)
C_Valeur_action = Label(Fenetre4,text=C_action,font=font)
C_Vente = Label(Fenetre4,text=C_message_vente,font=font)
C_clock = Label()


# Boutons
C_Investir = Button(Fenetre4,text="Invest",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=C_investir)
C_Cut = Button(Fenetre4,text="Cut",width=10,font=font,overrelief="groove",relief="flat",borderwidth=4,command=C_vendre)

# Les .grid()

C_Canvas2.grid(column=3,row=3)
C_Canvas1.grid(column=1,row=3,sticky=S)
C_Marché.grid(column = 2 ,row = 2)
C_Valeur_action.grid(column=2,row=3)
C_Investir.grid(column = 1,row = 5)
C_Cut.grid(column = 3,row = 5)
C_Vente.grid(column=3,row=6)
argentLabel.grid(column = 6,row=7)
C_actionLabel.grid(column = 6,row=8)
C_InvestirScale.grid(column = 1, row= 6)


'''
------------------------------ 		Infos et Achats 		---------------------------
'''


Infos = Tk()
Infos.title("Informations")
Infos.geometry("1350x40+0+660")
Text1 = Label(Infos,text="",font=font)
Text1.grid(column=0,row=0)
Entreprise = Tk()
Entreprise.title("Marché")
Entreprise.geometry("900x400+0+0")
benefice1 = False
benefice2 = False
benefice3 = False
benefice4 = False
benefice5 = False
benefice6 = False
benefice7 = False
benefice8 = False
Antiquité = True
MoyenAge = False
Colonisation = False
RévolutionIndustrielle = False
TempsModernes = False

Acheter1 = Button(Entreprise,text="Acheter un Serviteur pour 50 deniers" + ": +" + str(Ben1) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=50,benefice=Ben1: acheter(prix,benefice))
Acheter1.grid(column=0,row=0)

Acheter2 = Button(Entreprise,text="Acheter un Moulin pour 150 deniers"+ ": +" + str(Ben2) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=150,benefice=Ben2: acheter(prix,benefice))
Acheter2.grid(column=0,row=1)

Acheter3 = Button(Entreprise,text="Acheter une Villa pour 1 000 deniers"+ ": +" + str(Ben3) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=1000,benefice=Ben3: acheter(prix,benefice))
Acheter3.grid(column=0,row=2)

Acheter4 = Button(Entreprise,text="Acheter une Trière pour 2 500 deniers"+ ": +" + str(Ben4) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=2500,benefice=Ben4: acheter(prix,benefice))
Acheter4.grid(column=0,row=3)

Acheter5 = Button(Entreprise,text="Acheter une Légion pour 7 500 deniers"+ ": +" + str(Ben5) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=7500,benefice=Ben5: acheter(prix,benefice))
Acheter5.grid(column=0,row=4)

Acheter6 = Button(Entreprise,text="Acheter la Grèce pour 20 000 deniers"+ ": +" + str(Ben6) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=20000,benefice=Ben6: acheter(prix,benefice))
Acheter6.grid(column=0,row=5)

Acheter7 = Button(Entreprise,text="Acheter l'Empire Romain pour 50 000 deniers"+ ": +" + str(Ben7) + " / tour",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=50000,benefice=Ben7: acheter(prix,benefice))
Acheter7.grid(column=0,row=6)

Acheter8 = Button(Entreprise,text="Acheter l'Empire d'Alexandre le Grand pour 120 000 deniers",width=50,font=font,overrelief="groove",relief="flat",borderwidth=4,command= lambda prix=120000,benefice=Ben8: acheter(prix,benefice))
Acheter8.grid(column=0,row=7)


tick()


Fenetre.mainloop()
Entreprise.mainloop()