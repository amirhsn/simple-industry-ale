from sqlalchemy import *
from database.connection import engine

#Variabel tabel pekerja
def tabelPekerja(metadata):
    pekerja = Table(
        'pekerja',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('nama', String(100), nullable=False),
        Column('umur', Integer, nullable=False),
        Column('jabatan', String(100), nullable=False),
        Column('created_at', DateTime, nullable=False)
    )
    return pekerja