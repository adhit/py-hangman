def print_hangman(mistakes):
	if mistakes <=0:
		print ''
	elif mistakes == 1:
		print '''*
*
*
*
*
*
*
*
*
*
*
*
*
*
*'''
	elif mistakes == 2:
		print '''**********
*
*
*
*
*
*
*
*
*
*
*
*
*
*'''
	elif mistakes == 3:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*
*
*
*
*
*
*
*
*
*'''
	elif mistakes == 4:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*           *
*           *
*           *
*           *
*
*
*
*
*
*'''
	elif mistakes == 5:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*         * *
*        *  *
*           *
*           *
*
*
*
*
*
*'''
	elif mistakes == 6:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*         * * *
*        *  *  *
*           *   
*           *
*
*
*
*
*
*'''
	elif mistakes == 7:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*         * * *
*        *  *  *
*           *   
*           *
*          *
*         *
*
*
*
*'''
	else:
		print '''**********
*        *  
*        * * *
*        **   *
*        *****
*         * * *
*        *  *  *
*           *   
*           *
*          * *
*         *   *
*
*
*
*'''