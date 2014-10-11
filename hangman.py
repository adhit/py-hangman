import re

global_secret_word = "super cali fragilistic expiali docious"
global_mistakes_allowed = 10

def play():
	global global_secret_word
	secret_word = global_secret_word
	guessed_word = re.sub('[^ ]', '?', secret_word)
	wrong_guesses = set([])
	while not has_game_finished(guessed_word, wrong_guesses):
		print "--------------------------------------------------"
		print guessed_word
		print "Wrong guesses ({0}): {1}".format(len(wrong_guesses), ', '.join(sorted(wrong_guesses)))

		guess = raw_input("Your guess (a char): ")
		if guess:
			guess_char = guess[0]
		else:
			guess_char = ''
		if re.match("[a-z]", guess_char) is None:
			print "ERROR: Please input a char!"
			continue

		valid_guess = False
		new_word = ""
		for i in range(0, len(secret_word)):
			if secret_word[i] == guess_char:
				new_word = new_word + secret_word[i]
				valid_guess = True
			else:
				new_word = new_word + guessed_word[i]

		if not valid_guess:
			wrong_guesses = wrong_guesses.union(guess_char)
		else:
			guessed_word = new_word

	if has_game_lost(wrong_guesses):
		print "YOU LOST"
	elif has_game_won(guessed_word):
		print "YOU WON"

def has_game_finished(guessed_word, wrong_guesses):
	return has_game_lost(wrong_guesses) or has_game_won(guessed_word)

def has_game_lost(wrong_guesses):
	global global_mistakes_allowed
	return len(wrong_guesses) > global_mistakes_allowed

def has_game_won(guessed_word):
	global global_secret_word
	return guessed_word == global_secret_word

play()
