from game import State


class TestState:
    def test_is_lose(self):
        state = State(size=3)
        assert not state.is_lose()
        for i in range(3):
            state.enemy_pieces[i] = 1
        assert state.is_lose()
