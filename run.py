
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from models.customers import Orders, ProductLines, Payments, Products, Customers, OrderDetails, Employees, Offfices, engine

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

result = session.query(Customers)

# print(dir(session))

print("--------------------Customers----------------")

print(dir(result))
print(result)
# for r in result:
#     print(r)
