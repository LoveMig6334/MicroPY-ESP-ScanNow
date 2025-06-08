class Pin:
    def __init__(self, value=0):
        self.value = value
        self.freq = 80000000  # Default frequency

    def __str__(self):
        return str(self.value)
