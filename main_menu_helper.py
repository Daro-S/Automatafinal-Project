from minimize_dfa import minimize_dfa
from nfa_to_dfa import nfa_to_dfa
from is_accept_string import is_accepted
from graph import  new_graph
from is_dfa_or_nfa import is_dfa_or_nfa

def test_accept_string(fa):
    while True:
        # Prompt the user to enter a string to test
        input_string = input("Enter a string to test (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if input_string == 'exit':
            break
        
        # Check if the input string is accepted by the FA
        if is_accepted(fa, input_string):
            print("The input string is accepted by the FA.")
        else:
            print("The input string is rejected by the FA.")

def minimize_dfa_wrapper(fa):
    if is_dfa_or_nfa(fa) == "DFA":
        minimized_dfa = minimize_dfa(fa)
        new_graph(minimized_dfa,fa_filename="minimized_FA_graph")
    else:
        print("The given FA is not a DFA.")

def equivalent_dfa_wrapper(fa):
    if is_dfa_or_nfa(fa) == "NFA":
        eqivalent_dfa = nfa_to_dfa(fa)
        new_graph(eqivalent_dfa,fa_filename="equivalent_DFA_graph")
    else:
        print("The given FA is not an NFA.")