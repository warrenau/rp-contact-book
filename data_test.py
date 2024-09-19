from rpcontacts.database import createConnection
from PyQt5.QtSql import QSqlQuery


# create a connection
createConnection("contacts.sqlite")

# Prepare a query to insert sample data
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

# Sample data
data = [
    ("Linda", "Technical Lead", "linda@example.com"),
    ("Joe", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
]

# Insert sample data
for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()



query = QSqlQuery()
query.exec("SELECT name, job, email FROM contacts")

while query.next():
    print(query.value(0), query.value(1), query.value(2))