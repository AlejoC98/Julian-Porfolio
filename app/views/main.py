from flask import request, redirect, render_template, url_for, session, Blueprint, json, jsonify
from app import mail
from flask_mail import Message

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/About")
def about():
    return render_template("about.html")

@main.route("/Contact")
def contact():
    return render_template("contact.html")

@main.route("/Send-contact", methods=["POST", "GET"])
def sendcontact():

    data = request.form.to_dict()

    msg = Message(
        'A potencional customer is trying to contact you.',
        sender='Management',
        recipients=["ph.julianrd@gmail.com"]
    )

    # with current_app.open_resource("static/img/RealmFly/Vertical Realm Logo.png") as fp:
    #     msg.attach("static/img/RealmFly/Vertical Realm Logo.png", "image/png",
    #                fp.read(), 'inline', headers=[['Content-ID', '<logo>'], ])

    # with current_app.open_resource("static/img/Email/email_white.png") as fp:
    #     msg.attach("static/img/Email/email_white.png", "image/png",
    #                fp.read(), 'inline', headers=[['Content-ID', '<email_icon>'], ])

    # Email template
    msg.html = render_template(
        'email.html', User = "ph.julianrd@gmail.com", email_data = data)

    try:
        mail.send(msg)
        status = True        
    except Exception as e:
        status = False        
    
    if status == True:
        response = "SENDING"
    else:
        response = "ERROR"

    return response