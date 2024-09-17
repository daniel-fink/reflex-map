import { useEffect, useState } from "react";
import Map from "react-map-gl/maplibre";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import "@stadiamaps/maplibre-search-box/dist/style.css";
import "@watergis/maplibre-gl-legend/dist/maplibre-gl-legend.css";
import * as pmtiles from "pmtiles";
import { MapLibreSearchControl } from "@stadiamaps/maplibre-search-box";
import { MaplibreLegendControl } from "@watergis/maplibre-gl-legend";

export const MapLibre = (props) => {
  /**
   * We need to store the map object so we can do things like add controls or query features.
   */
  const [map, setMap] = useState(null);

  /**
   * Need to find a way to insert custom react code inside the useEffect.
   * This is currently the only way for react-map-gl maplibre to consume controls.
   *
   * This serves our specific purpose but is not meaningful to a consumer of this component.
   */
  useEffect(() => {
    if (!map) return;
    const fullScreenControl = new maplibregl.FullscreenControl();
    const navControl = new maplibregl.NavigationControl();

    const searchControl = new MapLibreSearchControl({
      useMapFocusPoint: true,
    });

    const legendControl = new MaplibreLegendControl(
      { google_maps: "Google Maps" },
      {
        title: "Legend",
        onlyRendered: false,
      }
    );
    map.addControl(fullScreenControl);
    map.addControl(navControl);
    map.addControl(searchControl, "top-left");
    map.addControl(legendControl, "top-left");

    return () => {
      map.removeControl(fullScreenControl);
      map.removeControl(searchControl);
      map.removeControl(navControl);
      map.removeControl(legendControl);
    };
  }, [map]);

  /**
   * We set protocol here for PMTiles.
   * This is optional, but if you want to use PMTiles, you need to set the protocol.
   */
  useEffect(() => {
    const protocol = new pmtiles.Protocol();
    maplibregl.addProtocol("pmtiles", protocol.tile);
    return () => {
      maplibregl.removeProtocol("pmtiles");
    };
  }, []);

  /**
   * MapLibre doesn't expose the features on mouse events unless explicitly stated.
   * This function will handle the mouse events and return the features.
   */
  const handleMouseClickEvent = (e, mouseEventFunction) => {
    if (!map) return;
    if (!e.point) return;
    const features = map.queryRenderedFeatures(e.point);
    return mouseEventFunction?.({ ...e, features });
  };

  return (
    <Map
      ref={setMap}
      mapLib={maplibregl}
      {...props}
      /** We handle the mouse events below after spreading props so that the props don't override them */
      onMouseDown={(e) => handleMouseClickEvent(e, props.onMouseDown)}
      onMouseUp={(e) => handleMouseClickEvent(e, props.onMouseUp)}
      onMouseMove={(e) => handleMouseClickEvent(e, props.onMouseMove)}
      onClick={(e) => handleMouseClickEvent(e, props.onClick)}
    />
  );
};
