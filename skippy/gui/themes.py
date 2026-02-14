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
            "WindowText": (230, 232, 235),
            "Button": (34, 38, 45),
            "Light": (90, 98, 110),
            "Midlight": (58, 66, 76),
            "Dark": (24, 28, 34),
            "Text": (230, 232, 235),
            "BrightText": (255, 255, 255),
            "ButtonText": (230, 232, 235),
            "Base": (24, 28, 34),
            "Window": (28, 32, 38),
            "Shadow": (10, 12, 14),
            "Highlight": (0, 168, 157),
            "HighlightedText": (20, 20, 20),
            "Link": (76, 189, 255),
            "AlternateBase": (36, 41, 49),
            "ToolTipBase": (28, 32, 38),
            "ToolTipText": (230, 232, 235),
            "LinkVisited": (120, 120, 120),
        },
        "disabled": {
            "WindowText": (130, 136, 145),
            "Text": (130, 136, 145),
            "ButtonText": (130, 136, 145),
            "Highlight": (90, 90, 90),
            "HighlightedText": (130, 136, 145),
        },
    }
)

LIGHT_THEME = Theme(
    {
        "active": {
            "WindowText": (28, 30, 33),
            "Button": (244, 238, 231),
            "Light": (210, 200, 190),
            "Midlight": (220, 210, 200),
            "Dark": (200, 190, 180),
            "Text": (28, 30, 33),
            "BrightText": (0, 0, 0),
            "ButtonText": (28, 30, 33),
            "Base": (255, 255, 255),
            "Window": (250, 246, 240),
            "Shadow": (120, 120, 120),
            "Highlight": (0, 168, 157),
            "HighlightedText": (28, 30, 33),
            "Link": (0, 122, 196),
            "AlternateBase": (242, 236, 228),
            "ToolTipBase": (255, 255, 255),
            "ToolTipText": (28, 30, 33),
            "LinkVisited": (160, 160, 160),
        },
        "disabled": {
            "WindowText": (130, 130, 130),
            "Text": (130, 130, 130),
            "ButtonText": (130, 130, 130),
            "Highlight": (200, 200, 200),
            "HighlightedText": (130, 130, 130),
        },
    }
)
