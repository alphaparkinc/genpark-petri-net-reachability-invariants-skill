class PetriNet:
    """
    Petri Net Discrete Event System.
    Analyzes place markings, transition firing semantics, and state space reachability.
    """
    def __init__(self, places, transitions):
        self.places = places
        self.transitions = transitions

    def is_enabled(self, marking, t_name):
        inputs, _ = self.transitions[t_name]
        for p, count in inputs.items():
            if marking.get(p, 0) < count:
                return False
        return True

    def fire(self, marking, t_name):
        if not self.is_enabled(marking, t_name):
            return None
        inputs, outputs = self.transitions[t_name]
        new_marking = dict(marking)
        for p, count in inputs.items():
            new_marking[p] -= count
        for p, count in outputs.items():
            new_marking[p] = new_marking.get(p, 0) + count
        return new_marking

    def reachable_markings(self, max_depth=10):
        init = tuple(sorted(self.places.items()))
        visited = {init}
        queue = [dict(self.places)]

        while queue:
            curr = queue.pop(0)
            for t in self.transitions:
                nxt = self.fire(curr, t)
                if nxt is not None:
                    nxt_tuple = tuple(sorted(nxt.items()))
                    if nxt_tuple not in visited:
                        visited.add(nxt_tuple)
                        queue.append(nxt)
        return len(visited)
