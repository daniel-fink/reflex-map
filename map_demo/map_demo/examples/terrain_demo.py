"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx

from ..layout import sidebar, topnav
from reflex_map import map
from reflex_map import source
from reflex_map import layer
from reflex_map import terrain_control


def terrain_demo() -> rx.Component:
    return rx.container(
        topnav(),
        rx.stack(
            sidebar(),
            rx.box(
                rx.heading("Terrain", size="8", fontWeight="lighter"),
                rx.box(
                    rx.text("Go beyond hillshade and show elevation in actual 3D."),
                    display="flex",
                    flex_direction="column",
                    gap="16px"
                ),
                rx.box(
                    terrain_map(),
                ),
                rx.code_block("""def terrain_map() -> rx.Component:
    return map(
        terrain_control(),
        source(
            layer(
                source="osm",
                type="raster",
            ),
            type="raster",
            title="OpenStreetMap",
            id="osm",
            tileSize=256,
            tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap Contributors",
            maxzoom=19
        ),
        source(
            layer(
                source="hillshade",
                type="hillshade",
                paint={"hillshade-shadow-color": "#473B24"},
            ),
            id="hillshade",
            type="raster-dem",
            url="https://demotiles.maplibre.org/terrain-tiles/tiles.json",
            tileSize=256,
        ),
        source(
            id="terrain",
            type="raster-dem",
            url="https://demotiles.maplibre.org/terrain-tiles/tiles.json",
            tileSize=256,
        ),
        terrain={"source": "terrain", "exaggeration": 1},
        zoom=12,
         initialViewState=dict(
            longitude=11.39085, latitude=47.27574, zoom=12, pitch=70
        ),
    )"""),
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


def terrain_map() -> rx.Component:
    return map(
        terrain_control(),
        source(
            layer(
                source="osm",
                type="raster",
            ),
            type="raster",
            title="OpenStreetMap",
            id="osm",
            tileSize=256,
            tiles=["https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap Contributors",
            maxzoom=19
        ),
        source(
            layer(
                source="hillshade",
                type="hillshade",
                paint={"hillshade-shadow-color": "#473B24"},
            ),
            id="hillshade",
            type="raster-dem",
            url="https://demotiles.maplibre.org/terrain-tiles/tiles.json",
            tileSize=256,
        ),
        source(
            id="terrain",
            type="raster-dem",
            url="https://demotiles.maplibre.org/terrain-tiles/tiles.json",
            tileSize=256,
        ),
        terrain={"source": "terrain", "exaggeration": 1},
        zoom=12,
        initialViewState=dict(
            longitude=11.39085, latitude=47.27574, zoom=12, pitch=70
        ),
    )