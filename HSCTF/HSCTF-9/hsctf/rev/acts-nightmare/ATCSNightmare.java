import java.util.*;

public class ATCSNightmare {

	public static String stackAttack(String in) {
		Stack<Character> s = new Stack<>();
		for (char c: in.toCharArray())
			s.push(c);
		String res = "";
		int i = 0;
		while (!s.isEmpty()) {
			res += (char)(s.pop() - i);
			i = (i + 1) % 4;
		}
		return res;
	}

    public static String stackAttackRev(String in) {
        String res = "";
        int decode = 0;
        for(int i = 0; i < in.length(); ++i){
            res += (char)(in.charAt(i) + decode);
            decode = (decode + 1) % 4;
        }
        String reversedString = "";
        for(int i = res.length()- 1; i >= 0; --i){
            reversedString += res.charAt(i);
        }
		return reversedString;
	}

	public static String recurses(String in, String out, int i) {
		if (in.isEmpty())
			return out;
		String res = out;
		if (i == 0){
			res += in.charAt(0);
            return recurses(in.substring(1), res, 1);
        }
		else
			res = in.charAt(1) + res;
		return recurses(in.charAt(0) + in.substring(2), res, 0);
	}

    public static String recursesRev(String in) {
        String res = "";
        int ptr1 = 0;
        int ptr2 = in.length() - 1;
        while(ptr1 < ptr2){
            res += in.charAt(ptr1);
            res += in.charAt(ptr2);
            ptr1 += 1;
            ptr2 -= 1;
        }

        String reversedString = "";
        for(int i = res.length()- 1; i >= 0; --i){
            reversedString += res.charAt(i);
        }
		return reversedString;
	}


	public static String linkDemLists(String in) {
		LinkedList<Character> lin = new LinkedList<>();
		for (char x: in.toCharArray())
			lin.add(x);
		String res = "";
		ListIterator<Character> iter = lin.listIterator(in.length()/2);
		while (iter.hasNext())
			res += iter.next();
		iter = lin.listIterator(in.length()/2);
		while (iter.hasPrevious())
			res += iter.previous();
		return res;
	}

    public static String linkDemListsRev(String in) {
		String res = "";
        for (int i = in.length() - 1; i >= in.length() / 2; --i){
            res += in.charAt(i);
        }
        for (int i = 0; i < in.length() / 2; ++i){
            res += in.charAt(i);
        }
		return res;
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String f = "flag{" + stackAttackRev(recursesRev(linkDemListsRev("20_a1qti0]n/5f642kb\\2`qq4\\0q"))) + "}";
		if (f.length() == 34 && f.substring(0, 4).equals("flag") && f.charAt(33) == '}') {
			f = f.substring(5, 33);
			if (linkDemLists(recurses(stackAttack(f), "", 1)).equals("20_a1qti0]n/5f642kb\\2`qq4\\0q")){
				System.out.println("Congrats! That is your flag!");
				System.out.println("flag{" + f + "}");
            } else
				System.out.println("Sorry, that is incorrect.");
		} else
			System.out.println("Sorry, that is incorrect.");
		in.close();
	}
}

// flag{th15_15nt_r0ck3t_sc1nc3_7272}