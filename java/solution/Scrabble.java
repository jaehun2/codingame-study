package solution;

import java.util.*;
import java.util.stream.Collectors;

public class Scrabble {

    public static void main(String[] args) {
        List<String> dictionary = new ArrayList<>();

        /*
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        for (int i = 0; i < N; i++) {
            String W = in.nextLine();
            dictionary.add(W);
        }
        String LETTERS = in.nextLine();
        */
        dictionary.add("because");
        dictionary.add("first");
        dictionary.add("these");
        dictionary.add("could");
        dictionary.add("which");
        dictionary.add("ichhwq");
        dictionary.add("ichhhw");
        String LETTERS = "hicquwh";

        // Write an action using System.out.println()
        // To debug: System.err.println("Debug messages...");

        //System.out.println("invalid word");

//        1. letters를 letterCounts로 만들기
//        2. 사전에 있는 단어를 만들수 있는지 판단하는 함수
//        3. 2번 함수를 이용하여 가능한 단어 리스트 리턴하는 함수
//        4. 3번 리스트에서 값 계산하여 변환 후 max 값 찾기

        // 1.
        Map<Character, Integer> letterCounts = makeLetterCounts(LETTERS);

        // 2.
        List<String> possibleWords = dictionary.stream().filter(word -> canBeMade(word, letterCounts)).collect(Collectors.toList());

        // 3.
        Map<Character, Integer> scoreMap = makeScoreMap();
        List<Integer> scores = possibleWords.stream().map(word -> calcScore(word, scoreMap)).collect(Collectors.toList());

        // 4.
        Integer maxScore = Collections.max(scores); // should return 7
        Integer maxIdx = scores.indexOf(maxScore);

        System.out.println(possibleWords.get(maxIdx));
    }

    private static Map<Character, Integer> makeLetterCounts(String letters) {
        Map<Character, Integer> letterCounts = new HashMap<>();

        for (int i = 0; i < letters.length(); i++) {
            char c = letters.charAt(i);
            int count = letterCounts.getOrDefault(c, 0);
            letterCounts.put(c, count + 1);
        }

        return letterCounts;
    }

    private static boolean canBeMade(String word, final Map<Character, Integer> letterCounts) {
        boolean result = true;
        Map<Character, Integer> copyLetterCounts = new HashMap<>(letterCounts);

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int count = copyLetterCounts.getOrDefault(c, 0);
            if (count == 0) {
                result = false;
                break;
            } else {
                copyLetterCounts.put(c, count - 1);
            }
        }

        return result;
    }

    private static int calcScore(String word, final Map<Character, Integer> scoreMap) {
        int score = 0;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int point = scoreMap.getOrDefault(c, 0);
            score += point;
        }

        return score;
    }

    private static Map<Character, Integer> makeScoreMap() {
        Map<Character, Integer> map = new HashMap<>();

        map.put('e', 1);
        map.put('a', 1);
        map.put('i', 1);
        map.put('o', 1);
        map.put('n', 1);
        map.put('r', 1);
        map.put('t', 1);
        map.put('l', 1);
        map.put('s', 1);
        map.put('u', 1);

        map.put('d', 2);
        map.put('g', 2);

        map.put('b', 3);
        map.put('c', 3);
        map.put('m', 3);
        map.put('p', 3);

        map.put('f', 4);
        map.put('h', 4);
        map.put('v', 4);
        map.put('w', 4);
        map.put('y', 4);

        map.put('k', 5);

        map.put('j', 8);
        map.put('x', 8);

        map.put('q', 10);
        map.put('z', 10);

        return map;
    }

}
