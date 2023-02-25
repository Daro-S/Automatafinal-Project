from graphviz import Digraph


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


if __name__ == '__main__':
    # Input the transaction table as a list of tuples
    print("Enter the transaction table (one transition per line, end with 'done'):")
    transaction = []
    while True:
        line = input().strip()
        if line == 'done':
            break
        parts = line.split(',')
        if len(parts) != 3:
            print("Invalid transaction format. Expected: <state>,<symbol>,<state>")
            continue
        transaction.append((parts[0].strip(), parts[1].strip(), parts[2].strip()))

    # Extract set of states and alphabet from transaction table
    states = set()
    alphabet = set()
    for t in transaction:
        states.add(t[0])
        states.add(t[2])
        alphabet.add(t[1])

    # Read start and accept states
    start_state = input("Enter the start state: ")
    accept_states = input("Enter the accept states (comma separated): ").split(",")

    # Convert transaction table to dictionary
    transition_dict = {(t[0], t[1]): t[2] for t in transaction}

    # Check if given FA is a DFA
    if is_dfa(states, alphabet, transition_dict, start_state, accept_states):
        print("The given FA is a DFA.")
    else:
        print("The given FA is NFA.")

    # Create the Graphviz visualization
    dot = Digraph()
    dot.attr('node', shape='circle')

    # Add the states to the graph
    for state in states:
        if state == start_state:
            dot.node(state, shape='doublecircle')
        elif state in accept_states:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state)

    # Add the transitions to the graph
    for t in transaction:
        dot.edge(t[0], t[2], label=t[1])

    # Render the graph
    dot.render('automaton.gv', view=True)
