"""SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/data.html
To create, select and manipulate data within a relational database
"""

from sqlalchemy import create_engine
from sqlalchemy import select, update, delete, insert, bindparam
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, relationship


# Establish connectivity - the Engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

Base = declarative_base()
# print(Base)

# Defining Table Metadata with the ORM
class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# print(User.__table__)
# print(Address.__table__)

# emit CREATE statements if given ORM registry
# mapper_registry.metadata.create_all(engine)
# The identical MetaData object is also present on the
# declarative base
Base.metadata.create_all(engine)

# Manipulate databases...
print("--- Instances of Classes represent Rows ---")
squidward = User(name="squidward", fullname='Squidward Tentacles')
krabs = User(name='ehkrabs', fullname='Eugene H. Krabs')
sandy = User(name="sandy", fullname="Sandy Cheeks")
patrick = User(name="patrick", fullname="Patrick Starr")
spongebob = User(name='spongebob', fullname='spongebob squarpants')
# print(id(krabs))

with Session(engine) as session:
    session.add(spongebob)
    session.add(squidward)
    session.add(krabs)
    session.add(sandy)
    session.add(patrick)

    # print(session.new)  # to see a collection on the session
    #session.flush()

    print(session.execute(select(User)).all())
    # print(squidward)
    # print(session.get(User, 1))
    session.commit()

print("--- Insert Rows with scalar subquery ---")
scalar_subquery = (
    select(User.id)
    .where(User.name==bindparam('username'))
    .scalar_subquery()
)
with Session(engine) as session:
    result = session.execute(
        insert(Address).values(user_id=scalar_subquery),
        [
            {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@squirrelpower.org"},
        ]
    )
    session.commit()


print("--- Updating ORM Objects ---")
with Session(engine) as session:
    sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
    print(sandy)   
    sandy.fullname="Sandy Squirrels"
    print ("sandy in session.dirty:", sandy in session.dirty)
    sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
    print(sandy.addresses)

    print("--- ORM-enabled UPDATE statements ---")
    session.execute(
        update(User).
        where(User.name == 'sandy').
        values(fullname='Sandy Squirrel Extraordinaire')
    )
    print(session.execute(select(User)).all())

    print("--- Deleting ORM Objects ---")
    patrick = session.get(User, 4)
    print(patrick)
    session.delete(patrick)
    print(session.execute(select(User)).all())

    # session.execute(select(User).where(User.name == "patrick")).first()
    # session.execute(delete(User).where(User.name == "sandy"))

    session.commit()
    #session.rollback()

    

