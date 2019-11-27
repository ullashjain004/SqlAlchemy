from sqlalchemy.orm import create_engine
# create a Session object to use Session class from sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

# Creating connection between alchemy and sql lite 
engine = create_engine('sqlite:////web/Sqlite-Data/example4.db')
Session = sessionmaker(bind=engine)

session = Session()

