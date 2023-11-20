"""
Components/Badge
================

.. versionadded:: 2.0.0


.. seealso::

    `Material Design 3 spec, Badge <https://m3.material.io/components/badges/overview>`_

.. rubric:: Badges show notifications, counts, or status information on
    navigation items and icons.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/badges.png
    :align: center

Example
-------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor

        MDIcon:
            icon: "gmail"
            pos_hint: {'center_x': .5, 'center_y': .5}

            MDBadge:
                text: "12"
    '''


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/badges-example.png
    :align: center
"""

__all__ = ("MDBadge",)

import os

from kivy.lang import Builder

from kivymd.uix.label import MDLabel
from kivymd import uix_path

with open(
    os.path.join(uix_path, "badge", "badge.kv"), encoding="utf-8"
) as kv_file:
    Builder.load_string(kv_file.read())


class MDBadge(MDLabel):
    """
    Badge class.

    .. versionadded:: 2.0.0

    For more information see in the
    :class:`~kivymd.uix.label.label.MDLabel` class documentation.
    """
