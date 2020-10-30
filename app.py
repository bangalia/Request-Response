from flask import Flask

app = Flask(__name__)
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return 'Penguins are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def story(adjective,noun):
    return f'Today I looked out of my window and saw a {adjective} {noun}!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    """Display the result of two numbers entered by user multiplied"""
    answer = number1 * number2
    result = answer.isdigit
    return f'{number1} times {number2} is {result}'   
    
if __name__ == '__main__':
    app.run(debug=True)