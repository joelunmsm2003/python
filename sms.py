import time
import pyodbc

import requests
import urllib
import json


dsn = 'MyAwesomeDBConnection'
user = 'sms'
password = 'sms0l42015'
database = 'fpsp_pe'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)
cursor = cnxn.cursor()
cursor.tables()


a="select  count(*) FROM ordenestrabajo"
b=" INNER JOIN almacenes ON ordenestrabajo.codemp = almacenes.codemp AND ordenestrabajo.codalm = almacenes.codalm"
c= " RIGHT OUTER JOIN clientes ON ordenestrabajo.codemp = clientes.codemp AND ordenestrabajo.codcli = clientes.codcli"
d= " WHERE (ordenestrabajo.codemp = '21') AND (ordenestrabajo.estrec = '1') AND (ordenestrabajo.estent = '0')"

url ="http://dilootu.com/init/default/"
username = 'emisajel@integra.com'
password = 'Afpintegra4'
phone_number = '51975630660'
text_message = 'heloo'

headers = {'Content-Type': 'application/json'}
params = {'username' : 'emisajel@integra.com','password' : password,'phone_number':phone_number,'text_message':text_message}
reply = requests.get(url, params=params,headers=headers)
print reply.url


class Sms:

  def conteo(self):


    cursor.execute(a+b+c)
    print 'Executing SQL...'

    rows = cursor.fetchall()
    for row in rows:
      total = row[0]
      self.total = total

class Envio:

  def enviar(self,username,password,phone_number,text_message):

    #http://dilootu.com/init/default/api?username=USR&password=123&phone_number=991935157&text_message=HOLA

    url ="http://dilootu.com/init/default/"
    username = 'emisajel@integra.com'
    password = 'Afpintegra4'
    phone_number = '51975630660'
    text_message = 'heloo'
    params = {'username' : username,'password' : password,'phone_number':phone_number,'text_message':text_message}
    reply = requests.get(url, params=params)
    print reply.url





while (1):

  objeto= Sms()
  objeto.conteo()

  print(objeto.total)
  if objeto.total > 0 :

    envsms = Envio()
    envsms.enviar('emisajel@integra.com.pe','Afpintegra4','51975630660','holajoel')

    #Enviar sms por web2py
    #Actualizar sus tablas

   
  time.sleep(10000)

print "Good bye!"



