import reflex as rx

config = rx.Config(
    app_name="map_demo",
    tailwind={
        "theme": {
            "accentColor": "blue",
            "extend": {
                "colors": {
                    "blue": {
                        50: '#e3f2fd',
                        100: '#bbdefb',
                        200: '#90caf9',
                        300: '#64b5f6',
                        400: '#42a5f5',
                        500: 'rgb(35, 87, 141)',
                        600: '#1e73b8',
                        700: '#195ca2',
                        800: '#15478b',
                        900: '#113374',
                    }
                },
            },
        },
        "plugins": ["@tailwindcss/typography"],
    },
)