import requests
import smtplib
from lxml import html

fromaddr = "YOUR EMAIL"
toaddr = "WHERE TO SEND MAIL"
msg = "Batman Preventa - Cinepolis"
msg2 = "Batman Preventa - CineMex"
username = "USERNAME"
password = "PASWORD"
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)


head = {"Cookie":"Ciudad=tijuana"}
r = requests.get('http://www.cinepolis.com/manejadores/CarteleraPreventas.ashx?CP=CinepolisMX')
cmx = requests.get('http://www.cinemex.com')

if "batman" in r.content:
    print("Cinepolis: Fount It!")
    server.sendmail(fromaddr,toaddr,msg)
    server.quit()
else:
    print("Cinepolis: Not Found")


cnmxcontent = html.fromstring(cmx.content)
preventas = cnmxcontent.xpath('//div[@class="tab-content tab-content-presales"]/div[@class="row xs-clear-on-3 sm-clear-on-3 md-clear-on-4 clearfix movies-grid"]/div/a[@class="movies-grid-title"]/text()')

if any("Batman" in elm  for elm in preventas):
    print("Cinemex: Found It!")
    server.sendmail(fromaddr,toaddr,msg2)
    server.quit()
else:
    print("Cinemex: Not Found")