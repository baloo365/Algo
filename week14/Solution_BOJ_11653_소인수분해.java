import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

// n개의 수를 입력 받고 가능한 모든 부분집합 생성
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int i = 2;
		
		while (N!=1) {
			if(N % i ==0) {
				N = N/i;
				sb.append(i + "\n");
			} else {
				i++;
			}
				
		}
		
		System.out.println(sb);
	}
	
}
