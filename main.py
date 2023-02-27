from graphviz import Digraph

from is_dfa_or_nfa import is_dfa, is_accepted

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
    transition_dict = {}
    for t in transaction:
        transition_dict.setdefault((t[0], t[1]), set()).add(t[2])

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