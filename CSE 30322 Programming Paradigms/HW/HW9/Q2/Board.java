public class Board {
  private char[][] board;

  public Board() {
    this.board = new char[3][3];
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        this.board[i][j] = ' ';
      }
    }
  }

  public void printBoard() {
    System.out.println(this.board[0][0] + "|" + this.board[1][0] + "|" + this.board[2][0]);
    System.out.println("-+-+-");
    System.out.println(this.board[0][1] + "|" + this.board[1][1] + "|" + this.board[2][1]);
    System.out.println("-+-+-");
    System.out.println(this.board[0][2] + "|" + this.board[1][2] + "|" + this.board[2][2]);
  }

  public char getBoard(int n) {
    return this.board[(n - 1) % 3][(n - 1) / 3];
  }

  public boolean setBoard(int n, char player) {
    if (getBoard(n) != ' ') {
      return false;
    }
    this.board[(n - 1) % 3][(n - 1) / 3] = player;
    return true;
  }

  public boolean checkWin(int turnnum) {
    for (int i = 0; i < 3; i++) {
      if ((this.board[i][0] == this.board[i][1] && this.board[i][0] == this.board[i][2] && this.board[i][0] != ' ')
          || (this.board[0][i] == this.board[1][i] && this.board[0][i] == this.board[2][i]
              && this.board[0][i] != ' ')) {
        return true;
        // check horizontal and vertical wins
      }
    }
    if (this.board[1][1] != ' ') {
      if (this.board[0][0] == this.board[2][2] && this.board[0][0] == this.board[1][1]) {
        return true;
        // check backslash wins
      } else if (this.board[0][2] == this.board[2][0] && this.board[0][2] == this.board[1][1]) {
        return true;
        // check slash wins
      }
    }
    // draw
    if (turnnum > 9) {
      return true;
    }
    return false;
  }

}
