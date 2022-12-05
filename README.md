# Klondike-Solitaire

#    Program that takes in user input to display the necessary \n
#    information based on the input that is given
#
#    The first part of the program is the initialize function that \n
#    creates the board for the user
#
#    The next part is the display function that prints the board 
#    
#    Next is the stock_to_waste function that takes cards from \n
#    the stock and moves them to the waste
#
#    Next is the waste_to_tableau function that makes conditions \n
#    to determine if the waste will be appended to the tableau. \n
#    Also removes the waste once appended
#
#    Following that is the waste_to_foundation function that \n
#    if conditions are met, the waste will be appended to \n
#    the foundation and the removed onced appended 
#    
#
#    Onward is the tableau_to_foundation function that once again \n
#    makes condtions to to move the tableau to foundation and flips \n
#    the cards face up(if not already) 
#
#    Next is the tableau_to_tableau function that checks for \n
#    conditions to  move the tableau to the directory. Also flips \n
#    card face up(if not already) 
#
#    The next function is the check_win function that checks if the \n
#    user has one or not
#
#    The last function is the parse_option function that does error \n
#    checking for the user options and performs what is needed based \n
#    user input
#
#    Next is the main that takes in user input and displays the code \n
#    based on the user input
#    
#    The program will run until the user wins or quits(Option Q)
#
#    The program will also reprompt for user input, display the menu, \n
#    display the board, and the parse
