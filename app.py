from flask import Flask,  render_template, request
from db import insert_msg, display_msg

app = Flask(__name__, template_folder='templates', static_folder="styles")


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        msg = request.form.get('msg')
        print(name, msg)
        insert_msg(name, msg)
        chats = display_msg()
        return render_template('index.html', chats=chats)
    else:
        chats = display_msg()
        print(chats)
        return render_template('index.html', chats=chats)


if __name__ == "__main__":
    app.run(debug=True)
