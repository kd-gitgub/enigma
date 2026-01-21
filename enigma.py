
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


# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    pass
