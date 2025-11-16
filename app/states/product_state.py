import reflex as rx
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    description: str
    price: float
    images: list[str]
    category: str
    sizes: list[str]


PRODUCTS_DATA: list[Product] = [
    {
        "id": 1,
        "name": "Camisa Escolar Branca",
        "description": "Camisa de manga curta, 100% algodão, ideal para o dia a dia escolar.",
        "price": 550.0,
        "images": ["/placeholder.svg", "/placeholder.svg", "/placeholder.svg"],
        "category": "shirts",
        "sizes": ["6", "8", "10", "12", "14", "P", "M"],
    },
    {
        "id": 2,
        "name": "Calça Escolar Cinza",
        "description": "Calça resistente e confortável, com elástico na cintura para melhor ajuste.",
        "price": 850.0,
        "images": ["/placeholder.svg", "/placeholder.svg"],
        "category": "pants",
        "sizes": ["6", "8", "10", "12", "14"],
    },
    {
        "id": 3,
        "name": "Saia Plissada Azul Marinho",
        "description": "Saia escolar clássica com pregas, tecido de alta durabilidade.",
        "price": 750.0,
        "images": ["/placeholder.svg", "/placeholder.svg"],
        "category": "skirts",
        "sizes": ["P", "M", "G"],
    },
    {
        "id": 4,
        "name": "Camisola de Lã Azul",
        "description": "Camisola de lã para os dias mais frios, com decote em V.",
        "price": 1200.0,
        "images": ["/placeholder.svg"],
        "category": "sweaters",
        "sizes": ["10", "12", "14", "P", "M", "G"],
    },
    {
        "id": 5,
        "name": "Sapato Escolar Preto",
        "description": "Sapato de couro sintético, resistente e fácil de limpar.",
        "price": 1500.0,
        "images": ["/placeholdersvg", "/placeholder.svg"],
        "category": "shoes",
        "sizes": ["30", "32", "34", "36", "38", "40"],
    },
    {
        "id": 6,
        "name": "Meias Brancas (Par)",
        "description": "Par de meias de algodão, confortáveis para uso diário.",
        "price": 150.0,
        "images": ["/placeholder.svg"],
        "category": "socks",
        "sizes": ["Único"],
    },
    {
        "id": 7,
        "name": "Colete de Segurança",
        "description": "Colete refletor de alta visibilidade para segurança.",
        "price": 950.0,
        "images": ["/placeholder.svg"],
        "category": "safety",
        "sizes": ["M", "G", "XG"],
    },
]


class ProductState(rx.State):
    products: list[Product] = PRODUCTS_DATA
    selected_category: str = "all"
    product_detail: Product | None = None
    selected_image: str = ""
    selected_size: str = ""

    @rx.event
    def on_load_products(self):
        category = self.router.page.params.get("category", "all")
        self.selected_category = category

    @rx.event
    def set_selected_category(self, category: str):
        self.selected_category = category

    @rx.var
    def filtered_products(self) -> list[Product]:
        if self.selected_category == "all":
            return self.products
        return [p for p in self.products if p["category"] == self.selected_category]

    @rx.event
    def load_product(self):
        self.product_detail = None
        self.selected_size = ""
        product_id = self.router.page.params.get("product_id", "")
        if product_id.isdigit():
            found_product = next(
                (p for p in self.products if p["id"] == int(product_id)), None
            )
            self.product_detail = found_product
            if self.product_detail:
                self.selected_image = self.product_detail["images"][0]
                if self.product_detail["sizes"]:
                    self.selected_size = self.product_detail["sizes"][0]
        yield

    @rx.event
    def set_selected_image(self, image_url: str):
        self.selected_image = image_url

    @rx.event
    def set_selected_size(self, size: str):
        self.selected_size = size