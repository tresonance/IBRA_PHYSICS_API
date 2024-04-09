from math import *
vo = 30 #vitesse initiale en m/s
alpha = 20 #angle alpha en degre
g = 9.81  #intensite pesantur en N/kg

x = 54 # mon joeur se trouve à x = 54m
y_joueur = 1.66 #hauteur du joueur 

aList = []
#for x in range(100):
    #Quand la balle sera à x = 54, 
    y_ball = -0.5*g*x**2/(vo*cos(alpha*pi/180))**2  + x * tan(alpha*pi/180)
#if y_ball >= -0.5:
#    aList.append((x, y_ball)  )
print("y de la ball est %s" % y_ball)
#print(aList)

'''
Problème:
Dans l'animation de la vidéo d'introduction, on a:
vo = 30 m/s #valeur de la vitesse initiale 
alpha = 20° #Angle que fait vecteur vo avec l'horizontal 
g = 9.81 N/kg  #intensite de la pesantur 

1) La balle touche le sol au point d'impact P: 
 a) quel est le temps mis avant d'atteindre P
 b) déterminer la distance de l'origine au point P
 c) quelle est la vitesse de la balle au point P
2) On suppose desormais que le joeur devant le but mesure 1.66m  et est à x = 54m de l'origine O
   En supposant qu'il ne fera aucun mouvement après le 
   depart de la balle du point O, dire si dans ces conditions , le but serait marqué ?
    Est ce que la balle le touchera ?
    autrement dit le but sera t -il. marqué ?
3) Par ailleurs si la balle n'était pas parti du point O
  mais à x0 = 1.32m de celui-ci et à une hauteur y0 = 1m,
  quelle serait la flèche (hautur maximale atteinte) ?
#Bon Courage! 
'''