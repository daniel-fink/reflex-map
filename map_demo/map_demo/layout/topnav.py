import reflex as rx

def topnav() -> rx.Component:
    return rx.container(
        rx.link("MapLibre GL Reflex", size="1.825rem", color="white", href="/"),
        class_name="topNav",
        size="4"
    ),