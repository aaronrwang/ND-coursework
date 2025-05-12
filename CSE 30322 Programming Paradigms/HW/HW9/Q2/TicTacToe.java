import java.util.Scanner;
import java.util.Random;

public class TicTacToe {
  public static boolean gameover = false;
  public static int turnnum = 1;

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Board board = new Board();
    board.printBoard();
    while (!gameover) {
      // Wait one second to simulate thinking
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {

      }
      if (turnnum % 2 == 1) {
        play('x', board, in);
      } else {
        play('o', board, in);
      }
      System.out.println("Turn: " + turnnum);
      board.printBoard();
      turnnum++;
      if (turnnum > 5) {
        gameover = board.checkWin(turnnum);
      }
    }
    if (turnnum == 10) {
      System.out.println("Draw!");
    } else if (turnnum % 2 == 0) {
      System.out.println("Player 1 has won!");
    } else {
      System.out.println("Computer has won!");
    }
    in.close();

  }

  public static void play(char player, Board board, Scanner in) {
    if (player == 'x') {
      System.out.println("Choose a valid spot (1-9):");
      // check for valid input
      while (!in.hasNextInt()) {
        System.out.println("That's not a number. Choose a valid spot (1-9):");
        in.next();
      }
      int spot = in.nextInt();
      while (spot < 1 || spot > 9 || board.getBoard(spot) == 'x' || board.getBoard(spot) == 'o') {
        System.out.println("Invalid spot; Choose a valid spot (1-9):");
        // check for valid input
        while (!in.hasNextInt()) {
          System.out.println("That's not a number. Choose a valid spot (1-9):");
          in.next();
        }
        spot = in.nextInt();
      }
      board.setBoard(spot, player);
    } else {
      // Computer generate number until valid
      Random rand = new Random();
      int spot = 1 + rand.nextInt(9);
      while (spot < 1 || spot > 9 || board.getBoard(spot) == 'x' || board.getBoard(spot) == 'o') {
        spot = 1 + rand.nextInt(9);
      }
      board.setBoard(spot, player);
    }
  }

}
