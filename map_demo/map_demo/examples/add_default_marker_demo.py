"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import Any, Dict
import reflex as rx
import reflex_map as rx_map

from ..layout import layout_container

def add_default_marker_demo() -> rx.Component:
    return layout_container(
        rx.box(
            rx.heading("Add a default marker", size="8", fontWeight="lighter"),
            rx.box(
                rx.text("Add a default marker to the map."),
                display="flex",
                flex_direction="column",
                gap="16px"
            ),
            rx.box(
                default_marker_map(),
            ),
            rx.code_block("""def default_marker_map() -> rx.Component:
    return map(
        marker(
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
        gap="48px"
        ),
        )


def default_marker_map() -> rx.Component:
    return rx_map.map(
        rx_map.marker(
            longitude=-96,
            latitude=37.8,
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