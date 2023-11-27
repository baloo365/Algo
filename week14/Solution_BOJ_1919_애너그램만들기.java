import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


// n개의 수를 입력 받고 가능한 모든 부분집합 생성
public class Main {
	
	public static int[] getAlphabetCount(String str) {
		int[] count = new int[26];
		
		for (int i = 0; i < str.length(); i++) {
		count[str.charAt(i) - 'a']++;
		}
		return count;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String T1 = br.readLine();
		String T2 = br.readLine();
		int number[] = getAlphabetCount(T1);
		int number2[] = getAlphabetCount(T2);
		int sum = 0;
			
			
			
			for (int i = 0; i < 26; i++) 
				sum += Math.abs(number[i] - number2[i]);
			
			    System.out.println(sum);
				
}
}

