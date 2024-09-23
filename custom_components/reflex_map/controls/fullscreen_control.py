"""Fullscreen Control for Maplibre GL JS."""

import json
import reflex as rx

control_options = {
    "position": "top-right",
}

class FullscreenControl(rx.Component):
    tag="FullscreenControl"

    lib_dependencies: list[str] = ["react-map-gl"]
    
    def add_imports(self):
      return {
          "react-map-gl": {rx.ImportVar(tag="useControl")},
      }

    def _get_custom_code(self) -> str | None:
        control_options_js = json.dumps(control_options)

        return f"""
const FullscreenControl = () => {{
  const controlOptions = {control_options_js};

  useControl(({{ mapLib }}) => {{
    const fullScreenControl = new mapLib.FullscreenControl(controlOptions);
    return fullScreenControl;
  }});
  return null;
}};
        """

def fullscreen_control() -> rx.Component:
    return FullscreenControl.create()

fullscreen_control = FullscreenControl.create