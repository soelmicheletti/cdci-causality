import statistics
from collections import Counter
from typing import Callable

import numpy as np


class CDCI:
    def __init__(
        self, dist_fn: Callable, max_dev: int = 3, epsilon: float = 1e-8
    ) -> None:
        self.dist_fn = dist_fn
        self.max_dev = max_dev
        self.epsilon = epsilon

    def _cond_dist(self, x: np.array, y: np.array) -> np.array:
        vmax = 2 * self.max_dev
        vmin = -2 * self.max_dev

        x = (x - x.mean()) / (x.std() + self.epsilon)
        t = x[np.abs(x) < self.max_dev]
        x = (x - t.mean()) / (t.std() + self.epsilon)
        xd = np.round(x * 2)
        xd[xd > vmax] = vmax
        xd[xd < vmin] = vmin

        x_count: Counter = Counter(xd)
        vrange = range(vmin, vmax + 1)

        pyx = []
        for x in x_count:
            if x_count[x] > 12:
                yx = y[xd == x]
                yx = (yx - np.mean(yx)) / (np.std(yx) + self.epsilon)
                yx = np.round(yx * 2)
                yx[yx > vmax] = vmax
                yx[yx < vmin] = vmin
                count_yx: Counter = Counter(yx)
                pyx_x = np.array([count_yx[i] for i in vrange], dtype=np.float64)
                pyx_x = pyx_x / pyx_x.sum()
                pyx.append(pyx_x)
        return pyx

    def _compute_probabilities(self, A: np.array, B: np.array):
        pyx = self._cond_dist(A, B)
        if len(pyx) == 0:
            return 0, 0
        pyx = np.array(pyx)
        mean_y = pyx.mean(axis=0)
        return pyx, mean_y

    def _causal_score(self, A: np.array, B: np.array) -> float:
        pyx, mean_y = self._compute_probabilities(A, B)
        return statistics.mean(
            [self.dist_fn(pyx[i], mean_y) for i in range(pyx.shape[0])]
        )

    def __call__(self, X: np.array, Y: np.array) -> float:
        combined_casual_score = self._causal_score(Y, X) - self._causal_score(X, Y)
        return combined_casual_score
