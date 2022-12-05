#######################################################################
#    Computer Project #10
#    
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
#######################################################################
from cards import Card, Deck

# Options for the user input
MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''
# Creates the board for the user
def initialize():
    deck = Deck()
    deck.shuffle()

    waste = []

    foundation = [[],[],[],[]]

    tableau = [[],[],[],[],[],[],[]]

    for i in range(7):
        for j in range(i,7):
            c=deck.deal()
            tableau[j].append(c)

    for col in tableau:
        for card in col:
            card.flip_card()
        
    for col in tableau:
        col[-1].flip_card()
    c = deck.deal()
    waste.append(c)   
   
    return tableau,deck,foundation, waste
# returns the tableau(7 cards), the user deck, \n
# foundation(consists of 4 cards), and the waste pile

# Displays the board
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
# Prints the user board

# Moves the stock pile to waste
def stock_to_waste( stock, waste ):
    
    if not stock.is_empty():
        waste.append(stock.deal())
        return True
    
    else:
        return False
# Returns True if the move is valid and flase if the move can't be done

# Moves the waste pile to the tableau      
def waste_to_tableau( waste, tableau, t_num ):
    if len(waste) == 0:
        return False
    

    if len(tableau[t_num]) == 0:
        if waste[-1].rank() == 13:
            tableau[t_num].append(waste.pop())
            return True
        else:
            return False

    t_card = tableau[t_num][-1]

    C1S = waste[-1].suit()
    C2S = t_card.suit()


    if waste[-1].rank() + 1  == t_card.rank():
        if C1S == 2:
            if C2S != 2 and C2S != 3:
                tableau[t_num].append(waste.pop())
                return True

        elif C1S == 3:
            if C2S != 3 and C2S != 2:
                tableau[t_num].append(waste.pop())
                return True

        elif C1S == 1:
            if C2S != 1 and C2S != 4:
                tableau[t_num].append(waste.pop())
                return True
        
        elif C1S == 4:
            if C2S != 4 and C2S != 1:
                tableau[t_num].append(waste.pop())
                return True
        else:
            return False
    return False

# Returns true if the move is valid(rank,color,suit) and returns false \n
# if the length of the waste is 0 or if the move \n
# can't be done

# Moves the waste pile to the foundatino pile    
def waste_to_foundation( waste, foundation, f_num ):
    if len(waste) == 0:
        return False

    if len(foundation[f_num]) == 0:
        if waste[-1].rank() == 1:
            foundation[f_num].append(waste.pop())
            return True
        else:
            return False
    
    if waste[-1].suit() == foundation[f_num][-1].suit():
        if waste[-1].rank() - 1 == foundation[f_num][-1].rank():
            foundation[f_num].append(waste.pop())
            return True

    return False

# Returns true if the move is valid(suit) and returns false if \n
# the length of the waste is 0 or the move can't be done

# Moves the tableau pile to the foundation pile    
def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    if len(tableau[t_num]) != 0:
        card = tableau[t_num][-1]
        if len(foundation[f_num]) == 0:
            if card.rank() == 1:
                foundation[f_num].append(tableau[t_num].pop())
                
                if tableau[t_num]:
                    if not tableau[t_num][-1].is_face_up():
                        tableau[t_num][-1].flip_card()
                return True
            else:
                return False
    
        if len(foundation[f_num]) > 0:
            card2 = foundation[f_num][-1]

            if card.rank() == card2.rank() + 1 and card.suit() == card2.suit():
                foundation[f_num].append(tableau[t_num].pop())
                
                if tableau[t_num] and not tableau[t_num][-1].is_face_up():
                    tableau[t_num][-1].flip_card()
                return True
            else:
                return False
    else:
        return False
# Checks for multiple condtions and returns true if the move is \n
# valid(rank,suit). Returns false if the the move is not valid

# Moves the tableau pile to the tableau directory 
def tableau_to_tableau(tableau, t_num1, t_num2 ):
    if len(tableau[t_num1]) != 0:

        if tableau[t_num1] == []:
            return False

        if tableau[t_num2] == []: 
            if tableau[t_num1][-1].rank() == 13:
                tableau[t_num2].append(tableau[t_num1].pop())

                if tableau[t_num1]:
                    if not tableau[t_num1][-1].is_face_up():
                        tableau[t_num1][-1].flip_card()
                return True

        else:
            if tableau[t_num1][-1].rank() + 1 == tableau[t_num2][-1].rank():
                C1S = tableau[t_num1][-1].suit()
                C2S = tableau[t_num2][-1].suit()

                if C1S == 2:
                    if C2S != 2 and C2S != 3:
                        tableau[t_num2].append(tableau[t_num1].pop())
                    else:
                        return False


                elif C1S == 3:
                    if C2S != 3 and C2S != 2:
                        tableau[t_num2].append(tableau[t_num1].pop())
                    else:
                        return False

                elif C1S == 1:
                    if C2S != 1 and C2S != 4:
                        tableau[t_num2].append(tableau[t_num1].pop())
                    else:
                        return False
                elif C1S == 4:
                    if C2S != 4 and C2S != 1:
                        tableau[t_num2].append(tableau[t_num1].pop())
                    else:
                        return False
                if tableau[t_num1]:
                    if not tableau[t_num1][-1].is_face_up():
                        tableau[t_num1][-1].flip_card()
                return True 
    return False

# Makes a series of checks(color,suit,rank) and if they pass, it returns true
# If the move is not valid, it returns false

# Checks if the user has won
def check_win (stock, waste, foundation, tableau):
    if len(stock) == 0 and waste == [] and tableau == [[],[],[],[],[],[],[]]:
        return True
    else:
        return False
# Returns true if the stock, waste, and tableau are empty
# Returns false if not all piles are empty

# Performs error checking and displays what is needed based on user input
def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above

# Returns the parse with the user input and returns None if the input is \n
# invalid
def main():

# initializes the board
    tableau, stock, foundation, waste = initialize() 
    print(MENU)

    while True:
        display(tableau, stock, foundation, waste)
        user_input = input("\nInput an option (TT,TF,WT,WF,SW,R,H,Q): " )
        parse_opt = parse_option(user_input)

        if parse_opt == None:
            continue
        
        if parse_opt[0] == "TT":
            tab = tableau_to_tableau(tableau, parse_opt[1]-1, parse_opt[2]-1)

            if tab == False:
                print("\nInvalid move!\n")
            
            if tab == True:
                win = check_win (stock, waste, foundation, tableau)
                
                if win == True:
                    print("You won!")
                    tableau, stock, foundation, waste = initialize()
                    quit()


        if parse_opt[0] == "TF":
            tab = tableau_to_foundation( tableau, foundation, parse_opt[1]-1,parse_opt[2]-1)

            if tab == False:
                print("\nInvalid move!\n")
            
            if tab == True:
                win = check_win (stock, waste, foundation, tableau)
                
                if win == True:
                    print("You won!")
                    tableau, stock, foundation, waste = initialize()
                    quit() 

        

        if parse_opt[0] == "WT":
            was = waste_to_tableau( waste, tableau, parse_opt[1]-1)

            if was == False:
                print("\nInvalid move!\n")

            if was == True:
                was = check_win (stock, waste, foundation, tableau)
                
                if was == True:
                    print("You won!")
                    tableau, stock, foundation, waste = initialize()
                    quit()

        if parse_opt[0] == "WF":
            was = waste_to_foundation( waste, foundation, parse_opt[1]-1)

            if was == False:
                print("\nInvalid move!\n")

            if was == True:
                was = check_win (stock, waste, foundation, tableau)
                
                if was == True:
                    print("You won!")
                    tableau, stock, foundation, waste = initialize()
                    quit() 
 
        if parse_opt[0] == "SW":
            try:
                stock_to_waste(stock,waste)

            except:
                print("\nInvalid move!\n")


        if parse_opt[0] == "R":
            tableau, stock, foundation, waste = initialize()

            print(MENU)

        if parse_opt[0] == "H":
            print(MENU)

# Quits the game
        if parse_opt[0] == "Q":
            quit()

        
 

if __name__ == '__main__':
     main()
