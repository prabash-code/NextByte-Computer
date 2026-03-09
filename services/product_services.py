from repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self,db):
        self.repo=ProductRepository(db)

    def get_all(self):
        return self.repo.get_all()

    def get_product(product_id,self):
        return self.repo.get_product(product_id)

    def search_product(quary:str,self):
        return self.repo.search_product(quary)


    def  check_product(product_id: int,self):
        return self.repo.check_stock(product_id)
        if stock is None:
            return {"available": False, "stock": 0}
        return {"available": stock > 0, "stock": stock}

    def check_compatible_motherboard(cpu_socket:str,self):
        return self.repo.check_compatible_motherboard(cpu_socket)