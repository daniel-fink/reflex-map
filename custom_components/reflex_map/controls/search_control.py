"""Search Control for Maplibre GL JS."""

import json
import reflex as rx

control_options = {
    "position": "top-left",
}
search_control_options = {
    "useMapFocusPoint": True,
}
class SearchControl(rx.Component):
    tag="SearchControl"
    lib_dependencies: list[str] = ["@stadiamaps/maplibre-search-box", "react-map-gl"]

    def add_imports(self):
        return {
            "": ["@stadiamaps/maplibre-search-box/dist/style.css"],
            "@stadiamaps/maplibre-search-box": {rx.ImportVar(tag="MapLibreSearchControl")},
            "react-map-gl": {rx.ImportVar(tag="useControl")},
        }

    def _get_custom_code(self) -> str | None:
        control_options_js = json.dumps(control_options)
        search_control_options_js = json.dumps(search_control_options)

        return f"""
const SearchControl = () => {{
  const controlOptions = {control_options_js};

  useControl(
    () => {{
      const searchControlOptions = {search_control_options_js};

      const searchControl = new MapLibreSearchControl(searchControlOptions);
      return searchControl;
    }},
    controlOptions
  );
  return null;
}};
        """

def search_control() -> rx.Component:
    return SearchControl.create()

search_control = SearchControl.create