import java.util.ArrayList;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public final class PhoneList {

    /**
     * Starts here!
     * @param args
     */
    public static void main(final String[] args) {
        try {
            new PhoneList().run();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private final Scanner scanner;
    private int nrOfTestCases;
    private int nrOfRows;
    private String newRow;
    private List<String> listOfPhoneNumbers;

    /**
     * Constructor. New instance of PhoneList.
     */
    public PhoneList() {
        this.scanner = new Scanner(System.in);
        this.listOfPhoneNumbers = new ArrayList<String>();
    }

    /**
     * Run method for PhoneList.
     */
    public void run() {
        nrOfTestCases = scanner.nextInt();

        if(nrOfTestCases < 1 || nrOfTestCases > 40) {
            throw new InputMismatchException("Number of test cases must be between 1-40");
        }

        for(int i=0; i<nrOfTestCases; i++) {
            testCaseExecution();
        }
    }

    //One test case execution. Takes one line with an integer which specifies the number of phone numbers
    //and then x number of phone numbers each on a new row.
    private void testCaseExecution() {
        nrOfRows = scanner.nextInt();
        listOfPhoneNumbers = new ArrayList<String>();

        if(nrOfRows < 1 || nrOfRows > 10000) {
            throw new InputMismatchException("Number of phone numbers must be between 1-10000");
        }

        for(int i=0; i<nrOfRows; i++) {
            newRow = scanner.next();
            if(newRow.length() > 10) {
                throw new InputMismatchException("Phone number must me less than 10 digits");
            }
            listOfPhoneNumbers.add(newRow);
        }

        Collections.sort(listOfPhoneNumbers);

        if(isListConsistent()) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }

    private boolean isListConsistent() {
        for(int a=1; a<nrOfRows; a++) {
            if(listOfPhoneNumbers.get(a).startsWith(listOfPhoneNumbers.get(a-1))) {
                return true;
            }
        }

        return false;
    }
}
