from flask import Flask, render_template, request
import smtplib
import os

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
    return render_template("index.html")


def send_email(name, email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="alexispaluch@gmail.com",
            msg=f"Subject: Message from Blog\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message:{message}")


if __name__ == "__main__":
    app.run(debug=True)
    