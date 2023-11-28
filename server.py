from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", )

@app.route('/play/<int:num>')
def multi_box(num):
    return render_template("index2.html", num=num)

@app.route('/play/<int:number>/<color>')
def multi_color(number, color):
    return render_template("index3.html", number=number, color=color)

if __name__=="__main__":
    app.run(debug=True)