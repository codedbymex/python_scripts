import imaplib
import email
import subprocess

username   = "someone@gmail.com" #  USERNAME HERE
password  = "somepassword"  #  PASSWORD HERE

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)

# retrieve a list of the mailboxes and select one
result, mailboxes = mail.list()
mail.select("Test")

result, numbers = mail.uid('search', None, 'UNSEEN')
uids = numbers[0].split()

# set flag seen for unseen mails
for i in uids:
	mail.uid('store', i, '+FLAGS','\SEEN')

if len(uids) > 0:
	result, messages = mail.uid('fetch', ','.join(uids[-10:]), '(BODY.PEEK[HEADER])')
	
	mail_sender = []
	mail_subject = []

	for _, message in messages[::2]:
		msg = email.message_from_string(message)
		email_subject = msg['subject']
		email_from = msg['from']
		mail_sender.append(email_from)
		if len(email_subject) > 20:
			email_subject = email_subject[:65]
		mail_subject.append(email_subject)

	cmd = 'zenity --info --width=500 --title="You have a massage from: {}"'\
		.format(frommes[0]).replace("<", "").replace(">", "")\
		+' --text="Subject: {}"'.format("".join(x.split()[0] for x in subject))
	subprocess.call(cmd, shell=True)

else:pass


	

