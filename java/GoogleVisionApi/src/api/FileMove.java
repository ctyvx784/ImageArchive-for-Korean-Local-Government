package api;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

public class FileMove {
	ArrayList<String> as = new ArrayList<String>();
	
	public void subDirList(String source) throws IOException, InterruptedException {
		File dir = new File(source);
		File[] fileList = dir.listFiles();
		
		for (int i = 0; i < fileList.length; i++) {
			File file = fileList[i];
			if (file.isFile()) {
				as.add(file.getName());
				System.out.println("\t 파일 이름=" +file.getName());
				// Rename
				//temp = ocr(source+file.getName());
				//System.out.println(temp);
				//System.out.println(ocr(source+file.getName()));
			}
			Thread.sleep(500);
		}
	}
}
