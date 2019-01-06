package api;

import java.util.List;

import org.snu.ids.*;

public class KeywordExtractExample {
	public static void main(String[] args) {
		keTest();
	}

	public static void keTest() {

		// string to extract keywords
		String strToExtrtKwrd = "기획 전시실 귀금속·보석 기증 및 개인 소 장 품";
		
		org.snu.ids.kkma.index.KeywordExtractor ke = new org.snu.ids.kkma.index.KeywordExtractor();
		// extract keywords
		org.snu.ids.kkma.index.KeywordList kl = ke.extractKeyword(strToExtrtKwrd, true);
		
		// print result
		for( int i = 0; i < kl.size(); i++ ) {
			org.snu.ids.kkma.index.Keyword kwrd = kl.get(i);
			System.out.println(kwrd.getString() + "\t" + kwrd.getCnt());
		}
	}

}
