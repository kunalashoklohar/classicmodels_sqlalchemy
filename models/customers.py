# from typing import Text
from sqlalchemy import create_engine,Column,String,Integer,Text,SmallInteger
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import Date, Float ,SMALLINT , BLOB
# from sqlalchemy.dialects import mysql

Base  = declarative_base()

SQl_URI = "mysql+pymysql://root:root@localhost/classicmodels"
engine = create_engine(SQl_URI,echo = True)

class Customers(Base):
    __tablename__ = 'customers'

    customerNumber = Column(Integer, primary_key=True , nullable=False)
    customerName = Column(String(50))
    contactLastName = Column(String(50))
    contactFirstName = Column(String(50))
    phone = Column(String(50))
    addressLine1 = Column(String(50))
    addressLine2 = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50))
    salesRepEmployeeNumber = Column(Integer)
    creditLimit = Column(Float(10,2))

    def __repr__(self) -> str:
        return str(self.customerNumber)  + " " + self.customerName  + " " + self.contactFirstName + " " + self.contactLastName +"@" + self.addressLine1


    def my_total(self):
        return 100    




class ProductLines(Base):
    __tablename__ = 'productlines'

    productLine = Column(String(50), primary_key=True , nullable=False)
    textDescription = Column(String(50))
    htmlDescription = Column(String(50))
    image = Column(BLOB(50))
 
class Products(Base):
    __tablename__ = 'products'
     
    
    productCode = Column(String(15), primary_key=True , nullable=False)
    productName = Column(String(70))
    productLine = Column(String(50))
    productScale = Column(String(10))
    productVendor = Column(String(50))
    productDescription = Column(Text)
    quantityInStock = Column(SmallInteger)
    buyPrice = Column(Float(10,2))
    MSRP = Column(Float(10,2))
    


class Orders(Base):
    __tablename__ = 'orders'

    orderNumber = Column(Integer, primary_key=True , nullable=False)
    orderDate = Column(Date)
    requiredDate = Column(Date)
    shippedDate = Column(Date)
    status = Column(String(15))
    comments = Column(Text)
    customerNumber = Column(Integer)
    
    def get_order_total():
        return 100
    

class OrderDetails(Base):
    __tablename__ = 'orderdetails'

    orderNumber = Column(Integer, primary_key=True , nullable=False)
    productCode = Column(String(15),primary_key=True,nullable=True)
    quantityOrdered = Column(SmallInteger)
    priceEach = Column(Float(10,20))
    orderLineNumber = Column(String(15))
     

class Payments(Base):
    __tablename__ = 'payments'

    customerNumber = Column(Integer, primary_key=True , nullable=False)
    checkNumber = Column(String(50),primary_key=True,nullable=True)
    paymentDate = Column(Date)
    amount = Column(Float(10,20))
  

class Employees(Base):
    __tablename__ = 'employees'

    employeeNumber = Column(Integer, primary_key=True , nullable=False)
    lastName = Column(String(50))
    firstName = Column(String(50))
    extension = Column(String(10))
    email = Column(String(100))
    officeCode = Column(String(10))
    reportsTo = Column(Integer)
    jobTitle = Column(String(50))
   

class Offfices(Base):
    __tablename__ = 'offices'

    officeCode = Column(String(10), primary_key=True , nullable=False)
    city = Column(String(50))
    phone = Column(String(50))
    addressLine1 = Column(String(50))
    addressLine2 = Column(String(50))
    state = Column(String(50))
    country = Column(String(50))
    postalCode = Column(String(15))
    territory = Column(String(10))
    

print("creating tables in the db::")
Base.metadata.create_all(engine)



# SELECT *
# FROM customers