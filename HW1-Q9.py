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
import itertools as it

''' Script Functions '''

def init_states():

    # Initialize States
    states.append(State(0))                             # q0
    states[0].transitions[transition_Alpha_Num] = 1

    states.append(State(1))                             # q1
    states[1].transitions[transition_Alpha_Num] = 1
    states[1].transitions[transition_Asperand] = 2

    states.append(State(2))                             # q2
    states[2].transitions[transition_Alpha_Num] = 3

    states.append(State(3))                             # q3
    states[3].transitions[transition_Alpha_Num] = 3
    states[3].transitions[transition_Period] = 4

    states.append(State(4))                             # q4
    states[4].transitions[transition_Alpha_Num] = 5

    states.append(State(5))                             # q5
    states[5].transitions[transition_Alpha_Num] = 6
    states[5].transitions[transition_Period] = 9

    states.append(State(6, True))                       # q6
    states[6].transitions[transition_Alpha_Num] = 7
    states[6].transitions[transition_Period] = 9

    states.append(State(7, True))                       # q7
    states[7].transitions[transition_Alpha_Num] = 8
    states[7].transitions[transition_Period] = 9

    states.append(State(8))                             # q8
    states[8].transitions[transition_Alpha_Num] = 8
    states[8].transitions[transition_Period] = 9

    states.append(State(9))                             # q9
    states[9].transitions[transition_Alpha_Num] = 10

    states.append(State(10))                            # q10
    states[10].transitions[transition_Alpha_Num] = 11

    states.append(State(11, True))                      # q11
    states[11].transitions[transition_Alpha_Num] = 12

    states.append(State(12, True))                      # q12

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




''' Main Script Starts Here '''

if __name__ == '__main__':
    # Alphabet
    transition_Alpha_Num = string.ascii_lowercase + string.digits   # transition used for domains
    transition_Asperand = '@'                                       # transition for '@'
    transition_Period = '.'                                         # transition for '.'

    current_state = 0                   # Starts at state 0
    states = []

    test_Input = ["abc@dsu.edu", "abc@pluto.dsu.edu", "11@123.com", "a.b.ab", "ab@ab", "ab@ab.abcd"]

    init_states()

    ####
    # for each letter in input/test:
    #     compare letter to current states transition
    #     save new current current_state
    #     loop
    # if current state is accept state
    #   string passes
    ####
    valid_input = True
    for each_String in test_Input:
        for each_Letter in each_String:
            print('(', current_state, ')   ------ ', each_Letter, ' ------>   ', end='')
            try:
                current_state = int([val for key, val in states[current_state].transitions.items() if each_Letter in key][0])
                print('(', current_state, ')')

            except:
                valid_input = False
                print('( X )')
                break


        if valid_input:
            input_Accepted = states[current_state].accept
        else:
            input_Accepted = False

        print(each_String, ": ", end='')
        print({True: "Input Accepted", False: "Input Rejected"}[input_Accepted])
        print()

        current_state = 0                  # restart DFA

    print("\n\nScript End")

''' End of Main Script '''