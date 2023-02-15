from __future__ import print_function

'''

Script Purpose: Homework One - Implement an FA
Script Version: 1.0 February 10, 2023
Script Author:  Kiera Conway, Student - Dakota State University

'''

''' Script Module Importing '''
# Python Standard Libaries
import sys          # import Python Standard Sys Library
import string                       # Special string Module


''' Script Functions '''

def init_states():
    # Initialize States
    states.append(State(0))
    states[0].transitions[transition_Alpha_Num] = 1

    states.append(State(1))
    states[1].transitions[transition_Alpha_Num] = 1
    states[1].transitions[transition_Asperand] = 2

    states.append(State(2))
    states[2].transitions[transition_Alpha_Num] = 3

    states.append(State(3, True))
    states[3].transitions[transition_Alpha_Num] = 3
    states[3].transitions[transition_Period] = 4

    states.append(State(4))

    # for each in states:
    #     states[each.number].print()


''' End of Script Functions '''

''' Script Classes '''


class State():
    def __init__(self, number, accept_state=False):
        self.number = number
        self.transitions = {}
        self.accept = accept_state

    def add_transition(self, input, new_state):
        self.transitions[input] = new_state

    def print(self):
        print('q'+ str(self.number) + ' Transitions:')
        for key, value in self.transitions.items():
            print('{', key, '} : ', value)
        print('Accept State = ', self.accept)
        print('\n')


''' End of Script Classes '''
def read_state(input, current_state):
    print()



''' Main Script Starts Here '''

if __name__ == '__main__':
    # Alphabet
    transition_Alpha_Num = string.ascii_lowercase + string.digits   # transition used for domains
    transition_Asperand = '@'                                       # transition for '@'
    transition_Period = '.'                                         # transition for '.'

    current_state = 0                   # Starts at state 0
    states = []

    test = "tst@dsu.edu"                        #todo: remove me

    init_states()

    ####
    # https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
    # https://www.geeksforgeeks.org/python-substring-key-match-in-dictionary/
    # for each letter in input/test:
    #     compare letter to current states transition
    #     save new current current_state
    #     loop
    # if current state is accept state
    #   string passes
    ####
    print()
    for each in test:
        # if each in states[current_state].transitions.keys():
        #     print("found!")
        print(current_state, ' : ', each, '---->', end='')
        #current_state = [val for key, val in states[current_state].transitions.items() if each in key]
        #
        # TODO: above finds the value, and returns the new state correctly. However, it returns as a list and I need an int
        #

        print(current_state)



    print("\n\nScript End")


''' End of Main Script '''