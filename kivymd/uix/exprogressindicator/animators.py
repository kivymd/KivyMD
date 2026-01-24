from kivymd.utils.cubic_bezier import CubicBezier
import math

# Ported from
# ./lib/java/com/google/android/material/progressindicator/


class LinearIndeterminateDisjointAnimator:
    # from LinearIndeterminateDisjointAnimatorDelegate.java
    INTERPOLATORS = [
        CubicBezier(0.2, 0.0, 0.8, 1.0).t,  # line1_head
        CubicBezier(0.4, 0.0, 1.0, 1.0).t,  # line1_tail
        CubicBezier(0.0, 0.0, 0.65, 1.0).t,  # line2_head
        CubicBezier(0.1, 0.0, 0.45, 1.0).t,  # line2_tail
    ]
    DURATION_TO_MOVE_SEGMENT_ENDS = [533, 567, 850, 750]
    DELAY_TO_MOVE_SEGMENT_ENDS = [1267, 1000, 333, 0]

    TOTAL_DURATION_IN_MS = 1800
    LOOP_DELAY = 20

    def get_fraction_in_range(self, playtime, start, duration):
        if duration == 0:
            return 0.0
        return max(0.0, min((playtime - start) / duration, 1.0))

    def compute_bar(self, playtime, head_idx, tail_idx):
        f_head = self.get_fraction_in_range(
            playtime,
            self.DELAY_TO_MOVE_SEGMENT_ENDS[head_idx],
            self.DURATION_TO_MOVE_SEGMENT_ENDS[head_idx],
        )
        f_tail = self.get_fraction_in_range(
            playtime,
            self.DELAY_TO_MOVE_SEGMENT_ENDS[tail_idx],
            self.DURATION_TO_MOVE_SEGMENT_ENDS[tail_idx],
        )

        start = self.INTERPOLATORS[head_idx](f_head)
        end = self.INTERPOLATORS[tail_idx](f_tail)
        return start, end

    def bars(self, time_sec):
        time_ms = (time_sec * 1000) % (self.TOTAL_DURATION_IN_MS + self.LOOP_DELAY)
        bar1 = self.compute_bar(time_ms, 0, 1)
        bar2 = self.compute_bar(time_ms, 2, 3)
        return bar1, bar2


class LinearIndeterminateContiguousAnimator:
    # from LinearIndeterminateContiguousAnimatorDelegate.java
    INTERPOLATOR = CubicBezier(0.4, 0.0, 0.2, 1.0).t

    TOTAL_DURATION_IN_MS = 667
    DURATION_PER_CYCLE_IN_MS = 333

    last_cycle_count = -1
    current_indices = [0, 0, 0]
    len_palette = 0

    def __init__(self):
        self.last_cycle_count = -1
        self.current_indices = [0, 0, 0]

    def get_fraction_in_range(self, playtime, start, duration):
        return max(0.0, (playtime - start) / duration)

    def bars(self, time_sec):
        time_ms = time_sec * 1000
        cycle_count = int(time_ms // self.DURATION_PER_CYCLE_IN_MS)
        playtime = time_ms % self.DURATION_PER_CYCLE_IN_MS

        if cycle_count != self.last_cycle_count:
            idx0 = cycle_count % self.len_palette
            idx1 = (cycle_count - 1) % self.len_palette
            idx2 = (cycle_count - 2) % self.len_palette
            self.current_indices = [idx0, idx1, idx2]
            self.last_cycle_count = cycle_count

        f1 = self.get_fraction_in_range(playtime, 0, self.TOTAL_DURATION_IN_MS)
        boundary_0_1 = self.INTERPOLATOR(f1)

        f2 = f1 + (self.DURATION_PER_CYCLE_IN_MS / self.TOTAL_DURATION_IN_MS)
        boundary_1_2 = self.INTERPOLATOR(min(f2, 1.0)) if f2 <= 1.0 else 1.0

        return (
            (0.0, boundary_0_1, self.current_indices[0]),
            (boundary_0_1, boundary_1_2, self.current_indices[1]),
            (boundary_1_2, 1.0, self.current_indices[2]),
        )


class CircularIndeterminateRetreatAnimator:
    # from CircularIndeterminateRetreatAnimatorDelegate.java
    INTERPOLATOR = CubicBezier(0.4, 0.0, 0.2, 1.0).t

    TOTAL_DURATION_MS = 6000
    DURATION_SPIN_MS = 500
    DURATION_GROW_MS = 3000
    DURATION_SHRINK_MS = 3000

    DELAY_SPINS_MS = [0, 1500, 3000, 4500]

    CONSTANT_ROTATION_DEGREES = 1080
    SPIN_ROTATION_DEGREES = 90

    END_FRACTION_RANGE = [0.10, 0.87]

    def __init__(self):
        self.complete_end_fraction = 0.0
        self.len_palette = 0

    def get_fraction_in_range(self, playtime, start, duration):
        if duration == 0:
            return 0.0
        return max(0.0, min((playtime - start) / duration, 1.0))

    def bars(self, time_sec):
        """
        Returns: (rotation, (start_fraction, end_fraction, color_index))
        """
        total_playtime_ms = time_sec * 1000

        rotation = self.CONSTANT_ROTATION_DEGREES * (
            total_playtime_ms / self.TOTAL_DURATION_MS
        )

        num_full_cycles = total_playtime_ms / self.TOTAL_DURATION_MS
        rotation += num_full_cycles * (
            len(self.DELAY_SPINS_MS) * self.SPIN_ROTATION_DEGREES
        )

        playtime_ms = total_playtime_ms % self.TOTAL_DURATION_MS

        for spin_delay in self.DELAY_SPINS_MS:
            f = self.get_fraction_in_range(
                playtime_ms, spin_delay, self.DURATION_SPIN_MS
            )
            rotation += self.INTERPOLATOR(f) * self.SPIN_ROTATION_DEGREES

        f_grow = self.get_fraction_in_range(playtime_ms, 0, self.DURATION_GROW_MS)
        f_shrink = self.get_fraction_in_range(
            playtime_ms, 3000, self.DURATION_SHRINK_MS
        )

        arc_growth_factor = self.INTERPOLATOR(f_grow) - self.INTERPOLATOR(f_shrink)
        start_fraction = 0.0
        end_fraction = self.END_FRACTION_RANGE[0] + (
            (self.END_FRACTION_RANGE[1] - self.END_FRACTION_RANGE[0])
            * arc_growth_factor
        )

        if self.complete_end_fraction > 0:
            end_fraction *= 1.0 - self.complete_end_fraction

        color_index = 0
        if self.len_palette > 0:
            color_index = int(playtime_ms // 1500) % self.len_palette

        return math.radians(rotation), (
            start_fraction,
            end_fraction,
            color_index,
        )


class CircularIndeterminateAdvancedAnimator:
    # from CircularIndeterminateAdvanceAnimatorDelegate.java
    INTERPOLATOR = CubicBezier(0.4, 0.0, 0.2, 1.0).t

    TOTAL_DURATION_MS = 5400
    TOTAL_CYCLES = 4

    DURATION_EXPAND = 667
    DURATION_COLLAPSE = 667
    DURATION_FADE_IN = 333

    DELAY_EXPAND = [0, 1350, 2700, 4050]
    DELAY_COLLAPSE = [667, 2017, 3367, 4717]
    DELAY_FADE_IN = [1000, 2350, 3700, 5050]

    TAIL_DEGREES_OFFSET = -20
    EXTRA_DEGREES_PER_CYCLE = 250
    CONSTANT_ROTATION_DEGREES = 1520

    def __init__(self):
        self.complete_end_fraction = 0.0
        self.len_palette = 0

    def get_fraction_in_range(self, playtime, start, duration):
        if duration == 0:
            return 0.0
        return max(0.0, min((playtime - start) / duration, 1.0))

    def get_color(self, time_sec, playtime_ms):
        if self.len_palette <= 0:
            return None, None, 0.0

        total_cycles_elapsed = int(
            ((time_sec * 1000) / self.TOTAL_DURATION_MS) * self.TOTAL_CYCLES
        )

        c_start_idx, c_end_idx, color_lerp = 0, 0, 0.0
        cycle_offset = total_cycles_elapsed % self.len_palette

        for i in range(self.TOTAL_CYCLES):
            f_fade = self.get_fraction_in_range(
                playtime_ms, self.DELAY_FADE_IN[i], self.DURATION_FADE_IN
            )
            if 0.0 < f_fade < 1.0:
                c_start_idx = (i + cycle_offset) % self.len_palette
                c_end_idx = (c_start_idx + 1) % self.len_palette
                color_lerp = self.INTERPOLATOR(f_fade)
                break
            elif f_fade >= 1.0:
                c_start_idx = (i + 1 + cycle_offset) % self.len_palette
                c_end_idx = c_start_idx
                color_lerp = 0.0
            else:
                c_start_idx = (cycle_offset) % self.len_palette
                c_end_idx = c_start_idx

        return c_start_idx, c_end_idx, color_lerp

    def bars(self, time_sec):
        """
        Returns: (rotation, (start_fraction, end_fraction, (c_start_idx, c_end_idx, color_lerp)))
        Note: rotation is 0 because Advance logic builds rotation into the fractions.
        """
        playtime_ms = (time_sec * 1000) % self.TOTAL_DURATION_MS
        animation_fraction = playtime_ms / self.TOTAL_DURATION_MS

        start_deg = (
            self.CONSTANT_ROTATION_DEGREES * animation_fraction
            + self.TAIL_DEGREES_OFFSET
        )
        end_deg = self.CONSTANT_ROTATION_DEGREES * animation_fraction

        for i in range(self.TOTAL_CYCLES):
            f_exp = self.get_fraction_in_range(
                playtime_ms, self.DELAY_EXPAND[i], self.DURATION_EXPAND
            )
            end_deg += self.INTERPOLATOR(f_exp) * self.EXTRA_DEGREES_PER_CYCLE
            f_col = self.get_fraction_in_range(
                playtime_ms, self.DELAY_COLLAPSE[i], self.DURATION_COLLAPSE
            )
            start_deg += self.INTERPOLATOR(f_col) * self.EXTRA_DEGREES_PER_CYCLE

        start_deg += (end_deg - start_deg) * self.complete_end_fraction

        return 0, (
            start_deg / 360.0,
            end_deg / 360.0,
            self.get_color(time_sec, playtime_ms),
        )
