import psycopg2
import psycopg2.extras
from contextlib import contextmanager
from core.settings import settings

db_config = {
    "host": settings.DB_HOST,
    "port":settings.DB_PORT,
    "user":settings.DB_USER,
    "password":settings.DB_PASSWORD,
    "database":settings.DB_NAME
}

# connection
def get_connection():
    return psycopg2.connect(**db_config)

# connection
@contextmanager
def get_db_connection():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


