# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np


class SearchTracker:
    def __init__(self):
        super().__init__()

        self._pos_new = None
        self._score_new = -np.inf

        self._pos_current = None
        self._score_current = -np.inf

        self._pos_best = None
        self._score_best = -np.inf

        self.pos_new_list = []
        self.score_new_list = []

        self.pos_current_list = []
        self.score_current_list = []

        self.pos_best_list = []
        self.score_best_list = []

    ### new ###

    @property
    def pos_new(self):
        return self._pos_new

    @pos_new.setter
    def pos_new(self, pos):
        self.pos_new_list.append(pos)
        self._pos_new = pos

    @property
    def score_new(self):
        return self._score_new

    @score_new.setter
    def score_new(self, score):
        self.score_new_list.append(score)
        self._score_new = score

    ### current ###

    @property
    def pos_current(self):
        return self._pos_current

    @pos_current.setter
    def pos_current(self, pos):
        self.pos_current_list.append(pos)
        self._pos_current = pos

    @property
    def score_current(self):
        return self._score_current

    @score_current.setter
    def score_current(self, score):
        self.score_current_list.append(score)
        self._score_current = score

    ### best ###

    @property
    def pos_best(self):
        return self._pos_best

    @pos_best.setter
    def pos_best(self, pos):
        self.pos_best_list.append(pos)
        self._pos_best = pos

    @property
    def score_best(self):
        return self._score_best

    @score_best.setter
    def score_best(self, score):
        self.score_best_list.append(score)
        self._score_best = score
