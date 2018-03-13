import smtplib as sp

try:
	# taking credentials and informations
	username = input("Enter email please: ")
	password = input("Enter password please: ")
	reciever = input("Enter email of reciever please: ")
	subject = input("Enter subject please: ")
	body = input("Enter Body please: ")


	# checking the website's name
	_, domain = username.split('@')

	try:
	# assigning the proper server request
	if domain == 'gmail.com':
		smtpObj = sp.SMTP('smtp.gmail.com', 587)
	else:
		smtpObj = sp.SMTP('smtp.mail.{0}'.format(domain), 587)

	# establish HELLO
	smtpObj.ehlo()

	# starting tls encryption
	smtpObj.starttls()

	# logging in 
	smtpObj.login('' + username, ''+ password)
	
	# sendinf the mail
	smtpObj.sendmail('' + username, '' + reciever, 'Subject:{0}\n{1}'.format(subject, body))

	# closing the server
	smtpObj.quit()

	# indication of task done
	print('Email delivered.')
except Exception as e:
    logging.error(traceback.format_exc())
