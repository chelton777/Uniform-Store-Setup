import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        "Zero Graus Uniforme",
                        href="/",
                        class_name="text-xl font-bold text-emerald-600",
                    ),
                    rx.el.p(
                        "Qualidade e conforto para o seu dia a dia escolar e profissional.",
                        class_name="mt-2 text-sm text-gray-500",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3("Links", class_name="font-semibold text-gray-900"),
                        rx.el.ul(
                            rx.el.li(
                                rx.el.a(
                                    "Início",
                                    href="/",
                                    class_name="hover:text-emerald-600",
                                )
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Produtos",
                                    href="/products",
                                    class_name="hover:text-emerald-600",
                                )
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Sobre Nós",
                                    href="/about",
                                    class_name="hover:text-emerald-600",
                                )
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Contato",
                                    href="/contact",
                                    class_name="hover:text-emerald-600",
                                )
                            ),
                            class_name="space-y-2 mt-4 text-gray-600",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3("Contato", class_name="font-semibold text-gray-900"),
                        rx.el.ul(
                            rx.el.li(
                                rx.el.a(
                                    rx.icon("phone", class_name="mr-2 h-4 w-4"),
                                    "+258 848304000",
                                    href="tel:+258848304000",
                                    class_name="flex items-center hover:text-emerald-600",
                                )
                            ),
                            rx.el.li(
                                rx.el.a(
                                    rx.icon(
                                        "message-circle", class_name="mr-2 h-4 w-4"
                                    ),
                                    "WhatsApp",
                                    href="https://wa.me/258848304000",
                                    target="_blank",
                                    class_name="flex items-center hover:text-emerald-600",
                                )
                            ),
                            rx.el.li(
                                rx.el.div(
                                    rx.icon("map-pin", class_name="mr-2 h-4 w-4"),
                                    "N4, Maputo, Moçambique",
                                    class_name="flex items-center",
                                )
                            ),
                            class_name="space-y-2 mt-4 text-gray-600",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-8",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 Zero Graus Uniforme. Todos os direitos reservados.",
                    class_name="text-sm text-gray-500",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.icon(
                            "facebook", class_name="h-5 w-5 hover:text-emerald-600"
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon(
                            "instagram", class_name="h-5 w-5 hover:text-emerald-600"
                        ),
                        href="#",
                    ),
                    rx.el.a(
                        rx.icon("twitter", class_name="h-5 w-5 hover:text-emerald-600"),
                        href="#",
                    ),
                    class_name="flex space-x-4 text-gray-500",
                ),
                class_name="mt-8 pt-8 border-t border-gray-200 flex justify-between items-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50",
    )