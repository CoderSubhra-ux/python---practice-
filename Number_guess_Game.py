print("__Hello,--- Welcome to number guess game---\n")
print('Aapko 9 chance milne wale hai agar ap guess na kr paye aapka game over ho jayega.....\n ')
n = 21
number_of_guesses = 1
while (number_of_guesses<=9):
	guess_number = int(input("Enter your number:- "))
	number_of_guesses = number_of_guesses+1
	if (guess_number>100):
		print("Out of range Aapko 100 ke aandar hi jhakna hai\n")
	elif(n<guess_number<30):
		print("Too closely… Thoda kam karein \n")
	elif(guess_number>n):
			print("Aapne bda no. le liya kam karein\n")
	elif(guess_number<n):
			print("Aapne Chota no. le liya thoda bada le\n")
	else:
			bache_hue = 9-number_of_guesses
			print(f"You win! Aapne {number_of_guesses} se game ko jit liya hai")
			print(f"Aapne {bache_hue} chance bacha liye")
			break
if number_of_guesses>9:
					print("Game over, Aapne apne 9 chance gawa diye- Aap haar gye"
