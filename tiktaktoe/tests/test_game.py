from game import State

size = 3


class TestState:
    def test_is_lose(self):
        state = State(size=size)
        assert not state.is_lose()
        for i in range(size):
            state.enemy_pieces[i] = 1
        assert state.is_lose()

    def test_is_draw(self):
        state = State(size=size)
        assert not state.is_draw()
        for i in range(size * size):
            if ((i // size) % 2 == 0 and i % size == 0) or (
                (i // size) % 2 == 1 and i % size != 0
            ):
                state.enemy_pieces[i] = 1
            else:
                state.pieces[i] = 1
        assert state.is_draw()
