from cassandra.cluster import Cluster

def get_connection():
    cluster = Cluster(['localhost'], port=9042)  # Replace with your Cassandra nodes and port
    session = cluster.connect('your_keyspace_name')  # Replace with your keyspace name
    return session



