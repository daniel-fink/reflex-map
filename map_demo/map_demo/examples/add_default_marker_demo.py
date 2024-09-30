import reflex as rx
import reflex_map as rx_map

from .. import layout

def add_default_marker_demo():
    return layout.container(
        "Add a default marker",
        rx.text("Add a default marker to the map."),
        rx.box(
            default_marker_map()
        ),
        rx.code_block("""
def default_marker_map() -> rx.Component:
    return rx_map.map(
        rx_map.marker(
            longitude=-96.123456,
            latitude=37.845678,
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
        """)
    )


def default_marker_map() -> rx.Component:
    return rx_map.map(
        rx_map.marker(
            longitude=-96.123456,
            latitude=37.845678,
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
