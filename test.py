from flask import Flask, render_template, request
from compute import compute
from model import InputForm

app = Flask(__name__)


@app.route('/hw3', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # how do you make it so that the user can enter things freely
        a = form.a.data
        # a = form.a.data
        # b = form.b.data
        # s = compute(a, b)
    else:
        s = None

    return render_template("view.html", form=form, s=s)


if __name__ == '__main__':
    app.run(debug=True)