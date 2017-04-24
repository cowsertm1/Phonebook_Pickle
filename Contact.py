class Contact:

    def __init__(self, nm, pn, em: str):
        # Initialize a person with their given name, phone number and email address
        self.Name = nm
        self.PhoneNumber = pn
        self.Email = em

    def printToScreen(self):
        """ Prints the person information to the screen """
        formatted = "\t" + self.Name + "\t\t" + self.PhoneNumber + "\t\t" + self.Email
        print(formatted)

    def printToFile(self, fn):
        """ Prints the person information to the given file, fn """
        formatted = self.Name + self.PhoneNumber + "," + self.Email + "\n"
        fn.write(formatted)

    def inFirstName(self, match):
        # Returns true if match is contained in the first name. False otherwise.  Case insensitive """
        if self.Name.lower().find(match.lower()) < 0:
            return False
        else:
            return True

    def inPhoneNumber(self, match):
        """ Returns true if match is contained in the Phone Number.
        False otherwise.  Case insensitive """
        if self.PhoneNumber.lower().find(match.lower()) < 0:
            return False
        else:
            return True

    def inEmail(self, match):
        """ Returns true if match is contained in the email address.
        False otherwise.  Case insensitive """
        if (self.Email.lower().find(match.lower()) < 0):
            return False
        else:
            return True