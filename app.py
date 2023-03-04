from flask import Flask, render_template, request 
from newfile import convert
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods= ['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        order_arr,num_arr = convert(rawtext)
    return render_template('order.html', order_arr=order_arr,num_arr=num_arr,)

if __name__ == "__main__":
    app.run(debug=True)