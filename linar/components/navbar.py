import reflex as rx

from rxconfig import config



def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_menu_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def navbar_icons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/Lunar.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Lunar Discord Bot", size="7", weight="bold"
                    ),
                    align_items="center",
                    gap="2em"
                ),
                rx.hstack(
                    navbar_icons_item(
                        "Home", "home", "/#"
                    ),
                    navbar_icons_item(
                        "Features", "code-xml", "/#"
                    ),
                    navbar_icons_item(
                        "Pricing", "coins", "/#"
                    ),
                    navbar_icons_item(
                        "Contact", "mail", "/#"
                    ),
                    navbar_icons_item(
                        "Terms", "layers", "/#"
                    ),
                    spacing="4",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/Lunar.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Lunar Discord Bot", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        navbar_icons_menu_item(
                            "Home", "home", "/#"
                        ),
                        navbar_icons_menu_item(
                            "Pricing", "coins", "/#"
                        ),
                        navbar_icons_menu_item(
                            "Contact", "mail", "/#"
                        ),
                        navbar_icons_menu_item(
                            "Services", "layers", "/#"
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="0.85em 2em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )