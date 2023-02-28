from graphviz import Digraph

def visualize_automaton(states, start_state, accept_states, transitions):
    """Create a Graphviz visualization of the finite automaton."""
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
    for t in transitions:
        dot.edge(t[0], t[2], label=t[1])

    # Render the graph
    dot.render('automaton.gv', view=True)
