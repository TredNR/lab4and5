from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'b5fa374447f10b'
app.config['MYSQL_DATABASE_PASSWORD'] = '7e50404a'
app.config['MYSQL_DATABASE_DB'] = 'heroku_8da7b2bec58bce2'
app.config['MYSQL_DATABASE_HOST'] = 'eu-cdbr-west-03.cleardb.net'
mysql.init_app(app)
