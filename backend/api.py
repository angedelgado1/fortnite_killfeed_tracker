from flask import Flask, request, jsonify
from ocr import extract_kill_feed_text
from parser import parse_kill_feed
from datetime import datetime, timedelta

app = Flask(__name__)
kill_feed_data = []
seen_kills = set()
EXPIRATION_TIME = timedelta(seconds=10)

def generate_kill_id(kill):
    """Creates a unique ID for each kill to prevent duplicates."""
    return f"{kill['killer']}-{kill['victim']}-{kill['weapon']}"

@app.route("/kills", methods=["GET"])
def get_kill_feed():
    """Fetch live kill feed."""
    global kill_feed_data, seen_kills

    kill_feed_text = extract_kill_feed_text()
    new_kills = parse_kill_feed(kill_feed_text)

    current_time = datetime.now()
    seen_kills = {k for k in seen_kills if k[1] > current_time - EXPIRATION_TIME}

    for kill in new_kills:
        kill_id = generate_kill_id(kill)
        if kill_id not in {k[0] for k in seen_kills}:
            kill["timestamp"] = current_time.strftime("%H:%M:%S")
            kill_feed_data.append(kill)
            seen_kills.add((kill_id, current_time))

    return jsonify(kill_feed_data)

@app.route("/clear", methods=["POST"])
def clear_kill_feed():
    """Manually clears the kill feed for a new match."""
    global kill_feed_data, seen_kills
    kill_feed_data = []
    seen_kills = set()
    return jsonify({"message": "Kill feed cleared"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
