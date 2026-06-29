from mysql.connector import pooling
from backend.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

_pool = None

def _get_pool():
    global _pool
    if _pool is None:
        _pool = pooling.MySQLConnectionPool(
            pool_name="todopool",
            pool_size=5,
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    return _pool

def get_connection():
    return _get_pool().get_connection()
