from FA import FA
def nfa_to_dfa(nfa: FA, start_state: str) -> FA:
    # Set up initial variables
    states = []
    state_map = {}
    unmarked_states = []
    alphabet = set()
    transitions = {}

    # Compute the epsilon closure of the start state
    start_closure = epsilon_closure(nfa, {start_state})
    unmarked_states.append(start_closure)

    # Process each set of unmarked states until there are no more
    while unmarked_states:
        # Get the next set of unmarked states
        current_states = unmarked_states.pop(0)

        # Add this set of states to the list of states
        state_map[current_states] = len(states)
        states.append(current_states)

        # Check each symbol in the alphabet to see where it goes
        for symbol in nfa.alphabet:
            alphabet.add(symbol)

            # Compute the next set of states for this symbol
            next_states = set()
            for state in current_states:
                if state in nfa.transitions and symbol in nfa.transitions[state]:
                    next_states |= set(nfa.transitions[state][symbol])
            next_closure = epsilon_closure(nfa, next_states)

            # Add the next set of states to the unmarked states if it's not already there
            if next_closure not in states and next_closure not in unmarked_states:
                unmarked_states.append(next_closure)

            # Add the transition to the transition table
            if current_states not in transitions:
                transitions[current_states] = {}
            transitions[current_states][symbol] = next_closure

    # Create the new DFA using the state map and transition table
    dfa = FA(
        states=[i for i in range(len(states))],
        alphabet=alphabet,
        transitions={},
        start_state=str(state_map[start_closure]),
        accept_states=[]
    )
    for key, value in transitions.items():
        dfa.transitions[str(state_map[key])] = {}
        for symbol, next_state in value.items():
            dfa.transitions[str(state_map[key])][symbol] = str(state_map[next_state])

        # Check if any of the NFA's accept states are in this set of states
        for state in key:
            if state in nfa.accept_states:
                dfa.accept_states.append(str(state_map[key]))

    return dfa
