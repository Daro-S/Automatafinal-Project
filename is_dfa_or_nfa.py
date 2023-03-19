from FA import FA
def is_dfa_or_nfa(fa: FA):
    is_dfa = True
    # Check if every state has at most one transition for each input symbol
    for state in fa.states:
        for symbol in fa.alphabet:
            if len(fa.transitions.get((state, symbol), [])) != 1:
                is_dfa = False

    # Check if there is an ε-transition or empty string transition
    for state in fa.states:
        if fa.transitions.get((state, 'ε'), []) != []:
            is_dfa = False
        if fa.transitions.get((state, 'eps'), []) != []:
            is_dfa = False
        if fa.transitions.get((state, ''), []) != []:
            is_dfa = False

    # Check if there are multiple transitions on the same symbol that lead to different states
    for state in fa.states:
        for symbol in fa.alphabet:
            next_states = fa.transitions.get((state, symbol), [])
            if len(next_states) > 1 and not is_dfa:
                is_dfa = False

    # Check if the number of transitions equals the number of states times the number of symbols
    num_transitions = sum(len(fa.transitions.get((state, symbol), [])) for state in fa.states for symbol in fa.alphabet)
    if num_transitions != len(fa.states) * len(fa.alphabet):
        is_dfa = False

    # Check if each state has the same number of transitions as the number of symbols in the alphabet
    for state in fa.states:
        num_state_transitions = sum(len(fa.transitions.get((state, symbol), [])) for symbol in fa.alphabet)
        if num_state_transitions != len(fa.alphabet):
            is_dfa = False

    if is_dfa:
        return "DFA"
    else:
        return "NFA"


