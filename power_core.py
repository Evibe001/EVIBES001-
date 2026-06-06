import time
import sys

# Use local power_logger if available
try:
    from power_logger import log
except ImportError:
    def log(msg, type="INFO"):
        print(f"[{type}] {msg}")

def charge_power():
    log("Initializing E VIBES Power Core...", "INFO")
    time.sleep(1)

    for i in range(0, 101, 10):
        bar = "█" * (i // 5) + "-" * (20 - (i // 5))
        sys.stdout.write(f"\rCharging: [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.2)

    print("\n")
    log("POWER FULLY CHARGED!", "SUCCESS")
    log("E VIBES IS NOW UNSTOPPABLE.", "POWER")

if __name__ == "__main__":
    charge_power()
