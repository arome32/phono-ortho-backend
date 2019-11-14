from flask import Flask, jsonify, request
from flask_cors import CORS
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return jsonify({ 'hello': 'Hello World!' })


@app.route('/<name>')
def hello_name(name):
    return jsonify({ 'name': name })

@app.route('/user', methods=['POST'])
def add_user():
  new_user = request.json
  create_csv(new_user['words'])
  return jsonify(new_user)

def create_csv(words):
    print('here')
    file = open('/tmp/pathname.csv','w+')
    file.write(',ORTHO TARGET,PRODUCTION,T/F')
    count = 0
    print('here')
    for word in words:
        boolVal = (words[word]['word'] == words[word]['spelled'])
        file.write(str(count) + ',' + words[word]['word'] + ',' + words[word]['spelled'] + ',' + str(boolVal) +',')
        count += 1
    file.close()
    print('finished 1')
    file = open('/tmp/pathname.csv','r+')
    print(file)
    for line in file:
        print(line)
    print('finished 2')
    sendEmail()
    
def sendEmail():
    print('1')
    emailfrom = "aromero.testing@gmail.com"
    emailto = "a.romero032@gmail.com"
    fileToSend = "/tmp/pathname.csv"
    username = "aromero.testing"
    password = "Rocknroll1!2"
    
    print('2')
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "help I cannot send an attachment to save my life"
    msg.preamble = "help I cannot send an attachment to save my life"
    print('3')

    fp = open(fileToSend)
    print('4')
    
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read())
    fp.close()
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)
    print('5')

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()
    print('6')


if __name__ == '__main__':
    app.run()