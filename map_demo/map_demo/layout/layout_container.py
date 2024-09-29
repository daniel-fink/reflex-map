import reflex as rx

from . import *

titles = {
    "Introduction": "",
    "3D Terrain": "3d-terrain",
    "PMTiles source and protocol": "pmtiles",
    "Extrude polygons for 3D indoor mapping": "3d-extrusion-floorplan",
    "Display feature information on click": "feature-info-on-click",
    "Display a popup": "popup",
    "Add a default marker": "add-a-marker",
}

class State(rx.State):
    @rx.var
    def current_url(self) -> str:
        return self.router.page.path

def render_example_page_links(title: dict) -> rx.Component:
    return rx.link(rx.text(title[0], fontSize="0.825rem", color=rx.cond(State.current_url == f"/{title[1]}", "red", "black")), href=f"/{title[1]}")


def layout_container(*children, **props) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.link("MapLibre GL Reflex", size="1.825rem", fontWeight="900", color="white", href="/"),
                class_name="max-w-6xl mx-auto h-full flex items-center px-4"
            ),
            class_name="fixed top-0 left-0 w-full h-16 bg-blue-500 z-50",
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.heading("Examples", size="3", class_name="mb-4 font-medium fixed bg-white w-[218px] pt-6 -mt-6 pb-1"),
                    rx.vstack(
                        rx.foreach(titles, render_example_page_links),
                        class_name="pt-8"
                    ),
                    class_name="fixed top-16 w-[260px] h-[calc(100vh-64px)] p-6 overflow-y-auto"
                ),
                rx.box(
                    *children,
                    class_name="flex-1 ml-[260px] h-[calc(100vh-64px)] p-6 pt-12 pb-12"
                ),
                class_name="flex"
            ),
            class_name="max-w-6xl mx-auto pt-16"
        ),
        class_name="relative"
    )