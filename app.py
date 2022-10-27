import random
from flask import Flask
app = Flask(__name__)
  

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
  if word.str() and n.isdigit():
    return f'{word}' * int(n)
  else: "Invalid input. Please try again by entering a word and a number!"

@app.route('/dicegame')
def dice_results():
  """6=win, else= lost"""
  result = random.randint(1,6)
  if result == 6:
    return f'You rolled a 6. You WON!'
  else: return f'You lost. You rolled a {result}'

if __name__ == '__main__':
  app.run(debug=True)
