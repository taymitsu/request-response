from flask import Flask
#import Flask library 
app = Flask(__name__)
#app variable to start writing routes  - instances for app server 

'''
@app.route('/')
def homepage(): #route function, shows in browser 
  """Display greeting""" #optional
  return 'Are you there, World? It\'s me, Ducky!' #return page content
'''

@app.route('/animal/<users_animal>') #<route variable>
def favorite_animal(users_animal): #route function
  """Display message to user"""
  return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(user_dessert):
  return f'How did you know I liked donuts?'

app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):

  return f'That {noun} is really {adjective}'

if __name__ == '__main__':
  app.run(debug=True, port=3000) 