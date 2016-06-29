import java.util.InputMismatchException;
import java.util.Scanner;

public class PizzaDelivery {
    public static void main(final String[] args) {
        try {
            new PizzaDelivery().run();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private final Scanner scanner;
    private int nrOfColumns, nrOfRows, currWay, shortWay, distance = 0;
    private static int town[][];


    public PizzaDelivery() {
        this.scanner = new Scanner(System.in);
    }


    public void run() {
        int nrOfTestCases = scanner.nextInt();

        if(nrOfTestCases < 1 || nrOfTestCases > 20) {
            throw new InputMismatchException("Number of test cases must be between 1-20");
        }

        for(int i=0; i<nrOfTestCases; i++) {
            testCaseExecution();
        }
    }

    private void testCaseExecution() {
        nrOfColumns = scanner.nextInt();
        if(nrOfColumns < 1 || nrOfColumns > 100) {
            throw new InputMismatchException("Value must be between 1-100");
        }

        nrOfRows = scanner.nextInt();
        if(nrOfRows < 1 || nrOfRows > 100) {
            throw new InputMismatchException("Value must be between 1-100");
        }

        town = new int[nrOfRows][nrOfColumns];

        for(int x=0; x<nrOfRows; x++){
            for(int y=0; y<nrOfColumns; y++){
                town[x][y] = scanner.nextInt();
                if(town[x][y] < 0 || town[x][y] > 1000) {
                    throw new InputMismatchException("Value must be between 1-1000");
                }
            }
        }

        shortWay = Integer.MAX_VALUE;
        for(int x=0; x<nrOfRows; x++){
            for(int y=0; y<nrOfColumns; y++){

                currWay = nrOfBlocksFromPos(x, y);

                if(currWay < shortWay){
                    shortWay = currWay;
                }
            }
        }
        System.out.println(shortWay+" blocks");
    }

    private int nrOfBlocksFromPos(final int column, final int row){
        distance = 0;

        for(int x=0; x<nrOfRows; x++){
            for(int y=0; y<nrOfColumns; y++){
                if(town[x][y] > 0){
                    distance += town[x][y]*(Math.abs(x-column) + Math.abs(y-row));
                }
            }
        }
        return distance;
    }

    public class Tuple<X, Y> {
        public final X x;
        public final Y y;
        public Tuple(X x, Y y) {
            this.x = x;
            this.y = y;
        }
    }
}

