
import pyodbc

print 'Conectando...'


dsn = 'MyAwesomeDBConnection'
user = 'sms'
password = 'sms0l42015'
database = 'fpsp_pe'

con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
cnxn = pyodbc.connect(con_string)
cursor = cnxn.cursor()
cursor.tables()
rows = cursor.fetchall()

a="select  count(*) FROM ordenestrabajo"
b=" INNER JOIN almacenes ON ordenestrabajo.codemp = almacenes.codemp AND ordenestrabajo.codalm = almacenes.codalm"
c= " RIGHT OUTER JOIN clientes ON ordenestrabajo.codemp = clientes.codemp AND ordenestrabajo.codcli = clientes.codcli"
d= " WHERE (ordenestrabajo.codemp = '21') AND (ordenestrabajo.estrec = '1') AND (ordenestrabajo.estent = '0')"
cursor.execute(a+b+c)


rows = cursor.fetchall()
for row in rows:
    total = row[0]




