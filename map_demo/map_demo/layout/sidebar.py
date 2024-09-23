import reflex as rx

titles = {
    "Terrain": "terrain",
}
def render_example_page_links(title: dict) -> rx.Component:
    return rx.link(rx.text(title[0], fontSize="0.825rem"), href=f"/{title[1]}")


def sidebar() -> rx.Component:
    return rx.box(
            rx.heading("Examples", size="3", marginBottom="16px", fontWeight="lighter"),
            rx.vstack(
                rx.link(rx.text("Introduction", fontSize="0.825rem"), href="/"),
                rx.foreach(titles, render_example_page_links)
            ),
            class_name="sidebar",
    )