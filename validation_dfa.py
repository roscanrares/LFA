class DFAValidator:
    def __init__(self, validation):
        self.sigma = validation.sigma
        self.states = validation.states
        self.transitions = validation.transitions
        self.starting_state = validation.starting_state
        self.final_states = validation.final_states
        self.validate_dfa()

    def validate_dfa(self):
        if self.starting_state is None:
            raise ValueError("No starting state defined.")
        starting_states = [state for state, attrs in self.states.items() if attrs['starting']]
        if len(starting_states) != 1:
            raise ValueError("Multiple starting states defined")

        for (from_state, symbol), to_state in self.transitions.items():
            if from_state not in self.states:
                raise ValueError("Transition from non-existing state")
            if to_state not in self.states:
                raise ValueError("Transition to non-existing state")

        for (from_state, symbol), to_state in self.transitions.items():
            if symbol not in self.sigma:
                raise ValueError("Transition with non-existing symbol")

        print("Validation successful")
