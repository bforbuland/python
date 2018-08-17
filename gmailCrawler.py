from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import gmailcount
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
sender=input("my email id:")
password=input("my password:")
receiver=input("your email id:")
subject='gmail Crawler'
textfile=open('D:\\output.txt', 'w')
msg('From')=sender
msg('To')=receiver
msg('To')=subject
body=('please get the attachment')
msg.attach(MIMEText(body,'plain'))
attachment=open('D:\\output.txt', 'rb')
part=MIMEBase('application','octet-stream')
part.set_payload(attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment;output.txt' +output.txt) #to get the output in the text file
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

inbox=gmailcount(label='INBOX')
spam=gmailcount(label='SPAM')
if spam/inbox<1:
    textfile.write('Good')
    server.sendmail(sender,receiver,text)
else:
    textfile.write('Poor')
    server.sendmail(sender,receiver,text)

server.quit()
textfile.close()
