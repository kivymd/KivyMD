import math
import sys
import bisect

float_epsilon = 8.3446500e-7

if sys.version_info < (3, 11):
    cbrt = lambda number: (abs(number) ** (1 / 3)) * (-1 if number < 0 else 1)
else:
    cbrt = math.cbrt


class CubicBezier:
    """Ported from Android source code"""

    p0 = 0
    p1 = 0
    p2 = 0
    p3 = 0

    def __init__(self, *args):
        self.p0, self.p1, self.p2, self.p3 = args

    def evaluate_cubic(self, p1, p2, t):
        a = 1.0 / 3.0 + (p1 - p2)
        b = p2 - 2.0 * p1
        c = p1
        return 3.0 * ((a * t + b) * t + c) * t

    def clamp_range(self, r):
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
        return abs(x - y) < float_epsilon

    def find_first_cubic_root(self, p0, p1, p2, p3):
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
