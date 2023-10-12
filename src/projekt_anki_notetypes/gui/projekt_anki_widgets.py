from pathlib import Path
from typing import Tuple

from aqt.qt import (
    QCursor,
    QDir,
    QHBoxLayout,
    QIcon,
    QLabel,
    QPixmap,
    QSize,
    QSizePolicy,
    Qt,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
from aqt.utils import openLink

QDir.addSearchPath("icons", f"{Path(__file__).parent.parent}/resources")


def icon_button(icon_data: Tuple[str, Tuple[int, int], str]) -> QToolButton:
    (image, size, url) = icon_data
    icon = QIcon(QPixmap(f"icons:{image}"))
    button = QToolButton()
    button.setIcon(icon)
    button.setIconSize(QSize(size[0], size[1]))
    button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setAutoRaise(True)
    button.setToolTip(url)
    button.clicked.connect(lambda _, url=url: openLink(url))  # type: ignore
    return button


class AnkingIconsLayout(QHBoxLayout):
    def __init__(self, parent: QWidget) -> None:
        QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setup()
        parent.setLayout(self)

    def setup(self) -> None:
        self.addStretch()
        icon_objs = [
            ("projekt_anki.png", (31, 31), "https://anki.bvmd.de"),
            ("instagram.png", (31, 31), "https://www.instagram.com/anki_doc/"),
            ("discord.png", (31, 31), "https://discord.com/invite/5DMsDg8Rvu"),
        ]
        for obj in icon_objs:
            btn = icon_button(obj)
            self.addWidget(btn)
        self.addStretch()


class GithubLinkLayout(QHBoxLayout):
    def __init__(self, parent: QWidget, href: str) -> None:
        self.href = href

        QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setup()
        parent.setLayout(self)

    def setup(self) -> None:
        self.addStretch()
        text_layout = QVBoxLayout()
        self.addLayout(text_layout)
        self.addStretch()

        label = QLabel()
        label.setText(
            f'Fehler und Wünsche kannst du gerne <a href="{self.href}">hier</a> an uns weitergeben.'
        )
        label.setOpenExternalLinks(True)
        text_layout.addWidget(label)