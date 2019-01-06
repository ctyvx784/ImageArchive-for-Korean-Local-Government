package api;

public class Keyword {
	public void keTest(String a) {

		// string to extract keywords

		org.snu.ids.kkma.index.KeywordExtractor ke = new org.snu.ids.kkma.index.KeywordExtractor();
		// extract keywords

		org.snu.ids.kkma.index.KeywordList kl = ke.extractKeyword(a, true);

		// print result
		for (int i = 0; i < kl.size(); i++) {
			org.snu.ids.kkma.index.Keyword kwrd = kl.get(i);
			System.out.println(kwrd.getString() + "\t" + kwrd.getCnt());
		}

	}
}
