import feedparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

rss_channel = 'https://habr.com/rss/best/daily/'
filename = 'text.html'
data = feedparser.parse(rss_channel)

addr_from = '�� ����'
addr_to = '����'
password = '������'

msg = MIMEMultipart()
msg['From'] = addr_from
msg['To'] = addr_to
msg['Subject'] = 'Лучшее на habr.com за 24 часа'

with open(filename, "w", encoding='utf-8') as fp:
    fp.write('''
        <html>
        <head>
            <title>Лучшие публикации за сутки на habr.com</title>
            <style type="text/css">
            img {
                max-width: 50%;
                height: auto;
            }
            </style>
        </head>
        <body>
        </body>
        </html>
            ''')


head = data['feed']['title']
time = data['feed']['published']

with open(filename, 'a', encoding='utf-8') as fp:
    fp.write('<h1>' + head + '</h1>')
    fp.write('<h2>' + time + '</h2>')
    fp.write('<hr><hr>')

for i in range(len(data['entries'])):
    title_art = data['entries'][i]['title']
    time_art = data['entries'][i]['published']
    text_art = data['entries'][i]['summary']
    link_art = data['entries'][i]['id']
    author_art = data['entries'][i]['author']

    with open(filename, "a", encoding='utf-8') as fp:
        fp.write('<div>')
        fp.write('<h3>' + title_art + r'</h3>')
        fp.write('<h3>' + time_art + r'</h3>')
        fp.write('<h3>' + author_art + r'</h3>')
        fp.write(text_art + '<br>')
        fp.write('<hr>')
        fp.write('</div>')

with open(filename, encoding='UTF-8') as fp:
    file = MIMEText(fp.read())
    fp.close()
file.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(file)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(addr_from, password)
server.send_message(msg)
server.quit()
