from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)

class Message(FlaskForm):
	userMessage = StringField('message', validators[InputRequired()])
	#chatbotResponse

@app.route(' /', methods=['POST'])
def home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True)