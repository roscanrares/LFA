class DFA:
    def __init__(self, sigma, states, transitions, start_state, final_states):
        self.sigma = sigma
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def run(self, string):
        current_state = self.start_state
        for char in string:
            if char not in self.sigma:
                return False
            if (current_state, char) in self.transitions:
                current_state = self.transitions[(current_state, char)]
            else:
                return False
        return current_state in self.final_states