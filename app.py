from flask import Flask,render_template,request
import pandas as pd

app=Flask(__name__)
@app.route('/signin')
def signin():
    return render_template('sign-in.html')

@app.route('/calculate', methods=['POST'])
def calculate():
  
    try:
        users_df = pd.read_csv('users.csv')
    except FileNotFoundError:
       
        users_df = pd.DataFrame(columns=['user_id','username','email','password','occupation','points'])

   
    username = request.form.get('Username')
    email = request.form.get('Email')
    password = request.form.get('Password')
    occupation = request.form.get('Occupation')

    
    next_id = len(users_df) + 1

   
    new_user = {
        'user_id': next_id,
        'username': username,
        'email': email,
        'password': password,   # ideally hash this
        'occupation': occupation,
        'points': 0
    }

    
    new_user_df = pd.DataFrame([new_user])   # turn dict into one-row DataFrame
    users_df = pd.concat([users_df, new_user_df], ignore_index=True)

    return render_template('returnmsg.html')

@app.route('/')
def index():
    return render_template('shop.html')
@app.route('/module')
def module():
    return render_template('module.html')
@app.route('/training')
def training():
    return render_template('training.html')
@app.route('/map')
def map():
    return render_template('map.html')   


if __name__ == '__main__':
    app.run(debug=True)


