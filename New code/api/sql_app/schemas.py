from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    product_id: int
    customer_name: str
    customer_email: str
    shipping_address: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True

class OrderProductBase(BaseModel):
    order_id: int
    product_id: int


class OrderProductCreate(OrderProductBase):
    pass


class OrderProduct(OrderProductBase):
    class Config:
        orm_mode = True


class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderInDBBase(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True


class OrderProductInDBBase(OrderProductBase):
    id: int
    order_id: int
    product_id: int

    class Config:
        orm_mode = True


class ProductInDB(ProductInDBBase):
    class Config:
        orm_mode = True


class OrderInDB(OrderInDBBase):
    class Config:
        orm_mode = True


class OrderProductInDB(OrderProductInDBBase):
    class Config:
        orm_mode = True