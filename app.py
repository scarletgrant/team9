'''Code is commented for beginning programmers to read and understand every line.
    Will be simplified afterwards.
'''
#!/usr/bin/env/python
# import Flask in this app script from flask on the server
# import render_template to render a template from the app, in this case our index.html that we saved as template. Don't forget the comma
from flask import Flask, render_template, url_for

# Creat a Flask application with the name and filename of the app. Static files are served from the 'statis' directory.
app = Flask(__name__)#, static_url_path='')

# the route specifies the internal url and serves 'index.html'.
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return "<h1>map</h1>"




#from flask import abort
#app.route("/user/<id>")
#def get_user(id):
#    user = load_user(id) if not user:
#    abort(404)
    #return '<h1>Hello, %s</h1>' % user.name



# Ads condition in the script and runs it in debug mode
# If the script is the main function than run it. Check that it is this script that is 
# actually being executed and not any other.
if __name__ == "__main__":
    # if yes, than run (when you put the app in debug mode you don't have to restart the server all the time to see any changes in the script.)
    # app.debug = True
    app.run(debug=True)

# It won't make sense to load all elements again and again with each view so we create a 
# layout.html to store all of this and then wrap the current view in to this
# do all this in layout.html and put the body in {% block body %} {% end block %}

#@app.route("/bike-stations")
#def get_bike-stations():
    # returns all bike stations
    # function
    #return #

#@app.route("/available-bikes")
#def available-bikes():
    # returns number of available bikes at stations within 250/500/100 mt
    # function
    #return #
    
#@app.route("/weather-forecast")
#def weather-forecast():
    # returns forecasted weather 
    # function
    #return #

#@app.route("/available-bikes-forecast")
#def available-bikes-forecast():
    # returns forecast of available bikes
    # function
    #return #