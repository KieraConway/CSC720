from __future__ import print_function
'''

Script Purpose: Homework One - Implement a DFA
Script Version: 1.0 February 10, 2023
Script Author:  Kiera Conway, Student - Dakota State University

'''

''' Script Module Importing '''

# Python Standard Libaries
import sys              # import Python Standard Sys Library
import string           # Special string Module
import getopt

# Python 3rd Party Libraries
from prettytable import PrettyTable

''' End of Script Module Importing '''

''' Constant Initializing '''
# Script Constants
SCRIPT_ASSIGNMENT = "Homework One"
SCRIPT_TITLE = "Implement a DFA"
SCRIPT_VERSION = "Version: 1.0"
SCRIPT_AUTHOR = "Author: Kiera Conway"

''' End Constant Initialization '''

''' Global Initializing '''
# State Settings
states = []                             # list of State class
current_state = 0                       # starts at state 0
test_Input = []                         # list of test input strings

# Alphabet Sets
transition_Alpha_Num = string.ascii_lowercase\
                       + string.digits  # transition used for domains
transition_Ampersand = '@'              # transition for '@'
transition_Period = '.'                 # transition for '.'

# Flags
verbose = False                         # verbose flag
valid_input = True                      # input validation flag

''' End Global Initialization '''

''' Script Functions '''


def usage():
    print_line(95)
    print("\nA regex-free DFA simulation for email addresses\n "
          "ver 1.0, 2023\n "
          "Usage: python 3 dfa_sim.py -h -v\n\n"
          "-h  |  --help \t Display Usage summary \t|   Example: python 3 dfa_sim.py -h\n"
          "-v  |  --verbose \t Set Verbose Mode \t|   Example: python 3 dfa_sim.py -v\t|   Default:", "True" if verbose else "False")
    print_line(95)


def init_states():
    # Create States
    if verbose:
        print("Initializing States...\n")
    for i in range(0, 13):
        states.append(State(i))         # initialize empty States

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


def print_line(length):
    print()
    for i in range(0, length):
        print("-", end='')              # Print Separator
    print("\n")

''' End of Script Functions '''


''' Script Classes '''


class State:
    def __init__(self, number):
        self.number = number        # state number (q0 = 0, q1 = 1, etc)
        self.transitions = {}       # will hold state transitions
        self.accept = False         # whether state is an acceptance state

    def print(self):                                        # prints state information
        print('q' + str(self.number) + ' Transitions:')
        for key, value in self.transitions.items():
            print('{', key, '} : ', value)
        print('Accept State = ', self.accept)
        print('\n')

    def set_properties(self,
                       accept_state=False,
                       **transition_condition):             # Update State Properties

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

    # Print Basic Script Information
    print()
    print(SCRIPT_ASSIGNMENT)
    print(SCRIPT_TITLE)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print_line(25)

    # Create Acceptance table object and define headings
    accept_tbl = PrettyTable(['Input', 'Result'])

    # Parse User Input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vh", ["verbose", "help"])

        #len(sys.argv) sys.argv[1:]
        for opt, arg in opts:
            if opt in ['-v', '--verbose']:
                verbose = True
            elif opt in ['-h', '--help']:
                usage()
                exit()

    except Exception as err:
        print(f'Invalid Input: {err}\n Restoring Default Settings ...\n\n')

    # Initialize States
    init_states()

    # Configure Test Input
    test_Input = ["abc@dsu.edu", "abc@pluto.dsu.edu",
                  "11@123.com", "a.b.ab", "ab@ab",
                  "ab@ab.abcd", "inval@!"]

    if verbose:
        print("Testing Input...")

    for each_String in test_Input:                      # iterate through test strings

        prev_state = -1                                 # to track previous state

        # Create state table object and define headings
        state_tbl = PrettyTable(['Start State', 'Condition', 'End State'])

        for each_Letter in each_String:                 # Iterate through characters

            prev_state = current_state                  # save current state
            try:                                        # move states if transition cond met
                current_state = int([val for key, val
                                     in states[current_state].transitions.items()
                                     if each_Letter in key][0])

            except:                                     # if transition condition no met
                valid_input = False                     # flag invalid input
                current_state = '( X )'
                break                                   # exit loop
                # print('( X )')

            if verbose:
                # Initialize Variables for State Table
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
            input_Accepted = states[current_state].accept   # copy current state's accept state
        else:
            input_Accepted = False                          # set false acceptance if invalid input

        #  Consolidate acceptance into string
        accept_verdict = "Input Accepted" if input_Accepted else "Input Rejected"

        if verbose:

            # Set Acceptance Variables
            accept_string = each_String + ": " + accept_verdict

            # Print Table
            state_tbl.vrules = 0
            result = state_tbl.get_string(title=accept_string)
            print(result)
            print()

        # Add String and Verdict to Acceptance Table
        accept_tbl.add_row([each_String,  accept_verdict])

        # Restart DFA for next String
        current_state = 0

    if verbose:
        print("Compiling Final States...\n")

    # Print Acceptance Table
    accept_tbl.vrules = 0
    accept_tbl.hrules = 1
    result = accept_tbl.get_string()
    print(result)
    print()

    # Complete Script
    print("\n\nScript End")

''' End of Main Script '''