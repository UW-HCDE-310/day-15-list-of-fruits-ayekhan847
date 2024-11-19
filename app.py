from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

#Filter fruits to include only those starting with "o" and quantity less than 3
    filtered_fruits = []
    for fruit in fruits:
        if fruit["name"].startswith("o") and fruit["quantity"] <= 3:
            filtered_fruits.append(fruit)
    print(filtered_fruits)
    return render_template("index.html", fruits=filtered_fruits)
