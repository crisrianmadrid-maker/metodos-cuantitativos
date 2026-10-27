# Importar las liberías necesarias
from sqlalchemy import Column, Numeric, Integer, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd

# Información de conexión a PostgreSQL
USER = "escuela_user"
PASSWORD = "cris12345"
HOST = "localhost"
PORT = "5432"
DB_NAME = "escuela_db"
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# Creating a Database Connection

# SQLAlchemy creates database connections using create_engine() function. This function takes a
# connection URL and returns an engine object, which manages the connection between Python and the database.


engine = create_engine(DATABASE_URL)

# Declarar la base para los modelos
Base = declarative_base()


#  Definir la clase (tabla 'cotizaciones')
class Calificaciones(Base):
  __tablename__ = "calificaciones"

  id = Column(Integer, primary_key=True, autoincrement=True)
  alumno_id = Column(Integer, nullable=False)
  materia_id = Column(Integer, nullable=False)
  calificacion = Column(Numeric(precision=5, scale=2))
#  Crear una sesión para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()



mi_query= session.query(Calificaciones).filter(Calificaciones.materia_id == 5)
df = pd.read_sql(mi_query.statement, session.bind)


#---------------------------------------------------------------------
#sentencia = text("SELECT * FROM calificaciones where materia_id = 5;")
#resultado = session.execute(sentemi_queryncia)
#-----------------------------------------------------------------------

# Cerrar sesión
session.close()


#datos = pd.DataFrame(resultado.fetchall(), columns=resultado.keys())

media = df['calificacion'].astype(float).mean()
varianza = df['calificacion'].astype(float).var()
desviacion_estandar = df['calificacion'].astype(float).std()




