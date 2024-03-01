import math

# Made in reference with
# ~/material-components-android/lib/java/com/google/android/material/carousel/Arrangement.java


class Arrangement:
    MEDIUM_ITEM_FLEX_PERCENTAGE = 0.1

    def __init__(
        self,
        priority,
        target_small_size,
        min_small_size,
        max_small_size,
        small_count,
        target_medium_size,
        medium_count,
        target_large_size,
        large_count,
        available_space,
    ):
        self.priority = priority
        self.small_size = max(min(target_small_size, max_small_size), min_small_size)
        self.small_count = small_count
        self.medium_size = target_medium_size
        self.medium_count = medium_count
        self.large_size = target_large_size
        self.large_count = large_count
        self.fit(available_space, min_small_size, max_small_size, target_large_size)
        self.cost = self.calculate_cost(target_large_size)

    def __str__(self):
        return (
            f"Arrangement [priority={self.priority}, small_count={self.small_count},"
            f" small_size={self.small_size}, medium_count={self.medium_count},"
            f" medium_size={self.medium_size}, large_count={self.large_count},"
            f" large_size={self.large_size}, cost={self.cost}]"
        )

    def get_space(self):
        return (
            (self.large_size * self.large_count)
            + (self.medium_size * self.medium_count)
            + (self.small_size * self.small_count)
        )

    def fit(self, available_space, min_small_size, max_small_size, target_large_size):
        delta = available_space - self.get_space()
        if self.small_count > 0 and delta > 0:
            self.small_size += min(
                delta / self.small_count, max_small_size - self.small_size
            )
        elif self.small_count > 0 and delta < 0:
            self.small_size += max(
                delta / self.small_count, min_small_size - self.small_size
            )
        self.small_size = self.small_size if self.small_count > 0 else 0
        self.large_size = self.calculate_large_size(
            available_space, min_small_size, max_small_size, target_large_size
        )
        self.medium_size = (self.large_size + self.small_size) / 2
        if self.medium_count > 0 and self.large_size != target_large_size:
            target_adjustment = (target_large_size - self.large_size) * self.large_count
            available_medium_flex = (
                self.medium_size * self.MEDIUM_ITEM_FLEX_PERCENTAGE
            ) * self.medium_count
            distribute = min(abs(target_adjustment), available_medium_flex)
            if target_adjustment > 0:
                self.medium_size -= distribute / self.medium_count
                self.large_size += distribute / self.large_count
            else:
                self.medium_size += distribute / self.medium_count
                self.large_size -= distribute / self.large_count

    def calculate_large_size(
        self, available_space, min_small_size, max_small_size, target_large_size
    ):
        small_size = self.small_size if self.small_count > 0 else 0
        return (
            available_space
            - (
                ((float(self.small_count)) + (float(self.medium_count)) / 2)
                * small_size
            )
        ) / ((float(self.large_count)) + (float(self.medium_count)) / 2)

    def is_valid(self):
        if self.large_count > 0 and self.small_count > 0 and self.medium_count > 0:
            return (
                self.large_size > self.medium_size
                and self.medium_size > self.small_size
            )
        elif self.large_count > 0 and self.small_count > 0:
            return self.large_size > self.small_size
        return True

    def calculate_cost(self, target_large_size):
        if not self.is_valid():
            return float("inf")
        return abs(target_large_size - self.large_size) * self.priority

    @staticmethod
    def find_lowest_cost_arrangement(
        available_space,
        target_small_size,
        min_small_size,
        max_small_size,
        small_counts,
        target_medium_size,
        medium_counts,
        target_large_size,
        large_counts,
    ):
        lowest_cost_arrangement = None
        priority = 1

        for large_count in large_counts:
            for medium_count in medium_counts:
                for small_count in small_counts:
                    arrangement = Arrangement(
                        priority,
                        target_small_size,
                        min_small_size,
                        max_small_size,
                        small_count,
                        target_medium_size,
                        medium_count,
                        target_large_size,
                        large_count,
                        available_space,
                    )

                    if (
                        lowest_cost_arrangement is None
                        or arrangement.cost < lowest_cost_arrangement.cost
                    ):
                        lowest_cost_arrangement = arrangement
                        if lowest_cost_arrangement.cost == 0:
                            return lowest_cost_arrangement
                    priority += 1
        return lowest_cost_arrangement

    def get_item_count(self):
        return self.small_count + self.medium_count + self.large_count
