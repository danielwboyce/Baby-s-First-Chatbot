from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

babysFirst = ChatBot(name='PyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(babysFirst)
corpus_trainer.train('chatterbot.corpus.english')

print(babysFirst.get_response("hi"))

#this is a test comment for git



app = Flask(__name__)

class Message(FlaskForm):
	userMessage = StringField('message', validators[InputRequired()])
	#chatbotResponse

@app.route('s/', methods=['POST'])
def home():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True)