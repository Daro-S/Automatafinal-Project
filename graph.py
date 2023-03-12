import os
from graphviz import Digraph

def visualize_automaton(fa, fa_filename):
    """Visualize the automaton using graphviz."""
    graph = Digraph('Automaton', filename=f'AutomatonGraph/{fa_filename}.gv', format='png')
    for state in fa.states:
        if state in fa.accept_states:
            graph.node(state, shape='doublecircle')
        else:
            graph.node(state)

    graph.edge('', fa.start_state)

    for transition_key, dest_states in fa.transitions.items():
        if isinstance(dest_states, set):
            for dest_state in dest_states:
                graph.edge(transition_key[0], dest_state, label=transition_key[1])
        else:
            graph.edge(transition_key[0], dest_states, label=transition_key[1])

    # Check if the file exists and replace it if it does
    if os.path.exists(f"AutomatonGraph/{fa_filename}.gv.png"):
        os.replace(f"AutomatonGraph/{fa_filename}.gv.png", f"AutomatonGraph/{fa_filename}.gv.png")

    graph.render(view=True)
