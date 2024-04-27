from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models.models import Order
from src.utils.helpers import get_db

router = APIRouter()
order_service = ()


# @router.post("/orders/")
# def create_order(order: OrderCreate, db: Session = Depends(get_db)):
#     user = order_service.save_object(db, user_create)
#     return user

# @app.get("/orders/{order_id}")
# def read_order(order_id: int, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @app.put("/orders/{order_id}")
# def update_order(order_id: int, new_order: Order, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     # Update order attributes
#     for var, value in vars(new_order).items():
#         setattr(order, var, value)
#     db.commit()
#     db.refresh(order)
#     return order
#
#
# @app.delete("/orders/{order_id}")
# def delete_order(order_id: int, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if order is None:
#         raise HTTPException(status_code=404, detail="Order not found")
#     db.delete(order)
#     db.commit()
#     return {"message": "Order deleted successfully"}
