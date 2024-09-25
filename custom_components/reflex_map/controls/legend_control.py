"""Legend Control for Maplibre GL JS."""

import json
import reflex as rx

# Example usage with legend items
legend_items = {
    "google_satellite": "Google Satellite",
    "google_maps": "Google Maps",
}
legend_control_options = {
    "title": "Legend",
    "onlyRendered": False,
    "showCheckbox": True,
    "reverseOrder": False,
    "showDefault": True,
}
control_options = {
    "position": "top-left",
}

"""Legend Control for Maplibre GL JS."""

class LegendControl(rx.Component):
    tag="LegendControl"

    lib_dependencies: list[str] = ["@watergis/maplibre-gl-legend", "react-map-gl"]

    def add_imports(self):
      return {
          "": ["@watergis/maplibre-gl-legend/dist/maplibre-gl-legend.css"],
          "@watergis/maplibre-gl-legend": {rx.ImportVar(tag="MaplibreLegendControl")},
          "react-map-gl": {rx.ImportVar(tag="useControl")},
      }

    def _get_custom_code(self) -> str | None:
        # Convert legend_items into a JavaScript object
        legend_items_js = json.dumps(legend_items)
        legend_control_options_js = json.dumps(legend_control_options)
        control_options_js = json.dumps(control_options)

        return f"""
const LegendControl = () => {{
  const controlOptions = {control_options_js};
  
  useControl(
    () => {{
      const legendItems = {legend_items_js};
      const legendOptions = {legend_control_options_js};

      const legendControl = new MaplibreLegendControl(legendItems, legendOptions);
      return legendControl;
    }},
    controlOptions
  );
  return null;
}};
        """


def legend_control() -> rx.Component:
    return LegendControl.create()

legend_control = LegendControl.create