"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import Any, Dict, List

import reflex as rx

from reflex_map import map
from reflex_map import source
from reflex_map import layer
from reflex_map import popup

from .style import style

filename = f"{rx.config.get_config().app_name}/{rx.config.get_config().app_name}.py"

class MapState(rx.State):
    latitude: rx.Var[float] = -33.865143
    longitude: rx.Var[float] = 151.2099

    hoveredFeatures: rx.Var[List[Dict[str, Any]]] = []
    selectedFeatures: rx.Var[List[Dict[str, Any]]] = []

    def set_hovered_feature(self, event, features):
        if features:
            self.hoveredFeatures = features
        else:
            self.hoveredFeatures = {}

    def set_selected_feature(self, event, features):
        if features:
            self.selectedFeatures = features
            self.hoveredFeatures = []
        else:
            self.selectedFeatures = []

    

def index() -> rx.Component:
    return rx.box(
        rx.box(
            "Top Nav",
            class_name="topNav",
        ),
        rx.box(
            map(
                source(
                    layer(
                        id="google_maps",
                        type="raster",
                        source="google_maps",
                        layout={"visibility": "none"},
                    ),
                    type="raster",
                    id="google_maps",
                    title="Google Maps",
                    tileSize=256,
                    tiles=["https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"],
                ),
                popup(
                    rx.text("POPUP"),
                    latitude=-33.865143,
                    longitude=151.209900,
                    anchor="bottom",
                ),
                initialViewState=dict(
                    longitude=MapState.longitude, latitude=MapState.latitude, zoom=10
                ),
                on_click=MapState.set_selected_feature,
                on_mouse_move=MapState.set_hovered_feature,
                mapStyle="https://tiles.stadiamaps.com/styles/alidade_smooth.json",
            ),
            class_name="content",
        ),
        rx.box(
            rx.text("Sidebar"),
            class_name="sidebar",
        ),
        class_name="wrapper",
    )


# Add state and page to the app.
app = rx.App(style=style)
app.add_page(index)
