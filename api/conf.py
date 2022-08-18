"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count

def max_workers():    
    return cpu_count()

bind = '54.88.233.66:8000'
max_requests = 1000
workers = max_workers() 
