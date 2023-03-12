# Compute the epsilon closure of a set of states in an NFA
def epsilon_closure(nfa, states):
    # Initialize the closure with the input states
    closure = set(states)
    # Initialize the queue for processing epsilon transitions
    queue = list(states)
    # Process epsilon transitions
    while len(queue) > 0:
        state = queue.pop(0)   
        for next_state in nfa['transitions'].get(state, {}).get(None, []):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    # return tuple(sorted(closure, reverse=True))
    return frozenset(closure)


def nfa_to_dfa(nfa, start_state):
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
        for symbol in nfa['alphabet']:
            alphabet.add(symbol)

            # Compute the next set of states for this symbol
            next_states = set()
            for state in current_states:
                if state in nfa['transitions'] and symbol in nfa['transitions'][state]:
                    next_states |= set(nfa['transitions'][state][symbol])
            next_closure = epsilon_closure(nfa, next_states)

            # Add the next set of states to the unmarked states if it's not already there
            if next_closure not in states and next_closure not in unmarked_states:
                unmarked_states.append(next_closure)

            # Add the transition to the transition table
            if current_states not in transitions:
                transitions[current_states] = {}
            transitions[current_states][symbol] = next_closure

    # Create the new DFA using the state map and transition table
    dfa = {
        'alphabet': alphabet,
        'states': [i for i in range(len(states))],
        'transitions': {},
        'start_state': state_map[start_closure],
        'accept_states': []
    }
    for key, value in transitions.items():
        dfa['transitions'][state_map[key]] = {}
        for symbol, next_state in value.items():
            dfa['transitions'][state_map[key]][symbol] = state_map[next_state]

        # Check if any of the NFA's accept states are in this set of states
        for state in key:
            if state in nfa['accept_states']:
                dfa['accept_states'].append(state_map[key])

    return dfa
def nfa_to_dfa(nfa, start_state):
    # Set up initial variables
    states = []
    state_map = {}
    unmarked_states = []
    alphabet = set()
    transitions = {}

    # Add start state to the unmarked states
    unmarked_states.append([start_state])

    # Process each set of unmarked states until there are no more
    while unmarked_states:
        # Get the next set of unmarked states
        current_states = unmarked_states.pop(0)

        # Add this set of states to the list of states
        state_map[tuple(current_states)] = len(states)
        states.append(current_states)

        # Check each symbol in the alphabet to see where it goes
        for symbol in nfa['alphabet']:
            alphabet.add(symbol)

            # Find the next set of states for this symbol
            next_states = []
            for state in current_states:
                if symbol in nfa['transitions'][state]:
                    next_states.extend(nfa['transitions'][state][symbol])

            # Add the next set of states to the unmarked states if it's not already there
            if next_states not in states and next_states not in unmarked_states:
                unmarked_states.append(next_states)

            # Add the transition to the transition table
            if tuple(current_states) not in transitions:
                transitions[tuple(current_states)] = {}
            transitions[tuple(current_states)][symbol] = next_states

    # Create the new DFA using the state map and transition table
    dfa = {
        'alphabet': alphabet,
        'states': [i for i in range(len(states))],
        'transitions': {},
        'start_state': 0,
        'accept_states': []
    }
    for key, value in transitions.items():
        dfa['transitions'][state_map[key]] = {}
        for symbol, next_state in value.items():
            dfa['transitions'][state_map[key]][symbol] = state_map[tuple(next_state)]

        # Check if any of the NFA's accept states are in this set of states
        for state in key:
            if state in nfa['accept_states']:
                dfa['accept_states'].append(state_map[key])

    return dfa
nfa = {
    'alphabet': {'0', '1'},
    'states': {0, 1, 2},
    'transitions': {
        0: {'0': {0}},
        0: {'1': {1}},
        1: {'1': {1}},
        2: {}
    },
    'accept_states': {0, 1}
}

dfa = nfa_to_dfa(nfa, 0)
print(dfa)

