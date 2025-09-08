from flask import Flask, request, jsonify
app = Flask(__name__)
TASKS = []
@app.get("/")
def home():
    return "Hello from Flask + Docker!"
@app.post("/tasks")
def add_task():
    data = request.get_json(force=True)
    if not data or "title" not in data:
        return jsonify({"error":"title is required"}), 400
    task = {"id": len(TASKS)+1, "title": data["title"]}
    TASKS.append(task)
    return jsonify(task), 201
@app.get("/tasks")
def list_tasks():
    return jsonify(TASKS), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
