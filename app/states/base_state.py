import reflex as rx
from typing import TypedDict


class Category(TypedDict):
    name: str
    icon: str
    href: str


class BaseState(rx.State):
    """The base state for the app."""

    nav_links: list[dict[str, str]] = [
        {"name": "Início", "href": "/"},
        {"name": "Produtos", "href": "/products"},
        {"name": "Sobre Nós", "href": "/about"},
        {"name": "Contato", "href": "/contact"},
    ]
    categories: list[Category] = [
        {"name": "Calças", "icon": "trousers", "href": "/products?category=pants"},
        {"name": "Camisas", "icon": "shirt", "href": "/products?category=shirts"},
        {"name": "Camisolas", "icon": "user", "href": "/products?category=sweaters"},
        {"name": "Segurança", "icon": "hard-hat", "href": "/products?category=safety"},
        {"name": "Saias", "icon": "user-round", "href": "/products?category=skirts"},
        {"name": "Sapatos", "icon": "footprints", "href": "/products?category=shoes"},
        {"name": "Meias", "icon": "socks", "href": "/products?category=socks"},
    ]
    is_mobile_menu_open: bool = False

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open