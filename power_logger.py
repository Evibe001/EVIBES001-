import sys
import time

def log(message, type="INFO"):
    colors = {
        "INFO": "\033[94m",    # Blue
        "SUCCESS": "\033[92m", # Green
        "WARNING": "\033[93m", # Yellow
        "ERROR": "\033[91m",   # Red
        "POWER": "\033[95m\033[1m", # Magenta Bold
        "RESET": "\033[0m"
    }
    prefix = f"{colors.get(type, colors['INFO'])}[{type}]{colors['RESET']} "
    for char in f"{prefix}{message}":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        log(sys.argv[2], sys.argv[1])
    elif len(sys.argv) > 1:
        log(sys.argv[1])
