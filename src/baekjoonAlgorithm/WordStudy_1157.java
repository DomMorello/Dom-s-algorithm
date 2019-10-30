package baekjoonAlgorithm;

import java.io.*;
import java.util.Arrays;

/**
 * @author Dom_Morello
 * @Project Algorithm
 * @Date 2019. 10. 30.
 */
public class WordStudy_1157 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		char[] chArr = input.toCharArray();	//���ĺ� �迭�� ���ϱ� ���ؼ� char�迭����
		//���ĺ� �迭 ����
		char[] alphabet = new char[26];
		int[] count = new int[26];	//input�� ���Ե� ���ĺ��� ���� ���� �迭
		//���ĺ� �빮�ڷ� �ʱ�ȭ A~Z
		for(int i=0; i < alphabet.length; i++) {
			alphabet[i] = (char)(i+65);
		}
//		System.out.println(Arrays.toString(alphabet));
		//input���ڿ��� ���ĺ��� ��� �ݺ��ż� �����ϴ��� �˻�
		for(int i=0; i < chArr.length; i++) {
			for(int j=0; j < alphabet.length; j++) {
				if(chArr[i] == alphabet[j] || chArr[i] == alphabet[j]+32) {
					//�빮�ڶ� ���ų� �ҹ��ڶ� ������ �� ��ġ�� count�� 1���� ��Ų �� �ݺ��� break�Ѵ�.
					count[j]++;
					break;
				}
			}
		}
//		System.out.println(Arrays.toString(count));
		//count�迭���� �ִ��� �ϴ� ���غ���
		int max = count[0];
		for(int i=0; i < count.length; i++) {
			if(max < count[i]) {
				max = count[i];
			}
		}
//		System.out.println(max);
		//max���� ��ġ�ϴ� ��ġ�� char�� �̾ƶ�
		//dd
		int location = 0;
		int repeat = 0;
		for(int i=0; i < alphabet.length; i++) {
			if(max == count[i]) {
				repeat++;
				location = i;
			}
		}
//		System.out.println(location);
		if(repeat > 1) {
			System.out.println('?');
		}else {
			System.out.println(alphabet[location]);
		}
	}
}