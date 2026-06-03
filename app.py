from flask import Flask,render_template,request,redirect
import pandas as pd
import os
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
    password = request.form.get('password')
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
    users_df.to_csv(os.path.join(os.path.dirname(__file__), 'users.csv'), index=False)

    return render_template('returnmsg.html')
@app.route('/game')
def game():
    try:
        users_df = pd.read_csv('users.csv')
    except FileNotFoundError:
        users_df = pd.DataFrame(columns=['user_id','username','email','password','occupation','points'])

    # Sort by points (descending) or any other column
    users_df = users_df.sort_values(by='points', ascending=False)

    # Convert DataFrame to list of dicts for Jinja2
    users_list = users_df.to_dict(orient='records')
    
    top_users = users_df.head(5).to_dict(orient='records')

    while len(top_users) < 5:
        top_users.append({
            "user_id": None,
            "username": "-----",
            "email": "",
            "occupation": "",
            "points": 0
        })
    return render_template('game.html', users=top_users)

@app.route('/report', methods=['POST'])
def report():
    try:
        users_df = pd.read_csv('users.csv')
    except FileNotFoundError:
        users_df = pd.DataFrame(columns=['user_id','username','email','password','occupation','points'])

    username = request.form.get('username')
    location = request.form.get('location')
    description = request.form.get('description')

    # Handle file upload
    file = request.files['image']
    if file and file.filename != '':
        upload_folder = os.path.join(os.path.dirname(__file__), 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, file.filename)
        file.save(filepath)

    # Increment points
    if username in users_df['username'].values:
        users_df.loc[users_df['username'] == username, 'points'] += 10
    else:
        new_user = {
            'user_id': len(users_df) + 1,
            'username': username,
            'email': '',
            'password': '',
            'occupation': '',
            'points': 10
        }
        users_df = pd.concat([users_df, pd.DataFrame([new_user])], ignore_index=True)

    users_df.to_csv('users.csv', index=False)

    # Redirect back to leaderboard
    return redirect('/game')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/shop')
def shop():
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


