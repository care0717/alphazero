from __future__ import annotations

import copy


class State:
    def __init__(
        self,
        size: int = 3,
    ) -> None:
        self.size: int = size
        self.pieces: list[int] = [0] * (size * size)
        self.enemy_pieces: list[int] = [0] * (size * size)

    def is_lose(self) -> bool:
        def is_comp(x: int, y: int, dx: int, dy: int) -> bool:
            for k in range(self.size):
                if (
                    y < 0
                    or self.size - 1 < y
                    or x < 0
                    or self.size - 1 < x
                    or self.enemy_pieces[x + y * self.size] == 0
                ):
                    return False
                x, y = x + dx, y + dy
            return True

        if is_comp(0, 0, 1, 1) or is_comp(0, self.size - 1, 1, -1):
            return True
        for i in range(self.size):
            if is_comp(0, i, 1, 0) or is_comp(i, 0, 0, 1):
                return True
        return False

    def is_draw(self) -> bool:
        if self.is_lose():
            return False
        for i in range(self.size * self.size):
            if self.pieces[i] == 0 or self.enemy_pieces[i] == 0:
                return False
        return True

    def is_done(self) -> bool:
        return self.is_lose() or self.is_draw()

    def next(self, action: int) -> State:
        state = copy.deepcopy(self)
        state.pieces[action] = 1
        tmp = state.pieces
        state.pieces = state.enemy_pieces
        state.enemy_pieces = tmp
        return self
