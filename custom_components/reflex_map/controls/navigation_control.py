"""Navigation Control for Maplibre GL JS."""
import json
import reflex as rx

control_options = {
    "position": "top-right",
}

class NavigationControl(rx.Component):
    tag="NavigationControl"

    lib_dependencies: list[str] = ["react-map-gl"]

    def add_imports(self):
        return {
            "react-map-gl": {rx.ImportVar(tag="useControl")},
        }

    def _get_custom_code(self) -> str | None:
        control_options_js = json.dumps(control_options)

        return f"""
const NavigationControl = () => {{
  const controlOptions = {control_options_js};

  useControl(({{ mapLib }}) => {{
    const NavigationControl = new mapLib.NavigationControl(controlOptions);
    return NavigationControl;
  }});
  return null;
}};

        """

def navigation_control() -> rx.Component:
    return NavigationControl.create()

navigation_control = NavigationControl.create