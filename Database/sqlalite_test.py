from sqlalchemy.orm import create_engine
# create a Session object to use Session class from sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

# Creating connection between alchemy and sql lite
engine = create_engine('sqlite:////web/Sqlite-Data/example4.db')
Session = sessionmaker(bind=engine)

session = Session()

# Inserting data
# Creating new customer objects

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )
c1, c2

