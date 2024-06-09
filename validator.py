class Validation:
    def __init__(self, definition_file):
        self.file_path = definition_file
        self.sigma = set()
        self.states = {}
        self.transitions = {}
        self.starting_state = None
        self.final_states = set()

    def run(self):
        current_section = None
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.endswith(':'):
                    current_section = line[:-1].strip()
                    continue
                elif line.lower() == 'end':
                    current_section = None
                    continue
                if current_section:
                    if current_section == 'Sigma':
                        self.get_sigma(line)
                    elif current_section == 'States':
                        self.get_states(line)
                    elif current_section == 'Transitions':
                        self.get_transitions(line)


    def get_sigma(self, line):
        self.sigma.add(line.strip())

    def get_states(self, line):
        state_info = line.split(',')
        state_name = state_info[0].strip()
        modifiers = state_info[1:] if len(state_info) > 1 else []
        is_final = 'F' in modifiers
        is_starting = 'S' in modifiers
        self.states[state_name] = {'final': is_final, 'starting': is_starting}
        if is_final:
            self.final_states.add(state_name)
        if is_starting:
            if self.starting_state is not None:
                print(f"Multiple starting states defined: {self.starting_state} and {state_name}")
            self.starting_state = state_name

    def get_transitions(self, line):
        parts = [part.strip() for part in line.split(',')]
        if len(parts) == 3:
            from_state, symbol, to_state = parts
            self.transitions[(from_state, symbol)] = to_state
        elif len(parts) == 2:
            from_state, to_state = parts
            self.transitions[(from_state)] = to_state


