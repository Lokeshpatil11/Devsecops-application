from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB = "recipes.db"

def get_db():
    return sqlite3.connect(DB)

@app.route("/")
def health():
    return {"status": "Recipe App Running"}

@app.route("/recipes")
def recipes():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM recipes")
    data = cursor.fetchall()
    conn.close()

    return jsonify([r[0] for r in data])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
