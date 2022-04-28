from datetime import datetime
from sqlalchemy import delete, insert
from database.connection import engine, session, db_metadata, select, desc, insert, delete
from database.schemas.pekerja import tabelPekerja
from flask import Flask, redirect, url_for, request
from datetime import datetime

#Buat koneksi
connection = engine.connect()

#Tabel pekerja di definisikan
pekerja = tabelPekerja(db_metadata)

#Cek tabel 'pekerja' exist atau tidak
if (engine.has_table('pekerja')):
    pass
else:
    db_metadata.create_all(engine)
    print("=====\nSukses buat tabel baru\n=====\n")

# Mulai kerja API
# Setiap ada @, itu disebut decorator, buat deteksi URL path yang di hit

#Prepare all flask instances
app = Flask(__name__)

#Template response gagal
resultFailed = {
        'status' : 'error',
        'message' : 'cek ulang body request'
    }   

#Get semua data
@app.route('/api/get_all_data', methods=['GET'])
def getAllData():
    try:
        value = request.args['sort']
    except:
        value = 'normal' 

    if (value == 'dsc'):
        query = select([pekerja]).order_by(desc('created_at'))
    elif (value == 'asc'):
        query = select([pekerja]).order_by('created_at')
    else:
        query = select([pekerja])

    queryResult = connection.execute(query).fetchall()
    result = []
    for singleResult in queryResult:
        objectResult = {
            'id': singleResult.id,
            'nama': singleResult.nama,
            'umur': singleResult.umur,
            'jabatan': singleResult.jabatan,
            'created_at': singleResult.created_at
        }
        result.append(objectResult)
    result = {
        'status' : 'success',
        'total_data': len(queryResult),
        'message' : 'success get all data',
        'data': result
    }
    return result

#Post data
@app.route('/api/post_data', methods=['POST'])
def postData():
    f = request.form
    nama = ''      
    umur = ''
    jabatan = ''
    #Cek tipe data
    if((isinstance(nama, str)) and (isinstance(jabatan, str))):
        try:
            nama = f['nama']        
            umur = f['umur']
            jabatan = f['jabatan']
            umur = int(umur)
            query = insert(pekerja).values(nama=nama, umur=umur, jabatan=jabatan, created_at=datetime.now())
            connection.execute(query)
            result = {
                'status' : 'success',
                'message' : 'berhasil tambahkan data',
                'data' : {
                    'nama' : nama,
                    'umur' : umur,
                    'jabatan': jabatan
                }
            }
        except:
            result = resultFailed
    else:
        result = resultFailed
    
    return result

#delete data
@app.route('/api/delete_data', methods=['DELETE'])
def delete_data():
    f = request.form
    id = ''
    try:
        id = f['id']
        id = int(id)
        query = pekerja.delete().where(pekerja.c.id==id)
        connection.execute(query)
        result = {
            'status': 'success',
            'message': 'berhasil hapus data',
            'id': id
        }
    except:
        result = resultFailed
    return result

if __name__ == '__main__':
    app.run()