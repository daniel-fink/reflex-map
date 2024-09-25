"""MapLibre Reflex Component"""

from typing import Any, Dict, List, Optional
import reflex as rx
from reflex_map.maplibre_react import get_maplibre_js

class MapState(rx.State):
    latitude: float | None = 37.9677487
    longitude: float | None = -122.5727462
    
    hoveredFeatures: Dict[str, Any] = []
    selectedFeatures: Dict[str, Any] = []

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
            _var_is_string=False
        ),
    ]


class Map(rx.Component):
    tag = "MapLibre"

    initialViewState: dict | None
    mapStyle: str | None
    terrain: Optional[Dict[str, Any]]
    longitude: float | None
    latitude: float | None

    lib_dependencies: list[str] = ["react-map-gl", "pmtiles", "mapbox-gl", "maplibre-gl"]

    def add_imports(self):
      return {
            "react-map-gl": {rx.ImportVar(tag="Map", is_default=True)},
            "pmtiles": {rx.ImportVar(tag="* as pmtiles", is_default=True)},
            "maplibre-gl":{rx.ImportVar(tag="maplibregl", is_default=True)},
            "": ["maplibre-gl/dist/maplibre-gl.css"],
      }
    
    def _get_custom_code(self) -> str | None:
        return get_maplibre_js()
    
    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_click": _on_map_layer_mouse_event,
            "on_mouse_move": _on_map_layer_mouse_event,
        }

def map() -> rx.Component:
    return Map.create(
        mapStyle="https://tiles.stadiamaps.com/styles/alidade_smooth.json", # this is just another map style
    )

map = Map.create