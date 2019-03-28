'''Code is commented for beginning programmers to read and understand every line.
    Will be simplified afterwards.
'''
# import Flask in this app script from flask on the server
# import render_template to render a template from the app, in this case our index.html that we saved as template. Don't forget the comma
from flask import Flask, render_template

# app is a Flask application/function of Flask with the name and filename of the app
app = Flask(__name__)

# the route specifies where the location of the file? and url.
@app.route("/")
# eventually create extra route to the same view
@app.route("/home")

# function to return index.html. We create a folder calld templates in the root forlder as well where we store the index.html
def index():
    # it renders our index.html now. However, not the CSS that I also stored in templates.
    return render_template('index.html')
#creates extra page view
"""
#check tutorial 2 on minute 11, how to dynamically change title etc. https://www.youtube.com/watch?v=QnDWIZuWYW0
@app.route("/about")
def about():
    return "<h1>About</h1>"
"""
# It won't make sense to load all elements again and again with each view so we create a layout.html to store all of this and then wrap the current view in to this
# do all this in layout.html and put the body in {% block body %} {% end block %}

# Ads condition in the script and runs it in debug mode
# If the script is the main function than run it. Check that it is this script that is actually being executed and not any other.
if __name__ == "__main__":
    # if yes, than run (when you put the app in debug mode you don't have to restart the server all the time to see any changes in the script.)
    # app.debug = True
    app.run(debug=True)

    # flask wtform
# forms wysiwyg form editor
