from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)
filePathCSV = "products.csv"
filePathjson = "products.json"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding='utf-8') as i:
            datas = json.load(i)
        return render_template('items.html', items=datas.get("items"))
    except Exception as e:
        print({"error": "{}".format(e)})

@app.route('/products')
def products():
    source = request.args.get("source")
    if not source or source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source")

    id = request.args.get("id")
    products = []
    try:
        if source == "json":
            with open(filePathjson, 'r', encoding='utf-8') as f:
                products = json.load(f)
        elif source == "csv":
            with open(filePathCSV, 'r', encoding='utf-8') as f:
                products = list(csv.DictReader(f))

        if not id:
            return render_template('product_display.html', products=products)

        for product in products:
            if str(product.get("id")) == str(id):
                return render_template('product_display.html', products=[product])

        return render_template('product_display.html', error="Product not found")

    except Exception as e:
        print({"error": "{}".format(e)})
        return render_template('product_display.html', error="Error loading products")
if __name__ == '__main__':
    app.run(debug=True, port=5000)
