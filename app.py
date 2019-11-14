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

@app.route('/wakeup')
def wakeup():
    return jsonify({ 'wakeup': 'true' })

@app.route('/user', methods=['POST'])
def add_user():
  new_user = request.json
  print(new_user)
  create_csv(new_user)
  return jsonify(new_user)

def create_csv(user):
    words = user['words']
    name = user['name']

    file = open('/tmp/' + name + '_pretest.csv','w+')
    file.write(',ORTHO TARGET,PRODUCTION,T/F,')
    file.write('\n')
    count = 0

    for word in words:
        boolVal = (words[word]['word'] == words[word]['spelled'])
        file.write(str(count) + ',' + words[word]['word'] + ',' + words[word]['spelled'] + ',' + str(boolVal) +',')
        file.write('\n')
        count += 1
    file.close()
    
    sendEmail(name)
    
def sendEmail(name):
    emailfrom = "aromero.testing@gmail.com"
    emailto = "a.romero032@gmail.com"
    fileToSend = '/tmp/' + name + '_pretest.csv'
    username = "aromero.testing"
    password = "Rocknroll1!2"
    
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = (name + " Pretest Results")
    msg.preamble = (name + " Pretest Results")

    fp = open(fileToSend)
    
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read())
    fp.close()
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

if __name__ == '__main__':
    app.run()