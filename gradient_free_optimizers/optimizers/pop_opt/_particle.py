# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import random
import numpy as np
from scipy.spatial.transform import Rotation as R

from ..local_opt import HillClimbingOptimizer


def roation(n_dim, vector):
    if n_dim == 1:
        return -1  # not sure about that

    I = np.identity(n_dim - 1)
    R = np.pad(I, ((1, 0), (0, 1)), "minimum")
    R[0, n_dim - 1] = -1

    return np.matmul(R, vector)


class Particle(HillClimbingOptimizer):
    def __init__(
        self,
        *args,
        inertia=0.5,
        cognitive_weight=0.5,
        social_weight=0.5,
        temp_weight=0.2,
        rand_rest_p=0.03,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.global_pos_best = None

        self.inertia = inertia
        self.cognitive_weight = cognitive_weight
        self.social_weight = social_weight
        self.temp_weight = temp_weight
        self.rand_rest_p = rand_rest_p

    def _move_part(self, pos, velo):
        pos_new = (pos + velo).astype(int)
        # limit movement
        n_zeros = [0] * len(self.conv.max_positions)

        return np.clip(pos_new, n_zeros, self.conv.max_positions)

    @HillClimbingOptimizer.track_nth_iter
    @HillClimbingOptimizer.random_restart
    def move_linear(self):
        r1, r2 = random.random(), random.random()

        A = self.inertia * self.velo
        B = self.cognitive_weight * r1 * np.subtract(self.pos_best, self.pos_current)
        C = (
            self.social_weight
            * r2
            * np.subtract(self.global_pos_best, self.pos_current)
        )

        new_velocity = A + B + C
        return self._move_part(self.pos_current, new_velocity)

    @HillClimbingOptimizer.track_nth_iter
    @HillClimbingOptimizer.random_restart
    def move_spiral(self, center_pos):
        step_rate = (random.random() ** 1 / 3) * np.power(self.conv.dim_sizes, 1 / 3)

        # print("step_rate", step_rate)

        A = center_pos
        B = step_rate * roation(
            len(center_pos), np.subtract(self.pos_current, center_pos)
        )

        new_pos = A + B

        n_zeros = [0] * len(self.conv.max_positions)
        return np.clip(new_pos, n_zeros, self.conv.max_positions).astype(int)

    def evaluate(self, score_new):
        HillClimbingOptimizer.evaluate(self, score_new)
