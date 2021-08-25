import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SERVER = 'smtp.office365.com'
PORT = 587
MY_PASS = '*******'
#MY_MAIL =['anton.rubanik@pmi.com,alexandr','vyacheslav.ilyasov@pmi.com']#'anton.rubanik@pmi.com,alexandr.kovbasiuk@pmi.com,vyacheslav.ilyasov@pmi.com'
MY_MAILS =['anton.rubanik@pmi.com,alexandr','aleksey.chernov@pmi.com']
mail_content = 'Рассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\nРассылка Рассылка Рассылка\n'

msg = MIMEMultipart()

msg['From'] = 'anton.rubanik@pmi.com'
msg['To'] = ''
msg['Subject'] = 'Генератор спама'

msg.attach(MIMEText(mail_content, 'plain'))

for i in range(5):
    MY_ADDRESS = 'arubanik@pmintl.net'
    mailserver = smtplib.SMTP(SERVER,PORT)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(MY_ADDRESS, MY_PASS)
    #Adding a newline before the body text fixes the missing message body
    mailserver.sendmail('anton.rubanik@pmi.com',MY_MAILS,msg.as_string())
    mailserver.quit()
