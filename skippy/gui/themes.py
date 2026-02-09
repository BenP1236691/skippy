from PyQt5.QtGui import QColor, QPalette


class Theme:
    def __init__(self, colors):
        self.colors = colors

    def apply(self, palette):
        for role, color in self.colors.get("active", {}).items():
            palette.setColor(getattr(QPalette, role), QColor(*color))

        for role, color in self.colors.get("disabled", {}).items():
            palette.setColor(
                QPalette.Disabled, getattr(QPalette, role), QColor(*color)
            )


DARK_THEME = Theme(
    {
        "active": {
            "WindowText": (180, 180, 180),
            "Button": (53, 53, 53),
            "Light": (180, 180, 180),
            "Midlight": (90, 90, 90),
            "Dark": (35, 35, 35),
            "Text": (180, 180, 180),
            "BrightText": (180, 180, 180),
            "ButtonText": (180, 180, 180),
            "Base": (42, 42, 42),
            "Window": (53, 53, 53),
            "Shadow": (20, 20, 20),
            "Highlight": (42, 130, 218),
            "HighlightedText": (180, 180, 180),
            "Link": (56, 252, 196),
            "AlternateBase": (66, 66, 66),
            "ToolTipBase": (53, 53, 53),
            "ToolTipText": (180, 180, 180),
            "LinkVisited": (80, 80, 80),
        },
        "disabled": {
            "WindowText": (127, 127, 127),
            "Text": (127, 127, 127),
            "ButtonText": (127, 127, 127),
            "Highlight": (80, 80, 80),
            "HighlightedText": (127, 127, 127),
        },
    }
)

LIGHT_THEME = Theme(
    {
        "active": {
            "WindowText": (0, 0, 0),
            "Button": (240, 240, 240),
            "Light": (180, 180, 180),
            "Midlight": (200, 200, 200),
            "Dark": (225, 225, 225),
            "Text": (0, 0, 0),
            "BrightText": (0, 0, 0),
            "ButtonText": (0, 0, 0),
            "Base": (237, 237, 237),
            "Window": (240, 240, 240),
            "Shadow": (20, 20, 20),
            "Highlight": (76, 163, 224),
            "HighlightedText": (0, 0, 0),
            "Link": (0, 162, 232),
            "AlternateBase": (225, 225, 225),
            "ToolTipBase": (240, 240, 240),
            "ToolTipText": (0, 0, 0),
            "LinkVisited": (222, 222, 222),
        },
        "disabled": {
            "WindowText": (115, 115, 115),
            "Text": (115, 115, 115),
            "ButtonText": (115, 115, 115),
            "Highlight": (190, 190, 190),
            "HighlightedText": (115, 115, 115),
        },
    }
)
