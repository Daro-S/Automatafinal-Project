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
             dot.edge('', start_state, arrowhead='vee', style='solid')
        elif state in accept_states:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state)

    # Add the transitions to the graph
    for t in transaction:
        dot.edge(t[0], t[2], label=t[1])

    # Render the graph
    dot.render('automaton.gv', view=True)

    while True:
        # Prompt the user to enter a string to test
        input_string = input("Enter a string to test (or type 'exit' to quit): ")
         # Check if the user wants to exit
        if input_string == 'exit':
            break

        # Check if the input string is accepted by the FA
        if is_accepted(states, alphabet, transition_dict, start_state, accept_states, input_string):
            print("The input string is accepted by the FA.")
        else:
            print("The input string is not accepted by the FA.")


