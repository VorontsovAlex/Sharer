from redis import Redis

conn = Redis(host='172.20.10.2', port=6380)
print(conn.json().get('product:0002541'))