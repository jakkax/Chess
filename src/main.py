from chess.core.game_state import GameState
from chess.engine.engine import Engine
from chess.ui.tk.app import App


def main():
    # state = GameState.startingPosition()
    # engine = Engine()
    # app = App(state, engine)
    app = App()
    app.run()

if __name__ == "__main__":
    main()
