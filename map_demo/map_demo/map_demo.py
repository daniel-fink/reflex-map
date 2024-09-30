"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx

from .examples import *
from .layout import *
from .style import *

filename = f"{rx.config.get_config().app_name}/{rx.config.get_config().app_name}.py"

lib_dependencies: list[str] = ["react-map-gl"]
def add_imports(self):
    return {
        "react-syntax-highlighter": {rx.ImportVar(tag="PrismAsyncLight as SyntaxHighlighter")},
    }

def index():
    return layout.container(
        "Introduction",
        # rx.link(
        #     rx.callout(
        #         "Disclaimer: This project is not affiliated with or endorsed by MapLibre GL. It is an independent, open-source integration into the Reflex framework. For the official version, please visit the MapLibre website.",
        #         icon="info",
        #         variant="outline"
        #     ),
        #     href="https://maplibre.org",
        # ),
        rx.box(
            rx.box(
                "Reflex Map is a wrapper of ",
                rx.link("React-Map-GL", href="https://visgl.github.io/react-map-gl/"),
                " in ",
                rx.link("Reflex", href="https://reflex.dev/"),
                ".",
            ),
            rx.box(
                "It surfaces components from React-Map-GL, like ",
                rx.link("Markers", href="https://visgl.github.io/react-map-gl/docs/api-reference/marker"),
                " and ",
                rx.link("Popups", href="https://visgl.github.io/react-map-gl/docs/api-reference/popup"),
                " for use in Reflex apps.",
            )
        ),
        rx.box(
            rx.heading("Quick Start", class_name="text-lg lg:text-2xl"),
            default_map(),
            rx.box(
                rx.text("Install the reflex-map via pip."),
                rx.code("pip install reflex-map"),
                rx.text("You can then import the reflex-map MapLibre GL module in your project."),
                display="flex",
                flex_direction="column",
                gap="12px"
            ),
            rx.code_block("""
def reflex_map() -> rx.Component:
    return rx_map.map(
        rx_map.source(
            rx_map.layer(
                source="google_maps",
                type="raster",
            ),
            type="raster",
            title="Google Maps",
            id="google_maps",
            tileSize=256,
            tiles=["https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"],
            attribution="&copy; Google Maps"
        ),
        rx_map.search_control(),
        rx_map.navigation_control(),
        rx_map.fullscreen_control(),

        initialViewState=dict(
            longitude=151.209900, latitude=-33.865143, zoom=10
        ),
    )
        """),
            class_name="flex flex-col gap-6 w-full lg:gap-12"
        ),          
  
    ),


# Add state and page to the app.
app = rx.App(style=style)
app.add_page(index)
app.add_page(index, "/", "Home")
app.add_page(terrain_demo, "/3d-terrain", "3D Terrain")
app.add_page(pmtiles_demo, "/pmtiles", "PMTiles source and protocol")
app.add_page(extrude_3d_demo, "/3d-extrusion-floorplan", "Extrude polygons for 3D indoor mapping")
app.add_page(feature_info_on_click_demo, "/feature-info-on-click", "Display feature information on click")
app.add_page(display_popup_demo, "/popup", "Display a popup")
app.add_page(add_default_marker_demo, "/add-a-marker", "Add a default marker")