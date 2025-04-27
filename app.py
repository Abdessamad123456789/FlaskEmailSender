from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Configure your email settings here
EMAIL_ADDRESS = 'your_email'
EMAIL_PASSWORD = 'your_password'

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        to_email = request.form['to_email']
        subject = request.form['subject']
        message = request.form['message']

        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)

            flash('Email sent successfully!', 'success')
        except Exception as e:
            print(e)
            flash('Failed to send email.', 'error')

        return redirect('/')
    
    return render_template('send_email.html')

if __name__ == '__main__':
    app.run(debug=True)
