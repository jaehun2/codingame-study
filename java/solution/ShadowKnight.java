package solution;

import java.util.*;
import java.io.*;
import java.math.*;

public class ShadowKnight {

    static int minX, maxX, minY, maxY;

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int W = in.nextInt(); // width of the building.
        int H = in.nextInt(); // height of the building.
        int N = in.nextInt(); // maximum number of turns before game over.
        int X0 = in.nextInt();
        int Y0 = in.nextInt();

        minX = 0;
        minY = 0;
        maxX = W - 1;
        maxY = H - 1;

        // game loop
        while (true) {
            String bombDir = in.next(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");

            int[] nextPos = nextPos(X0, Y0, bombDir);

            X0 = nextPos[0];
            Y0 = nextPos[1];

            // the location of the next window Batman should jump to.
            System.out.println(X0 + " " + Y0);
        }
    }

    private static int[] nextPos(final int x, final int y, final String direction) {
        int nx = x;
        int ny = y;

        switch (direction) {
            case "U":
                ny = calcU(y);
                break;
            case "UR":
                ny = calcU(y);
                nx = calcR(x);
                break;
            case "R":
                nx = calcR(x);
                break;
            case "DR":
                ny = calcD(y);
                nx = calcR(x);
                break;
            case "D":
                ny = calcD(y);
                break;
            case "DL":
                ny = calcD(y);
                nx = calcL(x);
                break;
            case "L":
                nx = calcL(x);
                break;
            case "UL":
                ny = calcU(y);
                nx = calcL(x);
                break;
            default:
                break;
        }

        int[] result = {nx, ny};
        return result;
    }

    private static int calcU(int y) {
        int result = y - ((y - minY) / 2 + 1);
        maxY = y;
        return result;
    }

    private static int calcD(int y) {
        int result;
        if (maxY == 2) {
            result = y + ((maxY - y) / 2);
        } else {
            result = y + ((maxY - y) / 2 + 1);
        }
        minY = y;
        return result;
    }

    private static int calcL(int x) {
        int result = x - ((x - minX) / 2 + 1);
        maxX = x;
        return result;
    }

    private static int calcR(int x) {
        int result;
        if (maxX == 2) {
            result = x + ((maxX - x) / 2);
        } else {
            result = x + ((maxX - x) / 2 + 1);
        }
        minX = x;
        return result;
    }
}