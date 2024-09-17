"""MapLibre custom map component within Reflex"""

# Just a note on this file: 
# I was having trouble installing this component, I could never get it to work and sank too much time into playing around with it.
# I'm de-referencing it in my latest changes, most of the code was duplicated anyway, 
# but I do really like the idea to keep it seperated into a custom component. I'll keep it in the repo for now.

from typing import Any, Dict, List
import reflex as rx

class MapState(rx.State):
    latitude: rx.Var[float] = 37.9677487
    longitude: rx.Var[float] = -122.5727462
    
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

    

         
# https://visgl.github.io/react-map-gl/docs/api-reference/types#maplayermouseevent
class _MapLayerMouseEvent(rx.Base):
    """Defines the shape of the click event passed to onClick by react-map-gl."""
    event: Any
    type: str
    # The "target" object causes a circular reference, so we shouldn't allow access to it
    # target: Map
    originalEvent: Any
    point: Any # Point {x: number, y: number}
    lngLat: Dict[str, float] # {lng: number, lat: number}
    preventDefault: Any
    defaultPrevented: bool
    # Below features are what we are interested in
    features: List[Dict[str, Any]]

def _on_map_layer_mouse_event(e0: _MapLayerMouseEvent) -> Dict[str, float]:
    """Maps the onClick args from javascript to the event handled by the Reflex backend in python."""
    return [
        e0.event,
        rx.Var.create_safe(
            f"extractFeatureFromEvent({e0.features})",
        ),
    ]


class Map(rx.Component):
    # This import won't for anyone else unless they include our custom react component within their public assets
    # TODO: Find some way to do this without using a custom react component
    library = "/public/MapLibre"
    tag = "MapLibre"
    mapboxAccessToken: rx.Var[str]
    initialViewState: rx.Var[dict]
    mapStyle: rx.Var[str]
    lib_dependencies: list[str] = ["react-map-gl", "pmtiles", "mapbox-gl", "@stadiamaps/maplibre-search-box", "@watergis/maplibre-gl-legend", "maplibre-gl"]

    def _get_custom_code(self) -> str | None:
        return """
// extract only the features if they exist
const extractFeatureFromEvent = (features) => {
    return features
}
"""

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_click": _on_map_layer_mouse_event,
            "on_mouse_move": _on_map_layer_mouse_event,
        }

def map() -> rx.Component:
    return Map.create(
        mapStyle="https://tiles.stadiamaps.com/styles/alidade_smooth.json", # this is just another map style
        initialViewState=dict(
            longitude=MapState.longitude, latitude=MapState.latitude, zoom=10
        ),
        on_click=MapState.set_selected_feature,
        on_mouse_move=MapState.set_hovered_feature,
    )

map = Map.create