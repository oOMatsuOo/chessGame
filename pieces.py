
class Position:
    def __init__(self, line: str, column: int):
        self.line = line
        self.column = column

class Piece:
    def __init__(self, position: Position, color: str):
        self.position = position
        self.color = color
    
    def all_move():
        return
    
    def patern():
        return
    
    def move():
        return

class Queen(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []
    
    def patern(self):
        return [{"column": "x", "line": 0}, {"column": 0, "line": "x"}, {"column": "x", "line": "x"}]

    def move(self):
        return
    
class King(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []

    def patern(self):
        return [{"column": 1, "line": 0}, {"column": 0, "line": 1}]

    def move(self):
        return

class Knight(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []

    def patern(self):
        return [{"column": 2, "line": 1}, {"column": 1, "line": 2}]

    def move(self):
        return

class Bishop(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []

    def patern(self):
        return [{"column": "x", "line": "x"}]

    def move(self):
        return

class Rooks(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []
    
    def patern(self):
        return [{"column": "x", "line": 0}, {"column": 0, "line": "x"}]

    def move(self):
        return

class Pawn(Piece):
    def __init__(self, position: Position, color: str):
        super(position)
    
    def all_move(self):
        return []
    
    def patern(self):
        return [{"column": 1, "line": 0}]

    def move(self):
        return

