def get_transitions():
    """Prompt the user to enter the transition table as a list of tuples."""
    print("Enter the transition table (one transition per line, end with 'done'):")
    transitions = []
    while True:
        line = input().strip()
        if line == 'done':
            break
        parts = line.split(',')
        if len(parts) != 3:
            print("Invalid transition format. Expected: <state>,<symbol>,<state>")
            continue
        transitions.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
    return transitions


def extract_states_and_alphabet(transitions):
    """Extract the set of states and alphabet from the transition table."""
    states = set()
    alphabet = set()
    for state1, symbol, state2 in transitions:
        states.update((state1, state2))
        alphabet.add(symbol)
    return states, alphabet


def get_start_and_accept_states():
    """Read the start and accept states."""
    start_state = input("Enter the start state: ")
    accept_states = set(input("Enter the accept states (comma separated): ").split(","))
    return start_state, accept_states


def convert_transitions_to_dict(transitions):
    """Convert the transition table to a dictionary format."""
    transition_dict = {}
    for state1, symbol, state2 in transitions:
        transition_dict.setdefault((state1, symbol), set()).add(state2)
    return transition_dict