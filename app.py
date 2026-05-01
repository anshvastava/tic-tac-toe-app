from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Game state
board = [""] * 9
current_player = "X"

def check_winner():
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != "":
            return board[cond[0]]
    if "" not in board:
        return "Draw"
    return None

@app.route('/')
def home():
    return render_template('index.html', board=board)

@app.route('/move/<int:pos>')
def move(pos):
    global current_player, board

    if board[pos] == "":
        board[pos] = current_player

        winner = check_winner()
        if winner:
            return f"Game Over! Result: {winner} <br><a href='/reset'>Play Again</a>"

        current_player = "O" if current_player == "X" else "X"

    return redirect(url_for('home'))

@app.route('/reset')
def reset():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)