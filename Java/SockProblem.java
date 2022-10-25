import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** Sock Problem - count the number of pairs sock. The array number ar represents the color */

public class SockProblem {

	public static void main(String[] args) {
		List<Integer> ar = new ArrayList<>(Arrays.asList(10, 20, 20, 10, 10, 30, 50, 10, 20));

		Map<Integer, Integer> pairs = new HashMap<>();

		ar.forEach(num -> {
			if (pairs.containsKey(num)) {
				pairs.put(num, pairs.get(num) + 1);
			} else {
				pairs.put(num, 1);
			}
		});

		int pairCount = 0;

		List<Integer> count = new ArrayList<Integer>(pairs.values());

		for (int i = 0; i < count.size(); i++) {

			pairCount += count.get(i) / 2;
		}

		System.out.println(pairCount);
	}

}
