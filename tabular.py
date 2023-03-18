from tabulate import tabulate
from FA import FA

def tabular(dfa):
    # Build the table headers
    headers = ["State"] + list(dfa.alphabet)

    # Build the table rows
    rows = []
    for state in dfa.states:
        row = [state]
        for symbol in dfa.alphabet:
            target_state = dfa.transitions.get(state, {}).get(symbol, None)
            if target_state is None:
                row.append("Ø")
            else:
                row.append(target_state)
        rows.append(row)

    # Print the table
    print(tabulate(rows, headers=headers, tablefmt="grid"))
   

