from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from requests import Session
from database import get_db
from services.product_services import ProductService

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


# get all
@router.get("/")
def get_product(db: Session = Depends(get_db)):
    service = ProductService(db)
    return {service.get_all()}


# get element by id
@router.get("/{product_id}")
def get_items(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    product = service.get_product(product_id)


    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# search product

@router.get("/search/")
def search_product(q:str,db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.search_product(q)

@router.get("/{product_id}/stock")
def get_stock(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return  service.check_product(product_id)

@router.get("/compatible/motherboard/")
def get_compatible_motherboard(cpu_socket:str,db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.check_compatible_motherboard(cpu_socket)