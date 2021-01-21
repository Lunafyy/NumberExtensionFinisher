class NumberExtensionFinisher(object):
    def __init__(self, number):
        self.number = number
        self.extensions = ["st", "nd", "rd", "th"]
        
        finished = self.finisher()

        print(finished)

        quit()

    def finisher(self):
        endingNumber = int(self.number[-1])
        try:
            ext = self.extensions[endingNumber-1]
        except:
            ext = "th"
        return str(endingNumber) + ext


if __name__ == "__main__":
    NumberExtensionFinisher(input("Number: "))