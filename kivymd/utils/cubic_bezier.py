"""
Cubic Bézier curve interpolation utilities.

This module provides a mathematical implementation of a cubic Bézier curve
interpolator ported from the Android Material Design animation framework.

The implementation is primarily used for calculating easing functions and
animation timing curves. It allows converting an input progress value (X-axis)
into the corresponding interpolated output value (Y-axis) based on four Bézier
control points.

The module includes:
    - A compatibility implementation of the cubic root function for Python
      versions older than 3.11.
    - Numerical helpers for solving cubic equations.
    - The CubicBezier class for evaluating cubic Bézier easing curves.

The implementation follows the algorithm used in Android's Material Design
motion system to achieve accurate interpolation behavior.
"""

import math
import sys

float_epsilon = 8.3446500e-7

if sys.version_info < (3, 11):
    cbrt = lambda number: (abs(number) ** (1 / 3)) * (-1 if number < 0 else 1)
else:
    cbrt = math.cbrt


class CubicBezier:
    """
    Ported from Android source code.
    Represents a cubic Bézier curve interpolator.

    A cubic Bézier curve is defined by four control points:

        P0 — start point
        P1 — first control point
        P2 — second control point
        P3 — end point

    The curve is commonly used in UI animations to define easing behavior.
    Given an input progress value `x` in the range [0, 1], the class calculates
    the corresponding output value `y` on the curve.

    This implementation solves the cubic equation required to find the curve
    parameter `t` for a given X value and then evaluates the curve at that
    parameter to obtain the interpolated Y value.

    Attributes:
        p0 (float): First control point value.
        p1 (float): Second control point value.
        p2 (float): Third control point value.
        p3 (float): Fourth control point value.

    This type of interpolation is commonly used for:
        - Animation easing functions.
        - Progress indicators.
        - UI transitions.
        - Material Design motion effects.
    """

    p0 = 0
    p1 = 0
    p2 = 0
    p3 = 0

    def __init__(self, *args):
        self.p0, self.p1, self.p2, self.p3 = args

    def evaluate_cubic(self, p1, p2, t):
        """
        Evaluates a cubic Bézier polynomial.

        Args:
            p1 (float): First control point.
            p2 (float): Second control point.
            t (float): Curve parameter in the range [0, 1].

        Returns:
            float: Calculated Bézier curve value.
        """

        a = 1.0 / 3.0 + (p1 - p2)
        b = p2 - 2.0 * p1
        c = p1

        return 3.0 * ((a * t + b) * t + c) * t

    def clamp_range(self, r):
        """
        Clamps a calculated root value into the valid Bézier range.

        Small floating-point calculation errors are corrected using an
        epsilon tolerance. Values outside the acceptable range are converted
        to NaN.

        Args:
            r (float): Calculated root value.

        Returns:
            float: Corrected value or NaN if invalid.
        """

        if r < 0.0:
            if -float_epsilon <= r < 0.0:
                return 0.0
            else:
                return math.nan
        elif r > 1.0:
            if 1.0 <= r <= 1.0 + float_epsilon:
                return 1.0
            else:
                return math.nan
        else:
            return r

    def close_to(self, x, y):
        """
        Checks whether two floating-point numbers are approximately equal.

        Args:
            x (float): First value.
            y (float): Second value.

        Returns:
            bool: True when the difference is below the precision threshold.
        """

        return abs(x - y) < float_epsilon

    def find_first_cubic_root(self, p0, p1, p2, p3):
        """
        Finds the first valid root of a cubic equation.

        The method solves the cubic polynomial generated from the Bézier curve
        equation and returns a parameter `t` within the valid interval [0, 1].

        The implementation handles:
            - Linear equations.
            - Quadratic equations.
            - Cubic equations with one or multiple roots.
            - Floating-point precision issues.

        Args:
            p0 (float): Polynomial coefficient.
            p1 (float): Polynomial coefficient.
            p2 (float): Polynomial coefficient.
            p3 (float): Polynomial coefficient.

        Returns:
            float:
                The first valid root in the range [0, 1],
                or NaN if no valid root exists.
        """

        a = 3.0 * (p0 - 2.0 * p1 + p2)
        b = 3.0 * (p1 - p0)
        c = p0
        d = -p0 + 3.0 * (p1 - p2) + p3

        if self.close_to(d, 0.0):
            if self.close_to(a, 0.0):
                if self.close_to(b, 0.0):
                    return math.nan

                return self.clamp_range(-c / b)
            else:
                q = math.sqrt(b * b - 4.0 * a * c)
                a2 = 2.0 * a
                root = self.clamp_range((q - b) / a2)

                if not math.isnan(root):
                    return root

                return self.clamp_range((-b - q) / a2)

        a /= d
        b /= d
        c /= d
        o3 = (3.0 * b - a * a) / 9.0
        q2 = (2.0 * a * a * a - 9.0 * a * b + 27.0 * c) / 54.0
        discriminant = q2 * q2 + o3 * o3 * o3
        a3 = a / 3.0

        if discriminant < 0.0:
            mp33 = -(o3 * o3 * o3)
            r = math.sqrt(mp33)
            t = -q2 / r
            cos_phi = max(-1.0, min(t, 1.0))
            phi = math.acos(cos_phi)
            t1 = 2.0 * cbrt(r)
            root = self.clamp_range(t1 * math.cos(phi / 3.0) - a3)

            if not math.isnan(root):
                return root

            root = self.clamp_range(
                t1 * math.cos((phi + 2.0 * math.pi) / 3.0) - a3
            )

            if not math.isnan(root):
                return root

            return self.clamp_range(
                t1 * math.cos((phi + 4.0 * math.pi) / 3.0) - a3
            )
        elif self.close_to(discriminant, 0.0):
            u1 = -cbrt(q2)
            root = self.clamp_range(2.0 * u1 - a3)

            if not math.isnan(root):
                return root

            return self.clamp_range(-u1 - a3)

        sd = math.sqrt(discriminant)
        u1 = cbrt(-q2 + sd)
        v1 = cbrt(q2 + sd)

        return self.clamp_range(u1 - v1 - a3)

    def t(self, value: float):
        """
        Calculates the interpolated Bézier value for an input progress value.

        This method converts an X-axis position into the corresponding Y-axis
        position on the cubic Bézier curve.

        Args:
            value (float):
                Input progress value, normally in the range [0, 1].

        Returns:
            float:
                Interpolated output value based on the Bézier curve.
        """

        return self.evaluate_cubic(
            self.p1,
            self.p3,
            self.find_first_cubic_root(
                -value,
                self.p0 - value,
                self.p2 - value,
                1.0 - value,
            ),
        )
