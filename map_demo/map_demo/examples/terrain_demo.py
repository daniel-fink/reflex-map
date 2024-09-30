"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
import reflex_map as rx_map

from ..layout import layout_container

def terrain_demo() -> rx.Component:
    return layout_container(
        "Terrain",
        rx.text("Go beyond hillshade and show elevation in actual 3D."),
        rx.box(
            terrain_map()
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
    )


def terrain_map() -> rx.Component:
    return rx_map.map(
        rx_map.terrain_control(),
        rx_map.source(
            rx_map.layer(
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
        rx_map.source(
            rx_map.layer(
                source="hillshade",
                type="hillshade",
                paint={"hillshade-shadow-color": "#473B24"},
            ),
            id="hillshade",
            type="raster-dem",
            url="https://demotiles.maplibre.org/terrain-tiles/tiles.json",
            tileSize=256,
        ),
        rx_map.source(
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