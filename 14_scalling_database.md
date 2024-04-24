# Scaling Databases

Scaling databases is the process of adapting them to handle more data and users efficiently. It’s achieved by either upgrading existing hardware (vertical scaling) or adding more servers (horizontal scaling). Techniques like sharding and replication are key. This ensures databases continue to be a robust asset as they grow.

- indexing
# ACID
    Atomicity (Atomicitas): Atomicitas memastikan bahwa sebuah transaksi diperlakukan sebagai satu kesatuan kerja yang utuh, yang entah selesai sepenuhnya atau tidak dilakukan sama sekali. Dengan kata lain, jika salah satu bagian dari transaksi gagal, maka keseluruhan transaksi akan gagal, dan database akan tetap tidak berubah.

    Consistency (Konsistensi): Konsistensi memastikan bahwa sebuah transaksi membawa database dari satu keadaan yang valid ke keadaan lain yang valid pula. Ini menjamin bahwa semua modifikasi data dilakukan sesuai dengan aturan dan batasan yang telah ditetapkan, menjaga integritas database.

    Isolation (Isolasi): Isolasi memastikan bahwa eksekusi transaksi secara bersamaan menghasilkan hasil yang setara dengan eksekusi berurutan dari transaksi yang sama. Transaksi dieksekusi secara terisolasi satu sama lain, mencegah gangguan antar transaksi.

    Durability (Daya Tahan): Daya tahan menjamin bahwa setelah sebuah transaksi dikonfirmasi (committed), perubahannya bersifat permanen dan tidak akan hilang, bahkan jika terjadi kegagalan sistem. Perubahan yang dilakukan oleh transaksi yang sudah dikonfirmasi disimpan dalam memori yang tidak mudah hilang, biasanya penyimpanan disk, untuk memastikan persistensi data.

Properti-properti ini sangat penting untuk memastikan keandalan dan integritas data dalam sistem basis data relasional, terutama dalam lingkungan multi-pengguna dan bersamaan. Kepatuhan ACID sangat penting untuk menjaga konsistensi dan keandalan data, terutama dalam aplikasi di mana integritas data sangat krusial, seperti sistem keuangan, platform e-commerce, dan basis data perusahaan.
contohnya kalo di django
@transaction_atomic
kalo gorm
create -> if error rollback -> if not error commit


# TRANSACTION
Certainly! Here's an example in Python using SQLite to demonstrate a simple database transaction:

python

import sqlite3

# Connect to the SQLite database (creates if not exists)
conn = sqlite3.connect(':memory:')  # Use ':memory:' for in-memory database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )''')

# Sample data
users = [
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 40)
]

try:
    # Begin transaction
    conn.execute('BEGIN')

    # Insert multiple records into the table
    cursor.executemany('INSERT INTO users (id, name, age) VALUES (?, ?, ?)', users)

    # Update a record
    cursor.execute('UPDATE users SET age = 35 WHERE name = ?', ('Bob',))

    # Query the table
    cursor.execute('SELECT * FROM users')
    print("Records after update:")
    for row in cursor.fetchall():
        print(row)

    # Commit the transaction
    conn.commit()
    print("Transaction committed successfully.")
except sqlite3.Error as e:
    # Rollback the transaction in case of any error
    conn.rollback()
    print("Transaction rolled back due to error:", e)
finally:
    # Close the connection
    conn.close()

In this example:

    We establish a connection to an SQLite database (in-memory for simplicity).
    We create a users table if it does not exist.
    We define some sample data.
    We begin a transaction using BEGIN.
    We execute multiple SQL statements (inserting and updating records).
    If an error occurs, we roll back the transaction to maintain data integrity.
    Finally, we commit the transaction to save the changes made.






# N+1 PROBLEM
Certainly! The N+1 query problem often occurs in ORMs like GORM when dealing with relationships between tables. Here's an example in GORM demonstrating the N+1 query problem:

Suppose we have two models: User and Post, where each user can have multiple posts:

``` go

package main

import (
    "fmt"
    "gorm.io/driver/sqlite"
    "gorm.io/gorm"
)

type User struct {
    ID    uint
    Name  string
    Posts []Post // Relationship: User has many Posts
}

type Post struct {
    ID     uint
    UserID uint
    Title  string
    Body   string
}

func main() {
    // Connect to SQLite database
    db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})
    if err != nil {
        panic("failed to connect database")
    }
    defer db.Close()

    // Migrate the schema
    db.AutoMigrate(&User{}, &Post{})

    // Create some users and posts
    db.Create(&User{Name: "Alice", Posts: []Post{{Title: "Post 1", Body: "Body 1"}, {Title: "Post 2", Body: "Body 2"}}})
    db.Create(&User{Name: "Bob", Posts: []Post{{Title: "Post 3", Body: "Body 3"}}})

    // Fetch users along with their posts (N+1 query)
    var users []User
    db.Preload("Posts").Find(&users)

    // Print users and their posts
    for _, user := range users {
        fmt.Printf("User: %s\n", user.Name)
        for _, post := range user.Posts {
            fmt.Printf("  Post: %s\n", post.Title)
        }
    }
}
```

In this example:

    We have two models: User and Post, with a one-to-many relationship between them.
    We create some users along with their posts.
    When fetching users using db.Preload("Posts").Find(&users), GORM executes a query to fetch all users and then N additional queries (one for each user) to fetch their posts. This leads to the N+1 query problem, where we end up executing N additional queries to fetch the same data that could have been retrieved in a single query.

To avoid the N+1 query problem in GORM, you can use eager loading techniques like Preload, Joins, or Select to fetch associated data in a single query.


# Normalization
https://www.guru99.com/database-normalization.html


# FAILURE MODES
Failure Modes

There are several different failure modes that can occur in a database, including:

    Read contention: This occurs when multiple clients or processes are trying to read data from the same location in the database at the same time, which can lead to delays or errors.
    Write contention: This occurs when multiple clients or processes are trying to write data to the same location in the database at the same time, which can lead to delays or errors.
    Thundering herd: This occurs when a large number of clients or processes try to access the same resource simultaneously, which can lead to resource exhaustion and reduced performance.
    Cascade: This occurs when a failure in one part of the database system causes a chain reaction that leads to failures in other parts of the system.
    Deadlock: This occurs when two or more transactions are waiting for each other to release a lock on a resource, leading to a standstill.
    Corruption: This occurs when data in the database becomes corrupted, which can lead to errors or unexpected results when reading or writing to the database.
    Hardware failure: This occurs when hardware components, such as disk drives or memory, fail, which can lead to data loss or corruption.
    Software failure: This occurs when software components, such as the database management system or application, fail, which can lead to errors or unexpected results.
    Network failure: This occurs when the network connection between the database and the client is lost, which can lead to errors or timeouts when trying to access the database.
    Denial of service (DoS) attack: This occurs when a malicious actor attempts to overwhelm the database with requests, leading to resource exhaustion and reduced performance.

- DEADLOCK EXAMPLE
Sure, here's an example of a deadlock scenario using SQLAlchemy with a PostgreSQL database:

```python

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import threading

Base = declarative_base()

# Define a simple database model
class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)

# Connect to a PostgreSQL database
engine = create_engine('postgresql://username:password@localhost/db_name')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)

def transaction1():
    session = Session()
    session.begin()
    try:
        # Simulate a transaction that needs both resources
        session.query(Data).with_for_update().all()  # acquire lock on resource 1
        # Simulate waiting for resource 2
        with session.begin_nested():
            session.query(Data).with_for_update().all()  # acquire lock on resource 2
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Transaction 1 failed: {e}")
    finally:
        session.close()

def transaction2():
    session = Session()
    session.begin()
    try:
        # Simulate a transaction that needs both resources
        session.query(Data).with_for_update().all()  # acquire lock on resource 2
        # Simulate waiting for resource 1
        with session.begin_nested():
            session.query(Data).with_for_update().all()  # acquire lock on resource 1
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Transaction 2 failed: {e}")
    finally:
        session.close()

# Create and start the threads
thread1 = threading.Thread(target=transaction1)
thread2 = threading.Thread(target=transaction2)
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Program finished")
```







# PROFILING PERFORMANCE
Profiling Performance

There are several ways to profile the performance of a database:

    Monitor system performance: You can use tools like the Windows Task Manager or the Unix/Linux top command to monitor the performance of your database server. These tools allow you to see the overall CPU, memory, and disk usage of the system, which can help identify any resource bottlenecks.
    Use database-specific tools: Most database management systems (DBMSs) have their own tools for monitoring performance. For example, Microsoft SQL Server has the SQL Server Management Studio (SSMS) and the sys.dm_os_wait_stats dynamic management view, while Oracle has the Oracle Enterprise Manager and the v$waitstat view. These tools allow you to see specific performance metrics, such as the amount of time spent waiting on locks or the number of physical reads and writes.
    Use third-party tools: There are also several third-party tools that can help you profile the performance of a database. Some examples include SolarWinds Database Performance Analyzer, Quest Software Foglight, and Redgate SQL Monitor. These tools often provide more in-depth performance analysis and can help you identify specific issues or bottlenecks.
    Analyze slow queries: If you have specific queries that are running slowly, you can use tools like EXPLAIN PLAN or SHOW PLAN in MySQL or SQL Server to see the execution plan for the query and identify any potential issues. You can also use tools like the MySQL slow query log or the SQL Server Profiler to capture slow queries and analyze them further.
    Monitor application performance: If you are experiencing performance issues with a specific application that is using the database, you can use tools like Application Insights or New Relic to monitor the performance of the application and identify any issues that may be related to the database.

Have a look at the documentation for the database that you are using.
https://one.newrelic.com/



