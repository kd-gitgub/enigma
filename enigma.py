
class PlugLead:
    def __init__(self, mapping):
        # mapping is a 2-character string like "AB"
        # Store the two connected letters
        self.char1 = mapping[0]
        self.char2 = mapping[1]

    def encode(self, character):
        # If character matches first letter, return second
        if character == self.char1:
            return self.char2
        # If character matches second letter, return first
        elif character == self.char2:
            return self.char1
        # Otherwise return unchanged
        else:
            return character




class Plugboard:
    def __init__(self):
        # Initialize empty list of plug leads
        self.leads = []

    def add(self, lead):
        # Add a PlugLead to the plugboard (max 10 allowed)
        if len(self.leads) >= 10:
            raise ValueError("Plugboard can only have 10 leads")
        self.leads.append(lead)

    def encode(self, character):
        # Pass character through each lead
        for lead in self.leads:
            result = lead.encode(character)
            # If the character was changed, return immediately
            if result != character:
                return result
        # No lead affected this character, return unchanged
        return character
    
# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    pass
