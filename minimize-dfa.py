from FA import FA

def minimize_dfa(dfa):
    
    # Step 1: Initialize the partition as the accepting and non-accepting states
    partition = [dfa.accepting_states, dfa.states - dfa.accepting_states]
    print(f"Partition 0: {partition}")
    partition_changed = True
    step = 1

    # Step 2: Repeat until the partition no longer changes
    while partition_changed:
        partition_changed = False
        new_partition = []
        for group in partition:
            if len(group) <= 1:
                new_partition.append(group)
                continue
            # Step 2a: Divide each group into subgroups based on transitions
            subgroups = {}
            for state in group:
                transitions = dfa.transitions[state]
                subgroup_key = tuple(transitions.values())
                if subgroup_key not in subgroups:
                    subgroups[subgroup_key] = set()
                subgroups[subgroup_key].add(state)
            # Step 2b: Add the subgroups to the new partition
            for subgroup in subgroups.values():
                new_partition.append(subgroup)
                if len(subgroup) < len(group):
                    partition_changed = True
        prev_partition = partition
        partition = new_partition
        print(f"Partition {step}: {partition}")
        step += 1
        if partition == prev_partition:
            print("Since current and previous partition are the same, we stop.")
            break
    # Step 3: Build the new DFA using the partition as the states
    new_states = []
    new_accepting_states = set()
    new_transitions = {}
    for group in partition:
        new_state = ",".join(sorted(list(group)))
        new_states.append(new_state)
        for state in group:
            if state in dfa.accepting_states:
                new_accepting_states.add(new_state)
            transitions = dfa.transitions[state]
            for symbol, target_state in transitions.items():
                target_group = None
                for subgroup in partition:
                    if target_state in subgroup:
                        target_group = subgroup
                        break
                if target_group is not None:
                    target_state = ",".join(sorted(list(target_group)))
                if new_state not in new_transitions:
                    new_transitions[new_state] = {}
                new_transitions[new_state][symbol] = target_state
    return FA(new_states, dfa.alphabet, new_transitions, new_accepting_states, new_states[0])
