import reflex as rx

titles = {
    "3D Terrain": "3d-terrain",
    "PMTiles source and protocol": "pmtiles",
    "Extrude polygons for 3D indoor mapping": "3d-extrusion-floorplan",
    "Display feature information on click": "feature-info-on-click",
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

