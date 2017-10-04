package java_hashmap;

import java.util.HashMap;
import java.util.Random;

class Main {
    public static void main(String args[]) {
        int size = Integer.parseInt(args[0]);

        HashMap<Integer, Integer> subject = new HashMap<Integer, Integer>();
        Random rand = new Random();

        for (int i = 0; i < size; i++) {
            subject.put(i + (size * (rand.nextInt(size))), i);
        }
    }
}
