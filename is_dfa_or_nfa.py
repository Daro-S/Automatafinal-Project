
def is_dfa_or_nfa(states, alphabet, transition, start_state, accept_states):
    is_dfa = True

    # Check if every state has at most one transition for each input symbol
    for state in states:
        for symbol in alphabet:
            if len(transition.get((state, symbol), [])) != 1:
                is_dfa = False

    # Check if there is an ε-transition or empty string transition
    for state in states:
        if transition.get((state, 'ε'), []) != []:
            is_dfa = False

    # Check if there are multiple transitions on the same symbol that lead to different states
    for state in states:
        for symbol in alphabet:
            next_states = transition.get((state, symbol), [])
            if len(next_states) > 1 and not is_dfa:
                is_dfa = False

    # Check if the number of transitions equals the number of states times the number of symbols
    num_transitions = sum(len(transition.get((state, symbol), [])) for state in states for symbol in alphabet)
    if num_transitions != len(states) * len(alphabet):
        is_dfa = False

    # Check if each state has the same number of transitions as the number of symbols in the alphabet
    for state in states:
        num_state_transitions = sum(len(transition.get((state, symbol), [])) for symbol in alphabet)
        if num_state_transitions != len(alphabet):
            is_dfa = False

    if is_dfa:
        return "DFA"
    else:
        return "NFA"


def is_accepted(alphabet, transition, start_state, accept_states, input_string):
    # Check if the input string is composed only of symbols in the alphabet
    if not all(symbol in alphabet for symbol in input_string):
        return False

    # Simulate the automaton on the input string
    current_states = {start_state}
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            # Get the set of all possible next states for this state and symbol
            next_states_for_state = transition.get((state, symbol))
            if next_states_for_state is not None:
                next_states |= next_states_for_state
        # Update the set of current states to be the union of all next states
        current_states = next_states
    
    # Check if any of the final states are accept states
    return any(state in accept_states for state in current_states)