import reflex as rx
from app.states.base_state import BaseState
from app.states.contact_state import ContactState
from app.components.header import header
from app.components.footer import footer


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(class_name="absolute inset-0 bg-gray-900 opacity-60"),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Uniformes de Qualidade para um Futuro Brilhante",
                    class_name="text-4xl md:text-6xl font-extrabold text-white text-center tracking-tight",
                ),
                rx.el.p(
                    "Equipamos estudantes e profissionais com uniformes duráveis, confortáveis e com design moderno.",
                    class_name="mt-6 max-w-2xl mx-auto text-lg md:text-xl text-gray-200 text-center",
                ),
                rx.el.a(
                    "Ver Produtos",
                    href="/products",
                    class_name="mt-10 inline-block bg-emerald-500 text-white font-bold py-4 px-8 rounded-full shadow-lg hover:bg-emerald-600 transition-transform duration-300 ease-in-out transform hover:scale-105",
                ),
                class_name="relative z-10 flex flex-col items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32 md:py-48 flex items-center justify-center",
        ),
        style={
            "background_image": "url('/placeholder.svg')",
            "background_size": "cover",
            "background_position": "center",
        },
        class_name="relative bg-gray-50",
    )


def category_card(category: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(category["icon"], class_name="h-10 w-10 text-emerald-500 mb-4"),
            rx.el.h3(
                category["name"], class_name="text-lg font-semibold text-gray-800"
            ),
            class_name="flex flex-col items-center justify-center p-6",
        ),
        href=category["href"],
        class_name="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-shadow duration-300 ease-in-out border border-gray-100",
    )


def categories_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Nossas Categorias",
                class_name="text-3xl font-bold text-gray-900 text-center",
            ),
            rx.el.p(
                "Explore nossa vasta gama de uniformes para todas as necessidades.",
                class_name="mt-4 text-lg text-gray-600 text-center max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(BaseState.categories, category_card),
                class_name="mt-12 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-6",
            ),
            class_name="max-w-7xl mx-auto py-20 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50",
    )


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero_section(),
        categories_section(),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


from app.states.product_state import ProductState


def product_card(product: dict) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.image(
                src=product["images"][0],
                alt=product["name"],
                class_name="w-full h-48 object-cover rounded-t-xl",
            ),
            rx.el.div(
                rx.el.h3(
                    product["name"], class_name="font-semibold text-gray-800 truncate"
                ),
                rx.el.p(
                    f"{product['price']:.2f} MT",
                    class_name="text-emerald-600 font-bold mt-1",
                ),
                class_name="p-4",
            ),
        ),
        href=f"/product/{product['id']}",
        class_name="bg-white rounded-xl shadow-sm hover:shadow-xl transition-shadow duration-300 ease-in-out border border-gray-100 overflow-hidden flex flex-col",
    )


def products_page() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Nossos Produtos", class_name="text-4xl font-bold text-gray-900"
                ),
                rx.el.p(
                    "Encontre o uniforme perfeito para cada necessidade.",
                    class_name="text-lg text-gray-600 mt-2",
                ),
                class_name="text-center py-16 bg-gray-50",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        "Todos",
                        on_click=lambda: ProductState.set_selected_category("all"),
                        class_name=rx.cond(
                            ProductState.selected_category == "all",
                            "px-4 py-2 rounded-full font-medium bg-emerald-500 text-white shadow-md",
                            "px-4 py-2 rounded-full font-medium bg-white text-gray-700 hover:bg-gray-100",
                        ),
                    ),
                    rx.foreach(
                        BaseState.categories,
                        lambda cat: rx.el.button(
                            cat["name"],
                            on_click=lambda: ProductState.set_selected_category(
                                cat["href"].split("=")[1]
                            ),
                            class_name=rx.cond(
                                ProductState.selected_category
                                == cat["href"].split("=")[1],
                                "px-4 py-2 rounded-full font-medium bg-emerald-500 text-white shadow-md",
                                "px-4 py-2 rounded-full font-medium bg-white text-gray-700 hover:bg-gray-100",
                            ),
                        ),
                    ),
                    class_name="flex flex-wrap items-center justify-center gap-4 mb-12",
                ),
                rx.el.div(
                    rx.foreach(ProductState.filtered_products, product_card),
                    class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 lg:gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
        ),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


def product_detail_page() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.div(
            rx.el.h1("TEST PRODUCT"),
            rx.cond(
                ProductState.product_detail,
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src=ProductState.selected_image,
                            alt=ProductState.product_detail["name"],
                            class_name="w-full h-auto object-cover rounded-xl shadow-lg",
                        ),
                        rx.el.div(
                            rx.foreach(
                                ProductState.product_detail["images"],
                                lambda img: rx.el.button(
                                    rx.image(
                                        src=img,
                                        class_name="h-16 w-16 object-cover rounded-md",
                                    ),
                                    on_click=lambda: ProductState.set_selected_image(
                                        img
                                    ),
                                    class_name=rx.cond(
                                        ProductState.selected_image == img,
                                        "border-2 border-emerald-500 rounded-lg p-1",
                                        "p-1 opacity-75 hover:opacity-100",
                                    ),
                                ),
                            ),
                            class_name="flex gap-2 mt-4",
                        ),
                        class_name="w-full lg:w-1/2",
                    ),
                    rx.el.div(
                        rx.el.h1(
                            ProductState.product_detail["name"],
                            class_name="text-4xl font-bold text-gray-900",
                        ),
                        rx.el.p(
                            ProductState.product_detail["price"].to(str) + " MT",
                            class_name="text-3xl text-emerald-600 font-semibold my-4",
                        ),
                        rx.el.p(
                            ProductState.product_detail["description"],
                            class_name="text-gray-600 leading-relaxed",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Tamanho:",
                                class_name="font-semibold text-gray-800 mb-2 block",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    ProductState.product_detail["sizes"],
                                    lambda size: rx.el.button(
                                        size,
                                        on_click=lambda: ProductState.set_selected_size(
                                            size
                                        ),
                                        class_name=rx.cond(
                                            ProductState.selected_size == size,
                                            "px-4 py-2 border rounded-md border-emerald-500 bg-emerald-50 ring-2 ring-emerald-200 text-emerald-800 font-semibold",
                                            "px-4 py-2 border rounded-md hover:border-emerald-500 hover:bg-emerald-50 text-gray-700",
                                        ),
                                    ),
                                ),
                                class_name="flex flex-wrap gap-2",
                            ),
                            class_name="mt-6",
                        ),
                        rx.el.button(
                            rx.icon("shopping-cart", class_name="mr-2"),
                            "Adicionar ao Carrinho",
                            class_name="mt-8 w-full flex items-center justify-center bg-emerald-500 text-white font-bold py-4 px-8 rounded-full shadow-lg hover:bg-emerald-600 transition-transform duration-300 ease-in-out transform hover:scale-105",
                        ),
                        class_name="w-full lg:w-1/2 lg:pl-12 pt-8 lg:pt-0",
                    ),
                    class_name="flex flex-col lg:flex-row gap-8 lg:gap-16",
                ),
                rx.el.div(
                    rx.el.p(
                        "A carregar detalhes do produto...",
                        class_name="text-center text-gray-500 text-xl",
                    ),
                    class_name="flex items-center justify-center h-full",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 min-h-[50vh] flex items-center justify-center",
        ),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


def about_us_page() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Sobre a Zero Graus Uniforme",
                        class_name="text-4xl md:text-5xl font-extrabold text-gray-900",
                    ),
                    rx.el.p(
                        "Vestindo o futuro de Moçambique com qualidade e orgulho.",
                        class_name="mt-4 text-xl text-gray-600",
                    ),
                    class_name="text-center",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Nossa História",
                            class_name="text-3xl font-bold text-gray-800 mb-4",
                        ),
                        rx.el.p(
                            "Fundada com a paixão por fornecer uniformes de alta qualidade, a Zero Graus Uniforme nasceu da necessidade de vestir estudantes e profissionais com conforto, durabilidade e estilo. Desde o início, nosso compromisso tem sido com a excelência, desde a escolha dos tecidos até o acabamento final de cada peça.",
                            class_name="text-gray-600 leading-relaxed mb-4",
                        ),
                        rx.el.p(
                            "Com o passar dos anos, expandimos nossa linha de produtos para atender a uma variedade de setores, sempre mantendo nosso padrão de qualidade e atenção aos detalhes. Acreditamos que um bom uniforme pode inspirar confiança e profissionalismo, e é essa crença que nos move todos os dias.",
                            class_name="text-gray-600 leading-relaxed",
                        ),
                        class_name="md:w-1/2",
                    ),
                    rx.el.div(
                        rx.image(
                            src="/placeholder.svg",
                            class_name="rounded-2xl shadow-lg w-full h-full object-cover",
                        ),
                        class_name="md:w-1/2 mt-8 md:mt-0",
                    ),
                    class_name="flex flex-col md:flex-row gap-12 items-center mt-16",
                ),
                class_name="max-w-7xl mx-auto py-20 px-4 sm:px-6 lg:px-8",
            )
        ),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


def contact_page() -> rx.Component:
    return rx.el.main(
        header(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Entre em Contato",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 text-center",
                ),
                rx.el.p(
                    "Estamos aqui para ajudar. Envie-nos uma mensagem!",
                    class_name="mt-4 text-xl text-gray-600 text-center",
                ),
                class_name="py-16 bg-gray-50",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Informações de Contato",
                        class_name="text-2xl font-bold text-gray-800 mb-6",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon(
                                "phone", class_name="mr-3 h-5 w-5 text-emerald-600"
                            ),
                            "+258 84 830 4000",
                            href="tel:+258848304000",
                            class_name="flex items-center text-lg text-gray-700 hover:text-emerald-700",
                        ),
                        rx.el.a(
                            rx.icon(
                                "message-circle",
                                class_name="mr-3 h-5 w-5 text-emerald-600",
                            ),
                            "WhatsApp",
                            href="https://wa.me/258848304000",
                            target="_blank",
                            class_name="flex items-center text-lg text-gray-700 hover:text-emerald-700",
                        ),
                        rx.el.div(
                            rx.icon(
                                "map-pin", class_name="mr-3 h-5 w-5 text-emerald-600"
                            ),
                            rx.el.span("N4, Maputo, Moçambique"),
                            class_name="flex items-center text-lg text-gray-700",
                        ),
                        class_name="space-y-4",
                    ),
                    class_name="lg:w-1/3",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Nome Completo",
                            html_for="name",
                            class_name="font-medium text-gray-700",
                        ),
                        rx.el.input(
                            id="name",
                            name="name",
                            placeholder="Seu Nome",
                            class_name="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        rx.cond(
                            ContactState.form_errors.contains("name"),
                            rx.el.p(
                                ContactState.form_errors["name"],
                                class_name="text-red-500 text-sm mt-1",
                            ),
                            None,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email",
                            html_for="email",
                            class_name="font-medium text-gray-700",
                        ),
                        rx.el.input(
                            id="email",
                            name="email",
                            type="email",
                            placeholder="seu@email.com",
                            class_name="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        rx.cond(
                            ContactState.form_errors.contains("email"),
                            rx.el.p(
                                ContactState.form_errors["email"],
                                class_name="text-red-500 text-sm mt-1",
                            ),
                            None,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Mensagem",
                            html_for="message",
                            class_name="font-medium text-gray-700",
                        ),
                        rx.el.textarea(
                            id="message",
                            name="message",
                            placeholder="Como podemos ajudar?",
                            rows=4,
                            class_name="mt-1 w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-emerald-500 focus:border-emerald-500",
                        ),
                        rx.cond(
                            ContactState.form_errors.contains("message"),
                            rx.el.p(
                                ContactState.form_errors["message"],
                                class_name="text-red-500 text-sm mt-1",
                            ),
                            None,
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        rx.cond(
                            ContactState.is_submitting,
                            rx.el.span("Enviando...", class_name="flex items-center"),
                            rx.el.span("Enviar Mensagem"),
                        ),
                        type="submit",
                        disabled=ContactState.is_submitting,
                        class_name="w-full bg-emerald-500 text-white font-bold py-3 px-6 rounded-full shadow-lg hover:bg-emerald-600 transition-colors duration-300 disabled:bg-gray-400",
                    ),
                    on_submit=ContactState.handle_submit,
                    reset_on_submit=False,
                    class_name="lg:w-2/3 bg-white p-8 rounded-xl shadow-md border border-gray-200",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 flex flex-col lg:flex-row gap-12 lg:gap-24",
            ),
        ),
        footer(),
        class_name="font-['Poppins'] bg-white",
    )


def floating_whatsapp_button() -> rx.Component:
    return rx.el.a(
        rx.icon("message-circle", class_name="h-8 w-8 text-white"),
        href="https://wa.me/258848304000",
        target="_blank",
        class_name="fixed bottom-8 right-8 bg-emerald-500 p-4 rounded-full shadow-lg hover:bg-emerald-600 transition-transform duration-300 transform hover:scale-110 z-50",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)


def page_with_layout(component: rx.Component) -> rx.Component:
    return rx.el.div(component, floating_whatsapp_button())


app.add_page(lambda: page_with_layout(index()), route="/")
app.add_page(
    lambda: page_with_layout(products_page()),
    route="/products",
    on_load=ProductState.on_load_products,
)
app.add_page(
    lambda: page_with_layout(product_detail_page()),
    route="/product/[product_id]",
    on_load=ProductState.load_product,
)
app.add_page(lambda: page_with_layout(about_us_page()), route="/about")
app.add_page(lambda: page_with_layout(contact_page()), route="/contact")