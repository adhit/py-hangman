import re
import os
import hangmandrawer as hangmandrawer

class Hangman:
	secret_word = ""
	mistakes_allowed = 7

	'Game State'
	guessed_word = ""
	wrong_guesses = set([])

	def __init__(self):
		print "------- Initializing Hangman Game -------"
		self.secret_word = raw_input("The secret word: ")

		self.guessed_word = re.sub('[^ ]', '?', self.secret_word)
		self.wrong_guesses = set([])

	def play(self):
		while not self.has_game_finished():
			self.print_game_state()
			guess = raw_input("Your guess (a char): ")
			self.apply_game_state_changes(guess[0])

		os.system('clear')
		print "--------------------------------------------------"
		if self.has_game_lost():
			print "YOU LOST"
		elif self.has_game_won():
			print "YOU WON"
		hangmandrawer.print_hangman(len(self.wrong_guesses))

	def print_game_state(self):
		os.system('clear')
		print "--------------------------------------------------"
		print self.guessed_word
		print "Wrong guesses ({0}): {1}".format(len(self.wrong_guesses), ', '.join(sorted(self.wrong_guesses)))
		hangmandrawer.print_hangman(len(self.wrong_guesses))

	def apply_game_state_changes(self, guess_char):
		valid_guess = False
		new_word = ""
		for i in range(0, len(self.secret_word)):
			if self.secret_word[i] == guess_char:
				new_word = new_word + self.secret_word[i]
				valid_guess = True
			else:
				new_word = new_word + self.guessed_word[i]

		if not valid_guess:
			self.wrong_guesses = self.wrong_guesses.union(guess_char)
		else:
			self.guessed_word = new_word

	def has_game_finished(self):
		return self.has_game_lost() or self.has_game_won()

	def has_game_lost(self):
		return len(self.wrong_guesses) > self.mistakes_allowed

	def has_game_won(self):
		return self.guessed_word == self.secret_word

Hangman().play()
