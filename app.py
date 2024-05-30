from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'charancharry08@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'bcwcqibjvfklyihp'  # Replace with your email password

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    # Handle email sending logic here

    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    email = data['email']
    message = data['message']

    msg = Message('New Contact Form Submission',
                  sender=email,
                  recipients=['charancharry08@gmail.com'])  # Replace with your email
    msg.body = f"First Name: {first_name}\nLast Name: {last_name}\nPhone: {phone}\nEmail: {email}\nMessage:\n{message}"

    try:
        mail.send(msg)
        return jsonify({"message": "Email successfully sent!"}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to send email: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
