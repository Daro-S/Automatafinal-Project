
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


