"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from typing import Any, Dict
import reflex as rx
import reflex_map as rx_map

from ..layout import layout_container

class InfoState(rx.State):
    longitude: float | None = None
    latitude: float | None = None
    description: str = ""
    
    def set_selected_feature(self, data):
        if ("features" in data and data['features']):
            self.description = data['features'][0]['properties']['description']
            self.longitude = data['features'][0]["geometry"]["coordinates"][0]
            self.latitude = data['features'][0]["geometry"]["coordinates"][1]
        else:
            self.description = ""
            self.latitude = None
            self.longitude = None    

def feature_info_on_click_demo() -> rx.Component:
    return layout_container(
        "Display feature information on click",
        rx.text("When a user clicks a feature, show some text containing more information."),
        rx.html(
            InfoState.description,
            position="absolute",
            marginTop="170px",
            marginLeft="12px",
            zIndex="4",
            pointerEvents="none",
            background="rgba(255, 255, 255, 0.8)",
            maxWidth="300px",
            padding="8px",
            borderRadius="4px"
        ),
        rx.box(
            feature_info_on_click_map(),
        ),
        rx.code_block("""
class InfoState(rx.State):
    longitude: float = -77.04
    latitude: float = 38.907
    description: str = ""
    
    def set_selected_feature(self, event, data):
        if (data['features']):
            self.description = data['features'][0]['properties']['description']

        self.clickedLong = data['lngLat']['lng']
        self.clickedLat = data['lngLat']['lat']"""),

        rx.code_block("""def feature_info_on_click_map() -> rx.Component:
    return map(
        source(
            layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            layer(
                id="simple-tiles",
                type="raster",
                source="raster-tiles",
            ),
            type="raster",
            id="raster-tiles",
            tiles=["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap",
            tileSize=256,
            minzoom=0,
            maxzoom=19,
        ),
        source(
            layer(
                id="places",
                type="circle",
                paint={
                    "circle-radius": 10,  # Set the radius of the circle
                    "circle-color": "#007cbf",  # Set the color of the circle
                    "circle-stroke-width": 2,  # Optional: set a border around the circle
                    "circle-stroke-color": "#ffffff",  # Optional: border color
                },
                source="places",
            ),
            type="geojson",
            id="places",
            data={
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Some Data Here</strong><p>Some more data here</p>',
                            'icon': 'theatre'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.038659, 38.931567]
                        }
                    },
                ]
            }
        ),
        zoom=11.15,
        initialViewState=dict(
            longitude=-77.04, latitude=38.907, zoom=11.15
        ),
        on_click=InfoState.set_selected_feature
    )"""),
    )


def feature_info_on_click_map() -> rx.Component:
    return rx_map.map(
        rx.cond(
            InfoState.longitude is not None and InfoState.latitude is not None,
            rx_map.marker(
                longitude=InfoState.longitude,
                latitude=InfoState.latitude,
            ),
        ),
        rx_map.source(
            rx_map.layer(
                id="background",
                type="background",
                paint={"background-color": "#e0dfdf"},
            ),
            rx_map.layer(
                id="simple-tiles",
                type="raster",
                source="raster-tiles",
            ),
            type="raster",
            id="raster-tiles",
            tiles=["https://tile.openstreetmap.org/{z}/{x}/{y}.png"],
            attribution="&copy; OpenStreetMap",
            tileSize=256,
            minzoom=0,
            maxzoom=19,
        ),
        rx_map.source(
            rx_map.layer(
                id="places",
                type="circle",
                paint={
                    "circle-radius": 10,  # Set the radius of the circle
                    "circle-color": "#007cbf",  # Set the color of the circle
                    "circle-stroke-width": 2,  # Optional: set a border around the circle
                    "circle-stroke-color": "#ffffff",  # Optional: border color
                },
                source="places",
            ),
            type="geojson",
            id="places",
            data={
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Make it Mount Pleasant</strong><p><a href="http://www.mtpleasantdc.com/makeitmtpleasant" target="_blank" title="Opens in a new window">Make it Mount Pleasant</a> is a handmade and vintage market and afternoon of live entertainment and kids activities. 12:00-6:00 p.m.</p>',
                            'icon': 'theatre'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.038659, 38.931567]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Mad Men Season Five Finale Watch Party</strong><p>Head to Lounge 201 (201 Massachusetts Avenue NE) Sunday for a <a href="http://madmens5finale.eventbrite.com/" target="_blank" title="Opens in a new window">Mad Men Season Five Finale Watch Party</a>, complete with 60s costume contest, Mad Men trivia, and retro food and drink. 8:00-11:00 p.m. $10 general admission, $20 admission and two hour open bar.</p>',
                            'icon': 'theatre'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.003168, 38.894651]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Big Backyard Beach Bash and Wine Fest</strong><p>EatBar (2761 Washington Boulevard Arlington VA) is throwing a <a href="http://tallulaeatbar.ticketleap.com/2012beachblanket/" target="_blank" title="Opens in a new window">Big Backyard Beach Bash and Wine Fest</a> on Saturday, serving up conch fritters, fish tacos and crab sliders, and Red Apron hot dogs. 12:00-3:00 p.m. $25.grill hot dogs.</p>',
                            'icon': 'bar'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.090372, 38.881189]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Ballston Arts & Crafts Market</strong><p>The <a href="https://ballstonarts-craftsmarket.blogspot.com/" target="_blank" title="Opens in a new window">Ballston Arts & Crafts Market</a> sets up shop next to the Ballston metro this Saturday for the first of five dates this summer. Nearly 35 artists and crafters will be on hand selling their wares. 10:00-4:00 p.m.</p>',
                            'icon': 'art-gallery'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.111561, 38.882342]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Seersucker Bike Ride and Social</strong><p>Feeling dandy? Get fancy, grab your bike, and take part in this year\'s <a href="http://dandiesandquaintrelles.com/2012/04/the-seersucker-social-is-set-for-june-9th-save-the-date-and-start-planning-your-look/" target="_blank" title="Opens in a new window">Seersucker Social</a> bike ride from Dandies and Quaintrelles. After the ride enjoy a lawn party at Hillwood with jazz, cocktails, paper hat-making, and more. 11:00-7:00 p.m.</p>',
                            'icon': 'bicycle'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.052477, 38.943951]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Capital Pride Parade</strong><p>The annual <a href="https://www.capitalpride.org/parade" target="_blank" title="Opens in a new window">Capital Pride Parade</a> makes its way through Dupont this Saturday. 4:30 p.m. Free.</p>',
                            'icon': 'rocket'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.043444, 38.909664]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Muhsinah</strong><p>Jazz-influenced hip hop artist <a href="https://www.muhsinah.com" target="_blank" title="Opens in a new window">Muhsinah</a> plays the <a href="https://www.blackcatdc.com">Black Cat</a> (1811 14th Street NW) tonight with <a href="https://www.exitclov.com" target="_blank" title="Opens in a new window">Exit Clov</a> and <a href="https://godsilla.bandcamp.com" target="_blank" title="Opens in a new window">Gods’illa</a>. 9:00 p.m. $12.</p>',
                            'icon': 'music'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.031706, 38.914581]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>A Little Night Music</strong><p>The Arlington Players\' production of Stephen Sondheim\'s  <a href="http://www.thearlingtonplayers.org/drupal-6.20/node/4661/show" target="_blank" title="Opens in a new window"><em>A Little Night Music</em></a> comes to the Kogod Cradle at The Mead Center for American Theater (1101 6th Street SW) this weekend and next. 8:00 p.m.</p>',
                            'icon': 'music'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.020945, 38.878241]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {
                            'description':
                                '<strong>Truckeroo</strong><p><a href="http://www.truckeroodc.com/www/" target="_blank">Truckeroo</a> brings dozens of food trucks, live music, and games to half and M Street SE (across from Navy Yard Metro Station) today from 11:00 a.m. to 11:00 p.m.</p>',
                            'icon': 'music'
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-77.007481, 38.876516]
                        }
                    }
                ]
            }
        ),

        zoom=11.15,
        initialViewState=dict(
            longitude=-77.04, latitude=38.907, zoom=11.15
        ),
        on_click=InfoState.set_selected_feature
    )