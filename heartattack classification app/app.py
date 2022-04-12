from flask import Flask , request , render_template
import pickle
import pandas as pd



# loading the envirenmental variables 
def load(path):
    with open(path,'rb') as f : 
        var = pickle.load(f)
    return(var)


model = load('./model.pickle')



# flask app 


# to run this program open your CMD.exe and cd into the folder 
# type in your cmd :   python app.exe     
# open your browser and open 127.0.0.1:5000

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def intro():
    # the template in a state of submitting
    if request.method =="POST":
        #if the fields are filled when submitting
        if request.form["age"] and request.form["cp"] and request.form["trestbps"] and request.form["chol"] and request.form["restecg"] and request.form["thalach"]:
            # getting the features and processing them
            age = float(request.form["age"])
            cp = float(request.form["cp"])
            trestbps = float(request.form["trestbps"])
            chol = float(request.form["chol"])
            fbs = float(request.form["fbs"])
            restecg = float(request.form["restecg"])
            thalach = float(request.form["thalach"])
            exang = float(request.form["exang"])
            oldpeak = float(request.form["oldpeak"])
            slope = float(request.form["slope"])
            ca = float(request.form["ca"])
            thal = float(request.form["thal"])
            # creating the feature
            X = [[age, cp, trestbps, chol, fbs, restecg, thalach, exang,
   oldpeak, slope, ca, thal]]
            # predicting the charges
            pred = model.predict(X)
            # final state 
            if pred[0] == 0 : 
                state = "Ok"
            else : 
                state = "ILL"
            # open the template using the variables
            return render_template('animatedlogin.html', pred=state)
    # the template in initial state
    return render_template('animatedlogin.html')




if __name__ == "__main__" :
    app.run(debug=True)
