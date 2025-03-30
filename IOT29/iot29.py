#!/usr/bin/env python
# PgP 4/10/2024
# used in MIS312 to show how to build program
# by combining program with visual interface
# code generated using chatGPT 3.5
# should make window frame resizable vertically

import subprocess
from breezypythongui import EasyFrame

GET_THROTTLED_CMD = 'vcgencmd get_throttled'
MESSAGES = {
    0: 'Under-voltage!',
    1: 'ARM frequency capped!',
    2: 'Currently throttled!',
    3: 'Soft temperature limit active',
    16: 'Under-voltage has occurred since last reboot.',
    17: 'Throttling has occurred since last reboot.',
    18: 'ARM frequency capped has occurred since last reboot.',
    19: 'Soft temperature limit has occurred'
}

class Logger:
    COLOR_ERROR = '\033[91m'
    COLOR_SUCCESS = '\033[92m'
    COLOR_WARNING = '\033[33m'
    COLOR_RESET = '\033[0m'

    @classmethod
    def error(cls, msg):
        print(cls.COLOR_ERROR + msg + cls.COLOR_RESET)

    @classmethod
    def success(cls, msg):
        print(cls.COLOR_SUCCESS + msg + cls.COLOR_RESET)

    @classmethod
    def warn(cls, msg):
        print(cls.COLOR_WARNING + msg + cls.COLOR_RESET)

def check_throttling_issues():
    """Check for throttling issues since last reboot."""
    Logger.success("Checking for throttling issues since last reboot...")

    throttled_output = subprocess.check_output(GET_THROTTLED_CMD, shell=True)
    throttled_binary = bin(int(throttled_output.split(b'=')[1], 0))

    warnings = []

    for position, message in MESSAGES.items():
        # Check for the binary digits to be "on" for each warning message
        if len(throttled_binary) > position and throttled_binary[0 - position - 1] == '1':
            warnings.append(message)

    return warnings

class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title="CPU Check", width=250, height=300)
         

        # A single label in the first row.
        self.label = self.addLabel(text="Ready to check CPU",
                                   row=0, column=0,
                                   columnspan=2, sticky="NSEW")

        # Two command buttons in the second row.
        self.clearBtn = self.addButton(text="Clear",
                                       row=1, column=0,
                                       command=self.clear)
        self.restoreBtn = self.addButton(text="Check CPU",
                                         row=1, column=1,
                                         command=self.check_cpu)

    # Methods to handle user events.
    def clear(self):
        """Resets the label to the 'Ready to check CPU' string."""
        self.label["text"] = "Ready to check CPU"

    def check_cpu(self):
        """Check CPU throttling issues."""
        warnings = check_throttling_issues()
        if warnings:
            self.label["text"] += "\n" + "\n".join(warnings)
        else:
            self.label["text"] += "\nNo issues found."

def main():
    """Instantiate and pop up the window."""
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()
