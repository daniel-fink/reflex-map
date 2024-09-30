"""MapLibre Reflex Component"""

from typing import Any, Dict, List, Optional
import reflex as rx
from reflex_map.maplibre_react import get_maplibre_js
         
# https://visgl.github.io/react-map-gl/docs/api-reference/types#maplayermouseevent
class _SafeMapLayerMapEvent(rx.Base):
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
    features: List[Dict[str, Any]] | None

class _MapLayerMouseEvent(_SafeMapLayerMapEvent):
    target: Any # Whole map that causes circular reference

def _on_map_layer_mouse_event(e0: _MapLayerMouseEvent):
    """
    Maps the onClick args from javascript to the event handled by the Reflex.
    Returns dict-like object with keys defined in the _SafeMapLayerMapEvent class.
    See get_maplibre_js() in the maplibre_react.py file.
    """
    return rx.vars.var_operation_return(
        js_expression=f"extractSafeEvent({e0})"
    ),

class Map(rx.Component):
    tag = "MapLibre"

    initialViewState: rx.Var[dict | None]
    mapStyle: rx.Var[str | None]
    terrain: rx.Var[Dict[str, Any] | None]
    longitude: rx.Var[float | None]
    latitude: rx.Var[float | None]

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
    return Map.create()

map = Map.create