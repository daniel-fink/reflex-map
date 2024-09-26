"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx

from .examples.terrain_demo import terrain_demo
from .examples.pmtiles_demo import pmtiles_demo
from .examples.extrude_3d_demo import extrude_3d_demo
from .examples.feature_info_on_click_demo import feature_info_on_click_demo
from .examples.display_popup_demo import display_popup_demo
from .examples.add_default_marker_demo import add_default_marker_demo

from .layout.topnav import topnav
from .layout.sidebar import sidebar
from .examples.default_demo import default_map

from .style import style

filename = f"{rx.config.get_config().app_name}/{rx.config.get_config().app_name}.py"

lib_dependencies: list[str] = ["react-map-gl"]
def add_imports(self):
    return {
        "react-syntax-highlighter": {rx.ImportVar(tag="PrismAsyncLight as SyntaxHighlighter")},
    }

def index() -> rx.Component:
    return rx.container(
        topnav(),
        rx.stack(
            sidebar(),
            rx.box(
                rx.heading("Introduction", size="8", fontWeight="lighter"),
                rx.box(
                    rx.link("MapLibre GL JS", href="https://maplibre.org/maplibre-gl-js/docs/"),
                    rx.box(" is a TypeScript library that uses WebGL to render interactive maps from vector tiles in a browser. The customization of the map complies with the ", display="inline"),
                    rx.link("MapLibre Style Spec", href="https://maplibre.org/maplibre-style-spec"),
                    rx.box(". It is part of the ", display="inline"),
                    rx.link("MapLibre ecosystem", href="https://github.com/maplibre"),
                    rx.box(", with a counterpart for Android, iOS, and other platforms called ", display="inline"),
                    rx.link("MapLibre Native", href="https://github.com/maplibre/maplibre-native"),
                    rx.box(".", display="inline")
                ),
                rx.box(
                    rx.text("Our Python integration of MapLibre is built on the powerful MapLibre GL JS library, which uses WebGL to render interactive maps from vector tiles directly in the browser."),
                    rx.text("With our Reflex-based solution, Python users can now fully customize maps using the same MapLibre Style Spec, offering precise control over map design and appearance."),
                    rx.text("This project brings the flexibility of MapLibre’s ecosystem—previously accessible primarily through JavaScript—into the hands of Python developers."),
                    rx.text("Just like MapLibre GL JS has its native counterparts for Android and iOS, our Reflex integration is tailored for Python, making high-performance mapping and geospatial visualization available to an even wider audience."),
                    display="flex",
                    flex_direction="column",
                    gap="16px"
                ),
                rx.box(
                    rx.heading("Quick Start", size="7", fontWeight="lighter"),
                    default_map(),
                    rx.box(
                        rx.text("Install the reflex-map via pip."),
                        rx.code("pip install reflex-map"),
                        rx.text("You can then import the reflex-map MapLibre GL module in your project."),
                        display="flex",
                        flex_direction="column",
                        gap="12px"
                    ),
                    rx.code_block("""def default_map() -> rx.Component:
    return map(
        source(
            layer(
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
        search_control(),
        navigation_control(),
        fullscreen_control(),

        initialViewState=dict(
            longitude=151.209900, latitude=-33.865143, zoom=10
        ),
    )"""),
                    display="flex",
                    flex_direction="column",
                    gap="48px",
                    width="100%"
                ),          
                display="flex",
                flex_direction="column",
                gap="48px"
            ),
            
            class_name="content",
        ),

        class_name="wrapper",
        size="4"
    )


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