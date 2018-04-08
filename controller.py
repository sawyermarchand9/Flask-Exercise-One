from flask import Flask, render_template, request
from compute import compute
from model import InputForm

app = Flask(__name__)


@app.route('/hw1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        a = form.a.data
        b = form.b.data
        s = compute(a, b)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
