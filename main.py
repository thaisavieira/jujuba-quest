import time
import math
import random

classTypes = ['Mage', 'Barbarian', 'Acrher', 'Cleric']
statsNames = ['Attack', 'Speed', 'Defense', 'specialPower', 'Health']
classStats = [[3,5,5,10,100],[10,7,3,3,100],[7,10,5,1,100],[8,8,9,10,100]]
playerName = ''
playerStats = [0,0,0,0,0]
statAdjustment = [0,0,0,0,0]
playerClass = -1
money = 500
playerStatus = 'Alive'
playerLevel = 0
playerExp = 0
currentLocation = 'Home'
placesToTravel = [[],[]]