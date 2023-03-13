from is_dfa_or_nfa import is_dfa_or_nfa
from read_input import get_transitions, extract_states_and_alphabet, get_start_and_accept_states, convert_transitions_to_dict
from graph import original_graph
from main_menu_helper import test_accept_string, equivalent_dfa_wrapper, minimize_dfa_wrapper
from FA import FA

if __name__ == '__main__':
    transitions = get_transitions()
    states, alphabet = extract_states_and_alphabet(transitions)
    start_state, accept_states = get_start_and_accept_states()
    transition_dict = convert_transitions_to_dict(transitions)
    fa = FA(states, alphabet, transition_dict, accept_states, start_state)

    # Check if given FA is a DFA
    if is_dfa_or_nfa(fa) == "DFA":
        print("The given FA is a DFA.")
    else:
        print("The given FA is NFA.")

    # Visualize the automaton
    original_graph(fa,fa_filename="FA_graph")
    
    while True:
        print("Select an option:")
        print("1. Test accept string")
        if is_dfa_or_nfa(fa) == "DFA":
            print("2. Minimize DFA")
        elif is_dfa_or_nfa(fa) == "NFA":
            print("3. Find equivalent DFA")
        print("4. Exit")

        option = input("Enter option number: ")

        if option == "1":
            test_accept_string(fa)
        elif option == "2":
            minimize_dfa_wrapper(fa)
        elif option == "3":
            equivalent_dfa_wrapper(fa)
        elif option == "4":
            break
        else:
            print("Invalid option.")
