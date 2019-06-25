from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.L3_D3_db

# Set route
@app.route('/')
def index():
    # Set root_list to document in MongoDB
    root_list = db.list_of_lists_of_lists.find()

    # Return the template with the Lists object passed in
    return render_template('index.html', root_list=root_list)


if __name__ == "__main__":
    app.run(debug=True)
