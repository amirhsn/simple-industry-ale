from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

#Mesin DB
username = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'simple_industry'
engine = create_engine('mysql://'+username+':'+password+'@'+host+':'+port+'/'+database, echo=False)

#Variabel untuk simpan seluruh metadata
db_metadata = MetaData()

#Variabel untuk menyimpan sesi untuk setiap kali akses DB
Session = sessionmaker(bind=engine)
session = Session()