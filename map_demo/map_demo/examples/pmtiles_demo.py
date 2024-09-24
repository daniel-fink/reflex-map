"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx

from ..layout import sidebar, topnav
from reflex_map import map
from reflex_map import source
from reflex_map import layer


def pmtiles_demo() -> rx.Component:
    return rx.container(
        topnav(),
        rx.stack(
            sidebar(),
            rx.box(
                rx.heading("PMTiles", size="8", fontWeight="lighter"),
                rx.box(
                    rx.text("Uses the PMTiles plugin and protocol to present a map."),
                    display="flex",
                    flex_direction="column",
                    gap="16px"
                ),
                rx.box(
                    pmtiles_map(),
                ),
                rx.code_block("""def pmtiles_map() -> rx.Component:
    return map(
        source(
            layer(
                id="buildings",
                type="fill",
                paint={ "fill-color": "black" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="roads",
                type="line",
                paint={ "line-color": "black" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="boundaries",
                type="line",
                paint={ "line-color": "black", "line-width": 2 },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="water",
                type="fill",
                paint={ "fill-color": "blue" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            type="vector",
            id="example_source",
            url="pmtiles://https://data.source.coop/protomaps/openstreetmap/tiles/v3.pmtiles",
        ),
        zoom=12,
         initialViewState=dict(
            longitude=-122.5727462, latitude=37.9677487, zoom=13
        ),
        mapStyle="https://tiles.stadiamaps.com/styles/alidade_smooth.json",
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


def pmtiles_map() -> rx.Component:
    return map(
        source(
            layer(
                id="buildings",
                type="fill",
                paint={ "fill-color": "black" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="roads",
                type="line",
                paint={ "line-color": "black" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="boundaries",
                type="line",
                paint={ "line-color": "black", "line-width": 2 },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            layer(
                id="water",
                type="fill",
                paint={ "fill-color": "blue" },
                source_layer="example_source",
                layout={ "visibility": "visible" },
            ),
            type="vector",
            id="example_source",
            url="pmtiles://https://data.source.coop/protomaps/openstreetmap/tiles/v3.pmtiles",
        ),
        zoom=12,
         initialViewState=dict(
            longitude=-122.5727462, latitude=37.9677487, zoom=13
        ),
        mapStyle="https://tiles.stadiamaps.com/styles/alidade_smooth.json",
    )