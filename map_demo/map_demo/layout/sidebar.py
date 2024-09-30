import reflex as rx

# from . import *

titles = {
    "Introduction": "",
    "3D Terrain": "3d-terrain",
    "PMTiles source and protocol": "pmtiles",
    "Extrude polygons for 3D indoor mapping": "3d-extrusion-floorplan",
    "Display feature information on click": "feature-info-on-click",
    "Display a popup": "popup",
    "Add a default marker": "add-a-marker",
}


class SidebarState(rx.State):
    sidebar_open: bool = False

    def close_sidebar(self):
        self.sidebar_open = False

    def open_sidebar(self):
        self.sidebar_open = True

    @rx.var
    def current_url(self) -> str:
        return self.router.page.path


def render_example_page_links(title: dict) -> rx.Component:
    return rx.link(rx.text(title[0], fontSize="0.825rem",
                           color=rx.cond(SidebarState.current_url == f"/{title[1]}", "blue-300", "black")),
                   href=f"/{title[1]}")


def sidebar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("Examples", size="3", class_name="mb-4 font-medium fixed bg-white w-[218px] pt-6 -mt-6 pb-2"),
            rx.vstack(
                rx.foreach(titles, render_example_page_links),
                class_name="pt-10"
            ),
            class_name="fixed top-16 w-[260px] h-[calc(100vh-64px)] p-6 overflow-y-auto invisible lg:visible"
        ),
        mobile_sidebar()
    )


def render_example_page_links_mobile(title: dict) -> rx.Component:
    return rx.box(
        rx.link(
            rx.text(
                title[0],
                fontSize="0.825rem",
                color="black"
            ),
            href=f"/{title[1]}",
            class_name="p-4 w-full block"
        ),
        class_name=rx.cond(
            SidebarState.current_url == f"/{title[1]}",
            "block border-b w-full bg-blue-200 border-gray-300 hover:bg-blue-300 transition-colors duration-300 border",
            "block border-b w-full border-gray-300 hover:bg-blue-100 transition-colors duration-300 border"
        ),
        on_click=SidebarState.close_sidebar()
    )


def mobile_sidebar() -> rx.Component:
    return rx.box(
        rx.cond(
            SidebarState.sidebar_open,
            rx.box(
                rx.heading("Examples", size="3", class_name="h-10 p-2 pl-4 pr-4 font-medium bg-blue-600 lg:invisible"),
                rx.vstack(
                    rx.foreach(titles, render_example_page_links_mobile),
                    class_name="w-full flex gap-0"
                ),
                class_name=(
                    "fixed shadow-md left-0 top-0 h-full w-60 bg-gray-200 text-white z-50 "
                    "transition-transform duration-300 ease-out "
                    "translate-x-0 lg:invisible"
                ),
            ),
            rx.box(
                class_name=(
                    "fixed shadow-md left-0 top-0 h-full w-68 bg-gray-200 text-white z-50 "
                    "transition-transform duration-300 ease-in "
                    "-translate-x-full lg:invisible"
                )
            )
        ),
        rx.cond(
            SidebarState.sidebar_open,
            rx.box(
                on_click=SidebarState.close_sidebar(),
                class_name="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
            )
        ),
    )
