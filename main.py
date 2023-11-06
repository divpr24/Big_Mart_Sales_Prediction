from flask import Flask,render_template,url_for,request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Sales.html')

@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('Sales.html')
    else:
        item_weight = float(request.form['item_weight'])
        
    return render_template('Sales.html', score = item_weight)


if __name__ == "__main__":
    app.run(debug = True)
