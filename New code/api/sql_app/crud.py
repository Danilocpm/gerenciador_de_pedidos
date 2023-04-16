from sqlalchemy.orm import Session
from typing import List

from . import models, schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    for var, value in vars(product).items():
        if value is not None:
            setattr(db_product, var, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db.query(models.Product).filter(models.Product.id == product_id).delete()
    db.commit()


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    for var, value in vars(order).items():
        if value is not None:
            setattr(db_order, var, value)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    db.query(models.Order).filter(models.Order.id == order_id).delete()
    db.commit()


def add_product_to_order(db: Session, order_id: int, product_id: int, quantity: int):
    order_product = models.OrderProduct(order_id=order_id, product_id=product_id, quantity=quantity)
    db.add(order_product)
    db.commit()
    db.refresh(order_product)
    return order_product


def remove_product_from_order(db: Session, order_product_id: int):
    db.query(models.OrderProduct).filter(models.OrderProduct.id == order_product_id).delete()
    db.commit()


def get_order_products(db: Session, order_id: int) -> List[schemas.OrderProduct]:
    order_products = db.query(models.OrderProduct).filter(models.OrderProduct.order_id == order_id).all()
    return [schemas.OrderProduct.from_orm(order_product) for order_product in order_products]
