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
		
		while(true) {
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		
		if(A == 0 && B == 0) break;
		
		if(B%A == 0) {
			System.out.println("factor");
		} else if (A%B == 0) {
			System.out.println("multiple");
		} else {
			System.out.println("neither");
		}
		
		
		}
	}
	
}
