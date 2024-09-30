import reflex as rx

from . import *
from .layout_sidebar import *
from .layout_navbar import *

def layout_container(title, *children, **props) -> rx.Component:
    return rx.box(
        layout_navbar(),
        rx.box(
            rx.box(
                layout_sidebar(),
                rx.box(
                    rx.box(
                        rx.heading(title, class_name="text-xl lg:text-3xl"),
                        *children,
                        rx.link(
                            rx.callout(
                                "Disclaimer: This project is not affiliated with or endorsed by MapLibre GL. It is an independent, open-source integration into the Reflex framework. For the official version, please visit the MapLibre website.",
                                icon="info",
                                variant="outline"
                            ),
                            href="https://maplibre.org/",
                        ),
                        class_name="flex flex-col gap-6 w-full lg:gap-12 text-sm pb-6 lg:text-base"
                    ),
                    class_name="flex-1 h-[calc(100vh-64px)] p-4 pl-6 pr-6 lg:ml-[260px] lg:pt-12 lg:pb-12 lg:p-6"
                ),
                class_name="flex"
            ),
            class_name="max-w-6xl mx-auto pt-14 lg:pt-16"
        ),
        class_name="relative"
    )