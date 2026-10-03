from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "HEAD"])
def health():
    return jsonify(status="ok"), 200


@app.route("/receiveUpdate", methods=["GET", "HEAD", "POST"])
def receive_update():
    if request.method == "POST":
        print("=== RUBIKA UPDATE ===")
        print(request.get_json(silent=True))

    return jsonify(status="ok"), 200


@app.route("/receiveInlineMessage", methods=["GET", "HEAD", "POST"])
def receive_inline():
    if request.method == "POST":
        print("=== RUBIKA INLINE ===")
        print(request.get_json(silent=True))

    return jsonify(status="ok"), 200
