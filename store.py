import os
import time
import sys
clear = lambda: os.system('cls')
clear()

def AnotherOne():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global Price
	AO = str(input("Do you want to purchase another item? Y/N "))
	if (AO == "Y" or AO == "y"):
		clear()
		Menu()
	if (AO == "N" or AO == "n"):
		print("\n Thank You Have A Nice Day!")
		time.sleep(3)
		clear()
		sys.exit()
	else:
		print("  Command " + str(AO) + " not recognized... Try Again")
		time.sleep(2)
		clear()
		Store()
		print("Item Code					Item Name					Item Price")
		print("RJP1001						MILO						P8.00")
		print("RJP1002						PANCIT CANTON					P12.00")
		print("RJP1003						PIATTOS						P15.00")
		print("RJP1004						COKE						P10.00")
		print("RJP1005						MONDE SPECIAL MAMON				P20.00" + "\n")
		print("You Current Money is: P" + str(MahMoney) + ".00" + "\n")
		print("Enter Item Code: " + str(IC))
		print("Enter Quantity: " + str(Q))
		print("Total Price " + str(TPrice))
		print("Change: " + str(MahMoney))
		AnotherOne()



def ItemCode():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global Price
	global AO
	IC = str(input("Enter Item Code: "))
	if IC == "RJP1001":
		Price = 8
	elif IC == "RJP1002":
		Price = 12
	elif IC == "RJP1003":
		Price = 15
	elif IC == "RJP1004":
		Price = 10
	elif IC == "RJP1005":
		Price = 20
	else:
		IC = print("  No item code of " + str(IC) + " ...Please Try Again")
		time.sleep(2)
		clear()
		Menu()


def Quantity():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global Price
	global AO
	Q = (input("Enter Quantity: "))
	if Q.isdigit():
		Q = int(str(Q))
	else:
		print("  You must enter a number (i.e. 0,1,2...)")
		time.sleep(2)
		clear()
		Store()
		print("Item Code					Item Name					Item Price")
		print("RJP1001						MILO						P8.00")
		print("RJP1002						PANCIT CANTON					P12.00")
		print("RJP1003						PIATTOS						P15.00")
		print("RJP1004						COKE						P10.00")
		print("RJP1005						MONDE SPECIAL MAMON				P20.00" + "\n")
		print("You Current Money is: P" + str(MahMoney) + ".00" + "\n")
		IC = print("Enter Item Code: " + str(IC))
		Quantity()
		TotalPrice()
		Change()
		AnotherOne()

def TotalPrice():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global Price
	global AO
	TPrice = Price * Q
	if TPrice > MahMoney:
		print("  You dont have enough money to make the purchase")
		time.sleep(2)
		clear()
		Store()
		print("Item Code					Item Name					Item Price")
		print("RJP1001						MILO						P8.00")
		print("RJP1002						PANCIT CANTON					P12.00")
		print("RJP1003						PIATTOS						P15.00")
		print("RJP1004						COKE						P10.00")
		print("RJP1005						MONDE SPECIAL MAMON				P20.00" + "\n")
		print("You Current Money is: P" + str(MahMoney) + ".00" + "\n")
		IC = print("Enter Item Code: " + str(IC))
		Quantity()
		TotalPrice()
		Change()
		AnotherOne()
	else:
		print("Total Price: " + str(TPrice))

			
	

def Change():
	global Q
	global IC
	global MahMoney
	global TPrice
	global C
	global AO
	MahMoney = MahMoney - TPrice
	print("Change: " + str(MahMoney))



def DaMoney():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global AO
	MahMoney = (input("\n\n\nHow much is your Money?: "))
	if MahMoney.isdigit():
		MahMoney = int(str(MahMoney))
		clear()
		Menu()
	else:
		print("  You must enter a number (i.e. 0,1,2...)")
		time.sleep(2)
		clear()
		DaMoney()

	

def Menu():
	global IC
	global Q
	global MahMoney
	global TPrice
	global C
	global AO
	Store()
	print("Item Code					Item Name					Item Price")
	print("RJP1001						MILO						P8.00")
	print("RJP1002						PANCIT CANTON					P12.00")
	print("RJP1003						PIATTOS						P15.00")
	print("RJP1004						COKE						P10.00")
	print("RJP1005						MONDE SPECIAL MAMON				P20.00" + "\n")
	print("You Current Money is: P" + str(MahMoney) + ".00" + "\n")
	
	ItemCode()
	Quantity()
	TotalPrice()
	Change()
	AnotherOne()


def Store():
	print("\n\n")
	print("  _____  ____  ____   ____       _____  ____  ____   ____       _____ ______   ___   ____     ___ ")
	print(" / ___/ /    ||    \ |    |     / ___/ /    ||    \ |    |     / ___/|      | /   \ |    \   /  _]")
	print("(   \_ |  o  ||  D  ) |  |     (   \_ |  o  ||  D  ) |  |     (   \_ |      ||     ||  D  ) /  [_ ")
	print(" \__  ||     ||    /  |  |      \__  ||     ||    /  |  |      \__  ||_|  |_||  O  ||    / |    _]")
	print(" /  \ ||  _  ||    \  |  |      /  \ ||  _  ||    \  |  |      /  \ |  |  |  |     ||    \ |   [_ ")
	print(" \    ||  |  ||  .  \ |  |      \    ||  |  ||  .  \ |  |      \    |  |  |  |     ||  .  \|     |")
	print("  \___||__|__||__|\_||____|      \___||__|__||__|\_||____|      \___|  |__|   \___/ |__|\_||_____|")
	print("\n\n")
                                                                                                                                                         

DaMoney()