import reflex as rx
import reflex_map as rx_map

from .. import layout

def pmtiles_demo():
    return layout.container(
        "PMTiles",
        rx.text("Uses the PMTiles plugin and protocol to present a map."),
        rx.box(
            pmtiles_map()
        ),
        rx.code_block("""
def pmtiles_map() -> rx.Component:
    return rx_map.map(
        rx_map.source(
            rx_map.layer(
                id="water",
                type="fill",
                paint={ "fill-color": "#80b1d3" },
                source_layer="water",
                source="example_source"
            ),
            rx_map.layer(
                id="buildings",
                type="fill",
                paint={ "fill-color": "#d9d9d9" },
                source_layer="landuse",
                source="example_source",
            ),
            rx_map.layer(
                id="roads",
                type="line",
                paint={ "line-color": "#fc8d62" },
                source="example_source",
                source_layer="roads",
            ),
            rx_map.layer(
                id="pois",
                type="circle",
                paint={ "circle-color": "#ffffb3" },
                source="example_source",
                source_layer="pois",
            ),
            type="vector",
            id="example_source",
            url="pmtiles://https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles",
            attribution="&copy; Protomaps | &copy; pmtiles.io",
        ),
        zoom=13,
         initialViewState=dict(
            longitude=11.2543435, latitude=43.7672134, zoom=13,
        ),
    )
        """),
    )


def pmtiles_map() -> rx.Component:
    return rx_map.map(
        rx_map.source(
            rx_map.layer(
                id="water",
                type="fill",
                paint={ "fill-color": "#80b1d3" },
                source_layer="water",
                source="example_source"
            ),
            rx_map.layer(
                id="buildings",
                type="fill",
                paint={ "fill-color": "#d9d9d9" },
                source_layer="landuse",
                source="example_source",
            ),
            rx_map.layer(
                id="roads",
                type="line",
                paint={ "line-color": "#fc8d62" },
                source="example_source",
                source_layer="roads",
            ),
            rx_map.layer(
                id="pois",
                type="circle",
                paint={ "circle-color": "#ffffb3" },
                source="example_source",
                source_layer="pois",
            ),
            type="vector",
            id="example_source",
            url="pmtiles://https://pmtiles.io/protomaps(vector)ODbL_firenze.pmtiles",
            attribution="&copy; Protomaps | &copy; pmtiles.io",
        ),
        zoom=13,
         initialViewState=dict(
            longitude=11.2543435, latitude=43.7672134, zoom=13,
        ),
    )