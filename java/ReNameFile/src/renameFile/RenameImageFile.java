package renameFile;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class RenameImageFile {

	static int cnt = 0;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			subDirList("D:/�ͻ�� ����/�ͻ��û ���� - ���纻/35mm ����/");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void subDirList(String source) throws IOException {
		File dir = new File(source);
		File[] fileList = dir.listFiles();
		
		for (int i=0; i<fileList.length; i++) {
			File file = fileList[i];
			if(file.isFile()) {
				System.out.println("\t ���� �̸�="+ file.getName());
				//Rename			
				file.renameTo(new File("D:/images/image_"+cnt+".jpg"));
				cnt++;
			} else if (file.isDirectory()) {
				System.out.println("���丮 �̸� = "+ file.getName());
				subDirList(file.getCanonicalPath().toString());
			}
		}
	}

}
