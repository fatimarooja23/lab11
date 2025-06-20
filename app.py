from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Home route (index page)
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Department page route
@app.route('/department')
def department():
    return render_template('department.html')

# Doctors page route
@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

# Emergency page route
@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

# Online page route
@app.route('/online', methods=['GET', 'POST'])
def online():
    success = False  # Default to False
    
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        city = request.form.get('city')
        country = request.form.get('country')
        time = request.form.get('time')
        doctor = request.form.get('doctor')
        
        # Process form data here (e.g., save to database, send email, etc.)
        
        # After processing, set success to True
        success = True
    
    return render_template('online.html', success=success)



# Primary page route
@app.route('/primary')
def primary():
    return render_template('primary.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Contact page route (you already have this)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False  # Default success state
    
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        city = request.form.get('city')
        country = request.form.get('country')
        preferred_time = request.form.get('preferred_time')
        doctor_for = request.form.get('doctor_for')

        # Here, you can process the form data (e.g., save to database, send email, etc.)

        # After processing, set success to True
        success = True

    # Pass the success variable to the template
    return render_template('contact.html', success=success)




if __name__ == "__main__":
    app.run(debug=True)
