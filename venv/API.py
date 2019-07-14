from flask import Flask #import Flask module from flask package.
                        #Flask used to create instances of web application.
app = Flask(__name__)   #This line create an instance of your web application.
                        # __name__ is a special variable in python, it will equal to “__main__”
                        # if the module(python file) being executed as the main program.

@app.route("/hello")
def hello():            #This line define function that will be executed if we access route.
    return "Hello World!"

if __name__ == '__main__':  #This line mean that your flask app will being run if we run from app.py.
    app.run(debug=True)     # Notice also that we are setting the debug parameter to true.
                            # That will print out possible Python errors on the web page helping us trace the errors.
