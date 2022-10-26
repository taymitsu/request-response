from flask import Flask 
app = Flask(__name__)

'''
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

if __name__ == '__main__':
  app.run(debug=True)

'''

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
  """Display user input"""
  return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
  return f'How did you know I liked {users_dessert}'


@app.route('/madlibs/<users_adjective>/<users_noun>')
def madlib_game(users_adjective, users_noun):
  """Display user input"""
  return f'That is one {users_adjective} {users_noun}'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
  result = int(number1)*int(number2)
  return f'{number1} times {number2} is {result}'

'''
@app.route('/multiply/<hello>/<world>')
def invalid(hello, world):
  return f'Invalid inputs: {hello}, {world}. Please try again by entering 2 numbers!'
'''

@app.route('/multiply/<hello>/world>')
def invalid(hello, world):
#if hello.str() and world.str()
  return f'Invalid inputs: {hello}, {world}. Please try again by entering 2 numbers!'

@app.route('sayntimes/<word>/<n>')
def sayntimes(word, n):



if __name__ == '__main__':
  app.run(debug=True)
