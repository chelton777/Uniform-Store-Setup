import reflex as rx
from app.states.base_state import BaseState


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-600 hover:text-emerald-600 transition-colors duration-200 font-medium",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("shopping-bag", class_name="h-6 w-6 text-emerald-600"),
                    rx.el.span(
                        "Zero Graus Uniforme",
                        class_name="font-bold text-xl text-gray-800",
                    ),
                    class_name="flex items-center gap-2",
                ),
                href="/",
            ),
            rx.el.nav(
                rx.foreach(
                    BaseState.nav_links,
                    lambda link: nav_link(link["name"], link["href"]),
                ),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("menu", class_name="h-6 w-6 text-gray-600"),
                    on_click=BaseState.toggle_mobile_menu,
                    class_name="md:hidden",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between h-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        rx.cond(
            BaseState.is_mobile_menu_open,
            rx.el.div(
                rx.el.nav(
                    rx.foreach(
                        BaseState.nav_links,
                        lambda link: rx.el.a(
                            link["name"],
                            href=link["href"],
                            class_name="block py-2 px-4 text-sm text-gray-600 hover:bg-emerald-50 rounded-md",
                            on_click=BaseState.toggle_mobile_menu,
                        ),
                    ),
                    class_name="flex flex-col space-y-2 p-4",
                ),
                class_name="md:hidden bg-white shadow-lg rounded-b-lg",
            ),
            None,
        ),
        class_name="bg-white/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-100",
    )