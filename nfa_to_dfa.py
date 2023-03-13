from typing import Set

class FA:
    def __init__(self, states, alphabet, transitions, accept_states: Set[str], start_state):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = dict(transitions)
        self.accept_states = set(accept_states)
        self.start_state = str(start_state)


def epsilon_closure(nfa: FA, states: Set[str]) -> Set[str]:
    closure = set(states)
    stack = list(states)
    while len(stack) > 0:
        state = stack.pop()
        for next_state in nfa.transitions.get((state, None), []):
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return frozenset(closure)


def nfa_to_dfa(nfa: FA):
    states = []
    state_map = {}
    unmarked_states = []
    alphabet = nfa.alphabet
    transitions = {}

    start_closure = epsilon_closure(nfa, {nfa.start_state})
    unmarked_states.append(start_closure)

    start_state = ','.join(sorted(start_closure)).replace('frozenset', '')
    state_map[start_closure] = start_state
    states.append(start_state)

    while unmarked_states:
        current_states = unmarked_states.pop(0)

        for symbol in alphabet:
            next_states = set()
            for state in current_states:
                next_states |= set(nfa.transitions.get((state, symbol), []))
            next_closure = epsilon_closure(nfa, next_states)

            if next_closure not in state_map:
                state_map[next_closure] = ','.join(sorted(next_closure)).replace('frozenset', '')
                unmarked_states.append(next_closure)
                states.append(state_map[next_closure])

            if state_map[current_states] not in transitions:
                transitions[state_map[current_states]] = {}
            transitions[state_map[current_states]][symbol] = state_map[next_closure]

    dfa = FA(
        states=states,
        alphabet=alphabet,
        transitions=transitions,
        start_state=start_state,
        accept_states=set() # initialize accept_states to an empty set
    )
    for state in states:
        for nfa_accept_state in nfa.accept_states:
            if nfa_accept_state in state:
                dfa.accept_states.add(state)
                break

    return dfa



