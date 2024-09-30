import reflex as rx

from . import *
from .layout_sidebar import *

def layout_navbar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.link(
                        rx.icon("map-pin"),
                        "MapLibre GL", size="1.825rem", fontWeight="900", href="https://maplibre.org/",
                        class_name="flex items-center gap-2 text-blue-100"
                    ),
                    rx.link(
                        " Reflex", size="1.825rem", fontWeight="900", color="white", href="/",
                    ),
                    class_name="flex items-center gap-2 text-white",
                ),
                rx.button(
                    rx.cond(SidebarState.sidebar_open, rx.box(), rx.icon("menu")),
                    on_click=SidebarState.open_sidebar(),
                    class_name="lg:invisible bg-transparent"
                ),
                class_name="max-w-6xl mx-auto h-full flex justify-between items-center px-4 md:max-w[100%]"
            ),
            class_name="fixed top-0 left-0 w-full h-10 bg-blue-500 z-40 lg:h-16",
        )
    )