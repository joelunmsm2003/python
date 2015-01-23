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




class Cliente:

  def conteo(self):


    cursor.execute(a+b+c)
    print 'Executing SQL...'

    rows = cursor.fetchall()
    for row in rows:
      total = row[0]
      self.total = total


  def enviarSms(self,username,password,phone_number,text_message):

    #http://dilootu.com/init/default/api?username=USR&password=123&phone_number=991935157&text_message=HOLA

    url ="http://dilootu.com/init/default/api"
    params = {'username' : username,'password' : password,'phone_number':phone_number,'text_message':text_message}
    reply = requests.get(url, params=params)
    print reply.url





while (1):

  objeto= Cliente()
  objeto.conteo()

  print(objeto.total)

  if objeto.total > 0 :
    
    print 'Sms'
    #objeto.enviarSms('emisajel@integra.com.pe','Afpintegra4','51975630660','Esto es una prueba Xiencias')

    #Actualizar sus tablas

  time.sleep(10000)

print "Good bye!"



