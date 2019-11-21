# Packages for chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# Packages for Flask
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
	user_message = StringField('Message', validators=[DataRequired()])
	submit = SubmitField('Send')


messages_array = []

babysFirst = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(babysFirst)
corpus_trainer.train('chatterbot.corpus.english')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-will-be-longer-probably'

@app.route('/', methods=['GET', 'POST'])
def home():
	form = MessageForm()
	if form.validate_on_submit():
		messages_array.append(form.user_message.data)
		messages_array.append(babysFirst.get_response(form.user_message.data))
		print(messages_array)
	return render_template("template.html", messages_array=messages_array, form=form)


if __name__ == "__main__":
	app.run(debug=True)