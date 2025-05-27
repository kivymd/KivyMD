from typing import Optional

from kivy.uix.widget import Widget


class WrongChildException(Exception):
    """
    Raised when trying to add a child to parent element and the element doesn't expect a child of that type
    """

    def __init__(
        self,
        parent: Widget,
        child: Widget,
        accepted: Optional[list[str]] = None,
    ):
        accepted_msg = f", accepted types are {accepted}"
        msg = f"{parent.__class__.__name__} was not expecting a child of type {child.__class__.__name__}{accepted_msg if accepted else ''}"
        super().__init__(msg)
