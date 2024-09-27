"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx

from ..layout import sidebar, topnav
import reflex_map as rx_map



def extrude_3d_demo() -> rx.Component:
    return rx.container(
        topnav(),
        rx.stack(
            sidebar(),
            rx.box(
                rx.heading("Extrude polygons for 3D indoor mapping", size="8", fontWeight="lighter"),
                rx.box(
                    rx.text("Create a 3D indoor map with the fill-extrude-height paint property."),
                    display="flex",
                    flex_direction="column",
                    gap="16px"
                ),
                rx.box(
                    extrude_3d_map(),
                ),
                rx.code_block("""
def extrude_3d_map() -> rx.Component:
    return rx_map.map(
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
        rx_map.source(
            rx_map.layer(
                id="room-extrusion",
                type="fill-extrusion",
                paint={
                    "fill-extrusion-color": ["get", "color"],
                    "fill-extrusion-height": ["get", "height"],
                    "fill-extrusion-base": ["get", "base_height"],
                    "fill-extrusion-opacity": 0.5,
                },
                source="floorplan",
            ),
            type="geojson",
            id="floorplan",
            data="https://maplibre.org/maplibre-gl-js/docs/assets/indoor-3d-map.geojson",
        ),
        zoom=15.99,
        pitch=40,
        bearing=20,
        antialias=True,
        initialViewState=dict(
            longitude=-87.61694, latitude=41.86625, zoom=15.99,
            pitch=10
        ),
    )
                    """),
                display="flex",
                flex_direction="column",
                gap="48px",
                width="100%"
            ),
            class_name="content",
        ),

        class_name="wrapper",
        size="4"
    )


def extrude_3d_map() -> rx.Component:
    return rx_map.map(
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
        rx_map.source(
            rx_map.layer(
                id="room-extrusion",
                type="fill-extrusion",
                paint={
                    "fill-extrusion-color": ["get", "color"],
                    "fill-extrusion-height": ["get", "height"],
                    "fill-extrusion-base": ["get", "base_height"],
                    "fill-extrusion-opacity": 0.5,
                },
                source="floorplan",
            ),
            type="geojson",
            id="floorplan",
            data="https://maplibre.org/maplibre-gl-js/docs/assets/indoor-3d-map.geojson",
        ),
        zoom=15.99,
        pitch=40,
        bearing=20,
        antialias=True,
        initialViewState=dict(
            longitude=-87.61694, latitude=41.86625, zoom=15.99,
            pitch=10
        ),
    )