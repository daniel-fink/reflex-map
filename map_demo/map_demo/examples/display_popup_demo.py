"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
import reflex_map as rx_map

from ..layout import layout_container

def display_popup_demo() -> rx.Component:
    return layout_container(
        "Display a popup",
        rx.text("Add a popup to the map."),
        rx.box(
            display_a_popup_map()
        ),
        rx.code_block("""def display_a_popup_map() -> rx.Component:
    return map(
        popup(
            rx.html("<h1>Hello World!</h1>"),
            longitude=-96,
            latitude=37.8,
            closeButton=True,
        ),
        rx_map.source(
            rx_map.layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            rx_map.layer(
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
    )""")
    ),


def display_a_popup_map() -> rx.Component:
    return rx_map.map(
        rx_map.popup(
            rx.html("<h1>Hello World!</h1>"),
            longitude=-96.324,
            latitude=37.8,
            closeButton=True,
        ),
        rx_map.source(
            rx_map.layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            rx_map.layer(
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
