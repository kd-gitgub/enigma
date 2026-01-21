
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
    



class Reflector:
    def __init__(self, wiring):
        # wiring is a 26-character string mapping A-Z
        self.wiring = wiring

    def encode(self, character):
        # Find the index of the character (A=0, B=1, etc.)
        index = ord(character) - ord('A')
        # Return the character at that position in the wiring
        return self.wiring[index]
    




class Rotor:
    def __init__(self, wiring, notch):
        # wiring is a 26-character string mapping A-Z
        # notch is the position that triggers the next rotor to turn
        self.wiring = wiring
        self.notch = notch
        self.position = 0  # Current rotation position (0-25)

    def encode_right_to_left(self, character):
        # Signal going toward reflector
        index = ord(character) - ord('A')
        # Apply position offset
        index = (index + self.position) % 26
        # Get the encoded character from wiring
        encoded = self.wiring[index]
        # Remove position offset
        result_index = (ord(encoded) - ord('A') - self.position) % 26
        return chr(result_index + ord('A'))

    def encode_left_to_right(self, character):
        # Signal returning from reflector (reverse lookup)
        index = ord(character) - ord('A')
        # Apply position offset
        index = (index + self.position) % 26
        char_to_find = chr(index + ord('A'))
        # Find where this character appears in the wiring
        wiring_index = self.wiring.index(char_to_find)
        # Remove position offset
        result_index = (wiring_index - self.position) % 26
        return chr(result_index + ord('A'))

    def rotate(self):
        self.position = (self.position + 1) % 26

    def at_notch(self):
        return chr(self.position + ord('A')) == self.notch


# Historical rotor wirings
ROTOR_WIRINGS = {
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
    "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
    "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
}


def rotor_from_name(name):
    wiring, notch = ROTOR_WIRINGS[name]
    return Rotor(wiring, notch)


# You will need to write more classes, which can be done here or in separate files, you choose.


if __name__ == "__main__":
    # You can use this section to write tests and demonstrations of your enigma code.
    pass
