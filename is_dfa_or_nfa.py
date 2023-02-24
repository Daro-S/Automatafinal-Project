# Function to check if the given FA is a DFA
def is_dfa(states, alphabet, transition, start_state, accept_states):
    for state in states:
        for symbol in alphabet:
            if (state, symbol) not in transition:
                return False
    visited = set()
    queue = [start_state]
    while queue:
        current_state = queue.pop(0)
        visited.add(current_state)
        for symbol in alphabet:
            next_state = transition[(current_state, symbol)]
            if next_state not in states:
                return False
            if (current_state, symbol) in transition and next_state not in visited:
                queue.append(next_state)
    return all(state in visited for state in accept_states)

# Main program
if __name__ == '__main__':
    # Input the transaction table as a list of tuples
    print("Enter the transaction table (one transition per line, end with 'done'):")
    transaction = []
    while True:
        line = input().strip()
        if line == 'done':
            break
        parts = line.split(',')
        if len(parts) == 3:
            transaction.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))
        else:
            print("Invalid transaction format. Expected: <state>,<symbol>,<state>")
            continue

    # extract set of states and alphabet from transaction table
    states = set()
    alphabet = set()
    for t in transaction:
        states.add(t[0])
        states.add(t[2])
        alphabet.add(t[1])

    # read start and accept states
    start_state = input("Enter the start state: ")
    accept_states = input("Enter the accept states (comma separated): ").split(",")

    # convert transaction table to dictionary
    transition_dict = {(t[0], t[1]): t[2] for t in transaction}

    # check if given FA is a DFA
    if is_dfa(states, alphabet, transition_dict, start_state, set(accept_states)):
        print("The given FA is a DFA.")
    else:
        print("The given FA is a NFA.")
