import mysql.connector

# 1️⃣ Connect
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5255ravi",
    database="10000coders"
)

cursor = mydb.cursor()

# 2️⃣ Create table (okatey run cheyyi)
cursor.execute("""
CREATE TABLE IF NOT EXISTS `54r` (
    sno INT PRIMARY KEY AUTO_INCREMENT,
    s_name VARCHAR(50),
    s_email VARCHAR(100),
    s_mobile VARCHAR(15),
    s_city VARCHAR(50)
)
""")
print("Table created successfully!")

# 3️⃣ Insert values (executemany)
sql = "INSERT INTO `54r` (s_name, s_email, s_mobile, s_city) VALUES (%s, %s, %s, %s)"
values = [
    ("Krishna", "krishna@example.com", "9876500000", "Chennai"),
    ("Sita", "sita@example.com", "9876511111", "Bangalore"),
    ("Arjun", "arjun@example.com", "9876522222", "Delhi"),
    ("siva","siva@gamil.com","8973492","kkd")
]

cursor.executemany(sql, values)
mydb.commit()
print(cursor.rowcount, "records inserted successfully!")

# ✅ Clear any unread results before next execute
cursor.fetchall() if cursor.with_rows else None

# 4️⃣ Select the 'siva' row
cursor.execute("SELECT * FROM `54r` WHERE TRIM(LOWER(s_name)) = 'siva'")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Table empty cheyyi
cursor.execute("TRUNCATE TABLE `54r`")  # removes all previous rows
mydb.commit()
print("Table cleared!")


