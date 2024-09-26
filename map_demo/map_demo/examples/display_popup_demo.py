"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import Any, Dict
import reflex as rx

from ..layout import sidebar, topnav
from reflex_map import map
from reflex_map import source
from reflex_map import layer
from reflex_map import popup

def display_popup_demo() -> rx.Component:
    return rx.container(
        topnav(),
        rx.stack(
            sidebar(),
            rx.box(
                rx.heading("Display a popup", size="8", fontWeight="lighter"),
                rx.box(
                    rx.text("Add a popup to the map."),
                    display="flex",
                    flex_direction="column",
                    gap="16px"
                ),
                rx.box(
                    display_a_popup_map(),
                ),
                rx.code_block("""def display_a_popup_map() -> rx.Component:
    return map(
        popup(
            rx.html("<h1>Hello World!</h1>"),
            longitude=-96,
            latitude=37.8,
            closeButton=True,
        ),
        source(
            layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            layer(
                id="simple-tiles",
                type="raster",
                source="raster-tiles",
            ),
            type="raster",
            id="raster-tiles",
            tiles=["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap",
            tileSize=256,
            minzoom=0,
            maxzoom=19,
        ),

        initialViewState=dict(
            longitude=-96, latitude= 37.8, zoom=3
        ),
    )"""),
                display="flex",
                flex_direction="column",
                gap="48px",
                width="100%"
                
            ),
            style={"position": "relative"},
            class_name="content",
        ),

        class_name="wrapper",
        size="4"
    )


def display_a_popup_map() -> rx.Component:
    return map(
        popup(
            rx.html("<h1>Hello World!</h1>"),
            longitude=-96,
            latitude=37.8,
            closeButton=True,
        ),
        source(
            layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            layer(
                id="simple-tiles",
                type="raster",
                source="raster-tiles",
            ),
            type="raster",
            id="raster-tiles",
            tiles=["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap",
            tileSize=256,
            minzoom=0,
            maxzoom=19,
        ),

        initialViewState=dict(
            longitude=-96, latitude= 37.8, zoom=3
        ),
    )