from typing import Any, Dict, List

import reflex as rx
import reflex_map as rx_map

filename = f"{rx.config.get_config().app_name}/{rx.config.get_config().app_name}.py"

class MapState(rx.State):
    latitude: float = 37.9677487
    longitude: float = -122.5727462

    hoveredFeatures: List[Dict[str, Any]] = []
    selectedFeatures: List[Dict[str, Any]] = []

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

def render_demo(title: str):
    return rx.link(rx.text(title, fontSize="0.825rem"), href=f"/{title}")


def default_map() -> rx.Component:
    return rx_map.map(
        rx_map.source(
            rx_map.layer(
                source="google_maps",
                type="raster",
            ),
            type="raster",
            title="Google Maps",
            id="google_maps",
            tileSize=256,
            tiles=["https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"],
            attribution="&copy; Google Maps"
        ),
        rx_map.search_control(),
        rx_map.navigation_control(),
        rx_map.fullscreen_control(),

        initialViewState=dict(
            longitude=151.209900, latitude=-33.865143, zoom=10
        ),
    )