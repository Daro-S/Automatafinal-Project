def is_dfa(states, alphabet, transition, start_state, accept_states):

    # Check if all state-symbol pairs have transitions defined in the transition table

    if not all((state, symbol) in transition for state in states for symbol in alphabet):
        return False
    
      # Perform a breadth-first search to check if all states can be reached from the start state
    # without encountering an empty transition (i.e., the automaton is not an NFA)

    seen = set()
    queue = [start_state]
    while queue:
        current_state = queue.pop(0)
        seen.add(current_state)
        for symbol in alphabet:
            next_state = transition.get((current_state, symbol))
            if next_state is None or next_state not in states:
                return False
            if next_state not in seen:
                queue.append(next_state)
    
    # Check if all accept states were reached during the search

    return all(state in seen for state in accept_states)

def is_accepted(states, alphabet, transition, start_state, accept_states, input_string):
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