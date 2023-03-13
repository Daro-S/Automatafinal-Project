from FA import FA
def is_accepted(dfa: FA, input_string):
    # Check if the input string is composed only of symbols in the alphabet
    if not all(symbol in dfa.alphabet for symbol in input_string):
        return False

    # Simulate the automaton on the input string
    current_states = {dfa.start_state}
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            # Get the set of all possible next states for this state and symbol
            next_states_for_state = dfa.transitions.get((state, symbol))
            if next_states_for_state is not None:
                next_states |= next_states_for_state
        # Update the set of current states to be the union of all next states
        current_states = next_states
    
    # Check if any of the final states are accept states
    return any(state in dfa.accept_states for state in current_states)