from is_dfa_or_nfa import is_dfa_or_nfa, is_accepted
from read_input import get_transitions, extract_states_and_alphabet, get_start_and_accept_states, convert_transitions_to_dict
from graph import visualize_automaton

if __name__ == '__main__':
    transitions = get_transitions()
    states, alphabet = extract_states_and_alphabet(transitions)
    start_state, accept_states = get_start_and_accept_states()
    transition_dict = convert_transitions_to_dict(transitions)

    # Check if given FA is a DFA
    if is_dfa_or_nfa(states, alphabet, transition_dict, start_state, accept_states) == "DFA":
        print("The given FA is a DFA.")
    else:
        print("The given FA is NFA.")

    # Visualize the automaton
    visualize_automaton(states, start_state, accept_states, transitions)

    while True:
        # Prompt the user to enter a string to test
        input_string = input("Enter a string to test (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if input_string == 'exit':
            break

        # Check if the input string is accepted by the FA
        if is_accepted(alphabet, transition_dict, start_state, accept_states, input_string):
            print("The input string is accepted by the FA.")
        else:
            print("The input string is rejected by the FA.")
