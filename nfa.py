class NFA:
    def __init__(self, allowed_symbols, states, transitions, starting_state, winning_states):
        self.allowed_symbols = allowed_symbols
        self.states = set(states)
        self.transitions = self.convert_transitions(transitions)
        self.starting_state = starting_state
        self.winning_states = set(winning_states)

    def convert_transitions(self, transitions):
        converted_transitions = {}
        for (current_state, symbol), next_state in transitions.items():
            if (current_state, symbol) not in converted_transitions:
                converted_transitions[(current_state, symbol)] = set()
            if isinstance(next_state, str):
                converted_transitions[(current_state, symbol)].add(next_state)
            else:
                converted_transitions[(current_state, symbol)].update(next_state)
        return converted_transitions

    def add_transition(self, current_state, symbol, next_states):
        if (current_state, symbol) not in self.transitions:
            self.transitions[(current_state, symbol)] = set()
        self.transitions[(current_state, symbol)].update(next_states)

    def epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            if (state, '') in self.transitions:
                for next_state in self.transitions[(state, '')]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def find_reachable_states(self, current_states, symbol):
        next_states = set()
        for state in current_states:
            if (state, symbol) in self.transitions:
                next_states.update(self.transitions[(state, symbol)])
        return next_states

    def run(self, symbol_sequence):
        current_states = self.epsilon_closure({self.starting_state})
        for symbol in symbol_sequence:
            next_states = self.find_reachable_states(current_states, symbol)
            if not next_states:
                return False
            current_states = self.epsilon_closure(next_states)
        return any(state in self.winning_states for state in current_states)

