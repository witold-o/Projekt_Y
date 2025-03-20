import time
import os
import psycopg2
import sys

def wait_for_db():
    """Wait for the database to be ready."""
    db_host = os.getenv("DB_HOST", "db")
    db_port = os.getenv("DB_PORT", "5432")
    db_user = os.getenv("DB_USER", "your_user")
    db_password = os.getenv("DB_PASSWORD", "your_password")
    db_name = os.getenv("DB_NAME", "task_db")
    
    max_retries = 30
    retry_interval = 2  # seconds
    
    print(f"Waiting for database at {db_host}:{db_port}...")
    
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                dbname=db_name
            )
            conn.close()
            print("Database is ready!")
            return True
        except psycopg2.OperationalError as e:
            print(f"Database not ready yet (attempt {i+1}/{max_retries}): {e}")
            time.sleep(retry_interval)
    
    print("Failed to connect to the database after multiple attempts.")
    return False

if __name__ == "__main__":
    if not wait_for_db():
        sys.exit(1)