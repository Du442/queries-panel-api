from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import URL
import os
from dotenv import load_dotenv
from typing import Generator

# Override para definir .env como principal
load_dotenv(override=True)

# URL.create para definição mais organizada do path de acesso ao db
path = URL.create(
    drivername = os.getenv("DRIVERNAME", "postgresql+psycopg2"),
    user = os.getenv("USERNAME"),
    psw = os.getenv("PASSWORD"),
    host = os.getenv("HOST"),
    port = int(os.getenv("PORT")),
    db = os.getenv("DATABASE")
)

# Definição do engine através do URL criado
engine = create_engine(path, echo=True, pool_pre_ping=True)

# Função de iniciar a db
def init_db() -> None:

    # Import schemas after

    SQLModel.metadata.create_all(engine)

# Função de criar a session na db através do engine.
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session