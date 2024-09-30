import reflex as rx

from . import *
from .sidebar import *

def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.hstack(
                    rx.link(
                        "Reflex Map",
                        size="2",
                        fontWeight="900",
                        color="white",
                        href="/",
                    ),
                    rx.spacer(),
                    rx.link(
                        rx.icon("map-pin"),
                        "React Map GL", size="2", fontWeight="500", href="https://visgl.github.io/react-map-gl/",
                        class_name="flex items-center gap-2 text-blue-100"
                    ),
                    rx.link(
                        " Reflex", size="2", fontWeight="500", color="white", href="https://reflex.dev/",
                    ),
                    class_name="flex items-center gap-2 text-white",
                    width="100%"
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