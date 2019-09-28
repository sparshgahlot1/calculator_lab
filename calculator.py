from multiply import multiply
from divide import divide
from add import add
from subtract import subtract
import sys

if __name__ == '__main__':

	print("1. multiply")
	print("2. divide")
	print("3. subtract")
	print("4. add")
	a=int(sys.argv[1])

	x=int(sys.argv[2])
	y=int(sys.argv[3])
	
	if (a==1) :
		print(multiply(x,y))	
	elif(a==2) :
		print(divide(x,y))	
	elif(a==3) :
		print(subtract(x,y))
	elif(a==4) :
		print(add(x,y))
	else :
		print("ERROR")
