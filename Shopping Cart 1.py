Shopping Cart

def main():
	name = raw_input("What's your name? ").lower()
	count_letters(name)


def count_letter(name):

	letter_count = {}

	for l in name: 
		if l in letter_count:
			letter_count[l] += 1
		else:
			letter_count[l] = 1

	return letter_count



if __name__ == '__main__'
	main()





















