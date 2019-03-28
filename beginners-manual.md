**CONCEPT MANUAL TO RUN THE APP**

To start the app have python installed on your environment:

Install Python on the Mac:
  
Install latest pip:
    
    python3 -m pip install --user --upgrade pip
    

Installing virtual Environment
    
    python3 -m pip install --user virtualenv
    

Creating a virtual environment:
    
    python3 -m virtualenv env

Activate virtual environment:
    
      eg.: 
      
        source env/bin/activate
        
      or: 
      
        source /Users/admin/Documents/UCD/2_Software_Engineering/team9_dublinBikes_venv_py_37/bin/activate

  Install Flask
  
    pip install Flask
    
    pip install -U Flask

  Leaving virtual env:
  
    eg.: (team9_dublinBikes_venv_py_37) Scarlets-iMac:~ admin$ 
    
            deactivate

  Go to direcotory of app:
  
    eg.: Scarlets-iMac:~ admin$ 
    
            cd /Users/admin/Documents/UCD/2_Software_Engineering/team9

Set an environment variable to the file that will want to be pour Flask application. 

    Scarlets-iMac:team9 admin$ export FLASK_APP=app.py
    
    (On Windows use: set FLASK_APP=app.py)
    
Run the app

    flask run

    * Serving Flask app "app.py"

    * Environment: production

      WARNING: Do not use the development server in a production environment.
  
     Use a production WSGI server instead.
  
    * Debug mode: off

    * Running on http://127.0.0.1:5000/

    or http://localhost:5000/

    run application in debug mode to not having to terminate and rerun the app in terminal again for every change (on windows set instead of export):

    export FLASK_DEBUG=1

    flask run

Now changes happen immediate and you only have to refresh the browser. To do this easier we add in the function in the app:

if __name__ == "__main__":

    # if yes, than run (when you put the app in debug mode you don't have to restart the server all the time to see any changes in the script.)
   
    # app.debug = True
   
    app.run(debug=True)


"""
Have flask-mysqldb installed

In terminal:

    pip install flask-mysqldb

Leaving the virtualenv:

    deactivate

    create app.py

    python app.py

SEE APP FILES FOR COMMENTS
