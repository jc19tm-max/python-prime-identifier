print("Welcome to Prime Identifier")

user_input = input('What is the Number you are trying to identify as a prime or not (Please input only 1 number)? ')

clean1_user_input = user_input.replace(",","")
clean2_user_input = clean1_user_input.replace(" ", "")

try:
	number = float(clean2_user_input)
	
	if number == 0:
		print("Please input a Non-Zero Number")
		
	elif number<1 and number%1==0:
		print("Please input a Positive Number")
		
	elif number==1:
		print("The Number 1 is not a Prime Number because its only divisible by itself, it is known as a Multiplicative Identity")
		
	elif number % 1 == 0:
		divisible_by = 1
		divisible_by_list =[]
		while divisible_by < (number+1):
			a= number/divisible_by
			
			if a%1==0: divisible_by_list.append(divisible_by)
			
			divisible_by += 1
		
		if len(divisible_by_list)==2:
			status=" is a Prime Number because it is divisible by "
		else:
			status= " is a Composite Number because it is divisible by "
			
		b=str(len(divisible_by_list))
		
		c = f"{', '.join(str(x) for x in divisible_by_list[:-1])}, and {divisible_by_list[-1]}"

		formated_output= "The Number "+str(clean2_user_input) + status + b + " numbers" + ", they are "+c
		
		print(formated_output)
		
	else:
		print("Please input a Whole Number")
		
except:
	print("Please input a valid number")