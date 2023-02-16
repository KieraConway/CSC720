from __future__ import print_function

'''

Script Purpose: Homework One - Implement an FA
Script Version: 1.0 February 10, 2023
Script Author:  Kiera Conway, Student - Dakota State University

'''

''' Script Module Importing '''
# Python Standard Libaries
import sys              # import Python Standard Sys Library
import string           # Special string Module
import getopt
from prettytable import PrettyTable

# State Settings
states = []
current_state = 0  # Starts at state 0
test_Input = []

# Alphabet Sets
transition_Alpha_Num = string.ascii_lowercase + string.digits  # transition used for domains
transition_Ampersand = '@'  # transition for '@'
transition_Period = '.'     # transition for '.'

# Alphabet Sets
verbose = False              # verbose

''' Script Functions '''


def print_help():
    print("-h help"
          "-v verbose")

def init_states():
    # Create States
    if verbose:
        print("Initializing States...")
    for i in range(0, 13):
        states.append(State(i))

    # Set State Values
    if verbose:
        print("Setting State Properties...\n")
    states[0].set_properties(**{transition_Alpha_Num: 1})       # q0

    states[1].set_properties(**{transition_Alpha_Num: 1},
                             **{transition_Ampersand: 2})       # q1

    states[2].set_properties(**{transition_Alpha_Num: 3})       # q2

    states[3].set_properties(**{transition_Alpha_Num: 3},
                             **{transition_Period: 4})          # q3

    states[4].set_properties(**{transition_Alpha_Num: 5})       # q4

    states[5].set_properties(**{transition_Alpha_Num: 6},
                             **{transition_Period: 9})          # q5

    states[6].set_properties(True,
                             **{transition_Alpha_Num: 7},
                             **{transition_Period: 9})          # q6

    states[7].set_properties(True,
                             **{transition_Alpha_Num: 8},
                             **{transition_Period: 9})          # q7

    states[8].set_properties(**{transition_Alpha_Num: 8},
                             **{transition_Period: 9})          # q8

    states[9].set_properties(**{transition_Alpha_Num: 10})      # q9

    states[10].set_properties(**{transition_Alpha_Num: 11})     # q10

    states[11].set_properties(True,
                              **{transition_Alpha_Num: 12})     # q11

    states[12].set_properties(True)                             # q12


''' End of Script Functions '''


''' Script Classes '''


class State:
    def __init__(self, number):
        self.number = number
        self.transitions = {}
        self.accept = False

    def add_transition(self, input_condition, new_state):
        self.transitions[input_condition] = new_state

    def print(self):
        print('q' + str(self.number) + ' Transitions:')
        for key, value in self.transitions.items():
            print('{', key, '} : ', value)
        print('Accept State = ', self.accept)
        print('\n')

    '''
    '
    'transition_condition = {Condition: New State}
    '
    '''

    def set_properties(self, accept_state=False, **transition_condition):

        # Set Acceptance State
        self.accept = accept_state

        # Set Transitions
        for key, value in transition_condition.items():
            try:
                self.transitions[key] = value
            except Exception as err:
                print(f'Error: Invalid Transition Condition for State {self.number} <{err}>')
                quit()


''' End of Script Classes '''

''' Main Script Starts Here '''

if __name__ == '__main__':


    accept_tbl = PrettyTable(['Input', 'Result'])

    # Parse User Input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vt:", ["verbose =", "test ="])

        #len(sys.argv) sys.argv[1:]
        for opt, arg in opts:
            if opt in ['-v', '--verbose']:
                verbose = True
            # if opt in ['-t', '--test']:
            #     test_Input = arg

    except Exception as err:
        print(f'Invalid Input: {err}\n Restoring Default Settings ...')

    # Initialize States
    init_states()

    # Configure Test Input
    test_Input = ["abc@dsu.edu", "abc@pluto.dsu.edu", "11@123.com", "a.b.ab", "ab@ab", "ab@ab.abcd"]
    # if len(test_Input) == 0:
    #     test_Input = ["abc@dsu.edu", "abc@pluto.dsu.edu", "11@123.com", "a.b.ab", "ab@ab", "ab@ab.abcd"]


    ####
    #     compare letter to current states transition
    #     save new current current_state
    #     loop
    # if current state is accept state
    #   string passes
    ####
    if verbose:
        print("Testing Input...")

    valid_input = True                                  # Flag for input validation
    for each_String in test_Input:                      # Iterate through Test Strings

        prev_state = -1                                 # to track previous state

        # Create a tbl object and define headings
        state_tbl = PrettyTable(['Start State', 'Condition', 'End State'])

        for each_Letter in each_String:                 # Iterate through characters

            prev_state = current_state                  # save current state
            try:                                        # move states
                current_state = int([val for key, val in states[current_state].transitions.items() if each_Letter in key][0])

            except:                                     # if state is invalid
                valid_input = False                     # Flag invalid input
                current_state = '( X )'
                break                                   # Exit loop
                # print('( X )')

            if verbose:
                start_s = ''
                cond = '----- ' + each_Letter + ' ----->'
                end_s = ''

                try:
                    # Format and Save Start State
                    if states[prev_state].accept:
                        start_s = '(( ' + str(prev_state) + ' ))'
                    else:
                        start_s = '( ' + str(prev_state) + ' )'

                    # Format and Save End State
                    if states[current_state].accept:
                        end_s = '(( ' + str(current_state) + ' ))'
                    else:
                        end_s = '( ' + str(current_state) + ' )'

                    # Add information to State Table
                    state_tbl.add_row([start_s, cond, end_s])

                except Exception as err:
                    print(f'Error: Table Creation Unsuccessful <{err}>')

        # Check Input Validity Flag
        if valid_input:
            input_Accepted = states[current_state].accept
        else:
            input_Accepted = False

        if verbose:

            # Set Acceptance Variables
            accept_verdict = "Input Accepted" if input_Accepted else "Input Rejected"
            accept_string = each_String + ": " + accept_verdict

            # Print Table
            state_tbl.vrules = 0
            result = state_tbl.get_string(title=accept_string)
            print(result)
            print()

            # Print Acceptance
            # print(each_String, ": ", end='')
            # print({True: "Input Accepted", False: "Input Rejected"}[input_Accepted])
            # print()

        # Add information to Accept Table
        accept_tbl.add_row([each_String,  accept_verdict])

        current_state = 0  # restart DFA

    if verbose:
        print("Compiling Final States...\n")

    # Print Table
    accept_tbl.vrules = 0
    accept_tbl.hrules = 1
    result = accept_tbl.get_string()
    print(result)
    print()

    print("\n\nScript End")

''' End of Main Script '''