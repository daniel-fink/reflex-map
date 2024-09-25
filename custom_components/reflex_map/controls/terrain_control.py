"""Terrain Control for Maplibre GL JS."""
import json
import reflex as rx

control_options = {
    "source": "terrain",
    "exaggeration": 1
}

class TerrainControl(rx.Component):
    tag="TerrainControl"

    lib_dependencies: list[str] = ["react-map-gl"]

    def add_imports(self):
        return {
            "react-map-gl": {rx.ImportVar(tag="useControl")},
        }

    def _get_custom_code(self) -> str | None:
        control_options_js = json.dumps(control_options)

        return f"""
const TerrainControl = () => {{
  const controlOptions = {control_options_js};

  useControl(({{ mapLib }}) => {{
    const TerrainControl = new mapLib.TerrainControl(controlOptions);
    return TerrainControl;
  }});
  return null;
}};

        """

def terrain_control() -> rx.Component:
    return TerrainControl.create()

terrain_control = TerrainControl.create