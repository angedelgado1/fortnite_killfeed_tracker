import re
from rapidfuzz import fuzz
from utils import KILL_FEED_MAPPING, IGNORED_MESSAGES

def parse_kill_feed(kill_feed_text):
    """Processes the extracted kill feed text and returns structured kill data."""
    kills = []

    for line in kill_feed_text:
        line = line.strip()

        # Ignore messages we don't care about (like "knocked" messages)
        if any(ignore in line.lower() for ignore in IGNORED_MESSAGES):
            continue

        # Match standard elimination pattern
        match = re.search(r"(.*?) eliminated (.*?)", line)
        if match:
            killer, victim = match.groups()
            weapon = "Unknown"  # Default if no weapon is specified
            crown_dropped = "👑 Dropped" if "crown" in line.lower() else ""

            # Match elimination type (e.g., "sniped", "introduced to gravity")
            for phrase, mapped_weapon in KILL_FEED_MAPPING.items():
                if fuzz.partial_ratio(phrase.lower(), line.lower()) > 80:
                    weapon = mapped_weapon
                    break

            kills.append({
                "killer": killer,
                "victim": victim,
                "weapon": weapon,
                "crown_dropped": crown_dropped
            })

    return kills

if __name__ == "__main__":
    # Example input to test the parser
    sample_text = [
        "Player1 eliminated Player2 with a shotgun",
        "Player3 eliminated Player4 by studying the typhoon blade",
        "Player5 introduced Player6 to gravity",
        "Player7 sniped Player8"
    ]

    print(parse_kill_feed(sample_text))
