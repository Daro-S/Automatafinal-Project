class FA:
    def __init__(self, states, alphabet, transitions, accept_states: set[str], start_state):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = dict(transitions)
        self.accept_states = set(accept_states)
        self.start_state = str(start_state)
