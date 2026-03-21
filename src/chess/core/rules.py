class Rules:
    pass



# TODO

# rules: contain the blueprints of moves; how to make a move
# engine: applies rules to an actual situation

# rules will have en passant square, castling rights, promotion squares

# GameState (board)
#       ↓
# Engine scans board
#       ↓
# Engine reads piece type
#       ↓
# Rules provide movement pattern
#       ↓
# Engine builds pseudo-legal moves
#       ↓
# Engine simulates moves
#       ↓
# Engine filters illegal moves
