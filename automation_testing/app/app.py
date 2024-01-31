from flask import Flask, jsonify


"""a new variable with name app is created and __name__ 
assigns a special unique location in memory to it"""
app = Flask(__name__)


# define endpoint or route to the app
# e.g Https://www.gibberish.com/
@app.route('/')
def home():

    """dictionary cannot work but strings.
    so I have to convert my dict to str.
    for this reason I use jsonify"""
    return jsonify({'message': 'Hello, world'})


"""what is happening over here is __main__ checks the location 
of __name__ and call it specifically. if it was to call some 
other file it would be equal to something like __main__.thatfilename 
and so on till it reach's the file location"""
if __name__ == '__main__':
    app.run()