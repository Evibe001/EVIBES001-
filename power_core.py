import time
import sys

def charge_power():
    print("Initializing E VIBES Power Core...")
    time.sleep(1)

    for i in range(0, 101, 10):
        bar = "█" * (i // 5) + "-" * (20 - (i // 5))
        sys.stdout.write(f"\rCharging: [{bar}] {i}%")
        sys.stdout.flush()
        time.sleep(0.2)

    print("\n\n⚡ POWER FULLY CHARGED! ⚡")
    print("E VIBES is now UNSTOPPABLE.")

if __name__ == "__main__":
    charge_power()
