from sqlalchemy import (Column, ForeignKey, String, Table, DateTime, DECIMAL,
                        Text)
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(INTEGER)

    orders = relationship("Order", secondary="orders_products", back_populates="products")


class Order(Base):
    __tablename__ = "orders"

    id = Column(INTEGER, primary_key=True, index=True)
    delivery_address = Column(String)
    customer_name = Column(String)
    customer_email = Column(String)
    delivery_status = Column(String)
    created_at = Column(DateTime(),
                       server_default="CURRENT_TIMESTAMP",
                       nullable=False)

    customer_id = Column(INTEGER, ForeignKey("users.id"))
    customer = relationship("User", back_populates="orders")

    products = relationship("Product", secondary="orders_products", back_populates="orders")


class OrderProduct(Base):
    __tablename__ = "orders_products"

    order_id = Column(INTEGER, ForeignKey("orders.id"), primary_key=True)
    product_id = Column(INTEGER, ForeignKey("products.id"), primary_key=True)
