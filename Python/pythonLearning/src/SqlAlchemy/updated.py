import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine("mysql+pymysql://root:password@\
localhost/Geeks4Geeks")

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Students(Base):

    __tablename__ = 'students'

    first_name = db.Column(db.String(50), 
                           primary_key=True)
    last_name  = db.Column(db.String(50), 
                           primary_key=True)
    course     = db.Column(db.String(50))
    score      = db.Column(db.Float)

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Profile(Base):

    __tablename__ = 'profile'

    email   = db.Column(db.String(50), primary_key=True)
    name    = db.Column(db.String(100))
    contact = db.Column(db.Integer)

class Location(Base):

    __tablename__ = 'location'

    email = db.Column(db.String(50), primary_key=True)
    location = db.Column(db.String(100))

# CREATE THE SESSION OBJECT
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# TESTING OUR SESSION OBJECT
result = session.query(Students).all()

# SELECT first_name FROM students
result = session.query(Students.first_name)
print("Query 1:", result)

# SELECT first_name, last_name, course 
# FROM students
result = result.add_columns(Students.last_name, 
                            Students.course)
print("Query 2:", result)

for r in result:
    print(r.first_name, "|", r.last_name, "|", r.course)


# SELECT * FROM PROFILE
result = session.query(Students).count()

# VIEW THE RESULT
print("Count:", result)

# SELECT DISTINCT(first_name) FROM students;
result = session.query(Students) \
    .with_entities(db.distinct(Students.first_name)).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r)


# DELETE FROM profile WHERE email = 'ravipandey@zmail.com'
result = session.query(Profile) \
    .filter(Profile.email == 'ravipandey@zmail.com') \
        .delete(synchronize_session=False)
print("Rows deleted:", result)

result = session.query(Profile).count()
print("Total records:", result)


# SELECT email FROM student WHERE name LIKE 'Amit%';
result = session.query(Profile) \
    .with_entities(Profile.email) \
    .filter(Profile.name.like('Amit%')).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print("\n", r.email)

# SELECT first_name, last_name, SUM(score)
# AS total FROM students GROUP BY first_name, last_name;
result = session.query(Students) \
    .with_entities(
        Students.first_name,
        Students.last_name,
        db.func.sum(Students.score).label('total')
).group_by(
        Students.first_name,
        Students.last_name
).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r.first_name, r.last_name, "| Score =", r[2])

# SELECT * FROM students ORDER BY score DESC, course;
result = session.query(Students) \
    .order_by(
        Students.score.desc(),
        Students.course
).all()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r.first_name, r.last_name, r.course, r.score)


# SELECT * FROM profile LIMIT 1
result = session.query(Profile).first()

print(result.email, "|", result.name, "|", result.contact)

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r.email, r.name, r.contact)

# SELECT * FROM PROFILE
result = session.query(
    Profile.email,
    Profile.name,
    Profile.contact,
    Location.location
).join(Location, Profile.email == Location.email)

print("Query:", result)
print()

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r.email, "|", r.name, "|", r.contact, "|", r.location)


