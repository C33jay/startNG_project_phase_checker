""" This program helps to know if you'll be doing the start.ng 2020 project.
It calculates all your tasks score and compares it with the cut-off mark """

# global variables
score_gotten_for_user_all_track_task = 0.0
expected_overall_score_for_user_tracks = 0.0


def for_python_track():
	"""Collects the python track task-scores the score"""
	global expected_overall_score_for_user_tracks
	global score_gotten_for_user_all_track_task
	print('\n\t** PYTHON TRACK TASK CALCULATOR **')
	default_python_total = 13.0
	expected_overall_score_for_user_tracks += default_python_total
	while True:
		try:
			py_first_task = input('What is your python first task score (its the area of circle calculator program with a total of 2 points): ')
			py_second_task = input('What is your python second task score (its the user data validation program with a total of 3 points): ')
			py_third_task = input('What is your python third task score (its the number guessing program with a total of 3 points): ')
			py_fourth_task = input('What is your python fourth task score (its the bank system program with a total of 5 points): ')
			user_total_python_score = float(py_first_task) + float(py_second_task) + float(py_third_task) + float(py_fourth_task)
			score_gotten_for_user_all_track_task += user_total_python_score
			print("\n\tYour total python track score is " + str(user_total_python_score))
			
		except ValueError:
			print('\nYou entered a wrong input somewhere. Enter correctly! (You are only entering numbers eg.: 3.2, 4. Do not leave any empty\n')
			continue
		else:
			break
	

def for_general_track():
	"""Collects the general track task-scores"""
	global expected_overall_score_for_user_tracks
	global score_gotten_for_user_all_track_task
	print('\n\t** GENERAL TRACK TASK CALCULATOR **')
	default_general_total = 11.0
	expected_overall_score_for_user_tracks += default_general_total
	while True:
		try:
			first_general_task = input('What is your first general task score (its the first git task with a total of 1 point): ')
			second_general_task = input('What is your second general task score (its the piggyvest testing task with a total of 2 points): ')
			third_general_task = input('What is your third general task score (its that bonus class task with a total of 1 point): ')
			fourth_general_task = input('What is your fourth general task score (its the software testing class task by @ with a total of 2 points): ')
			fifth_general_task = input('What is your fifth general task score (its the kuba bank review with a total of 5 points): ')
			user_total_general_track_score = float(first_general_task) + float(second_general_task) + float(third_general_task) + float(fourth_general_task) + float(fifth_general_task)
			score_gotten_for_user_all_track_task += user_total_general_track_score
			print('\n\tYour total general track score is ' + str(user_total_general_track_score))
		
		except ValueError:
			print('\nYou entered a wrong input somewhere. Enter correctly! (You are only entering numbers eg.: 3.2, 4. Do not leave any empty\n')
			continue
			
		else:
			break
	
	
# Main program
print('\t*** ORACLE BAHOSE PROJECT QUALIFICATION CHECKER !!! ***')

# Collect the tracks user is offering
user_tracks = list(input("Select your tracks\nSelect as eg:12 if you're offering both python and general tracks. Dont put comma between the numbers!!!\nSee the options below:\n\t1 - Python Track\n\t2 - General Track\n\t"))

for user_track in user_tracks:
	if user_track != '1' and user_track != '2':
		print('Wrong Track Choice Entered!')
		exit()

# Check if user selects python track and collect python track tasks scores
if '1' in user_tracks:
	for_python_track()
	
# check if user selects general track and collect general track tasks scores	
if '2' in user_tracks:
	for_general_track()

# Calculate the expected cut-off score
expected_overall_score_for_user_tracks = 0.7 * expected_overall_score_for_user_tracks

# Display user total and total expected scores
print('\nThis is your overall score for all track-task you did: ' + str(score_gotten_for_user_all_track_task))
print('This is the expected overall score for the tracks you are doing: ' + '{:.1f}'.format(expected_overall_score_for_user_tracks))

# Check if user score is less than expected or more to know if user passes or fails
if score_gotten_for_user_all_track_task > expected_overall_score_for_user_tracks:
	print('\nORACLE BAHOSE SAYS: Good job! You will do project')

else:
	print("\nORACLE BAHOSE SAYS: Ella ojukan! No project for you. But you've come a long way nonetheless so keep working hard")