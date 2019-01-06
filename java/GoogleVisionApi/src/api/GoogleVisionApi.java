package api;

import com.google.cloud.vision.v1.ImageAnnotatorClient;
import com.google.cloud.vision.v1.AnnotateImageRequest;
import com.google.cloud.vision.v1.AnnotateImageResponse;
import com.google.cloud.vision.v1.BatchAnnotateImagesResponse;
import com.google.cloud.vision.v1.EntityAnnotation;
import com.google.cloud.vision.v1.Feature;
import com.google.cloud.vision.v1.Feature.Type;
import com.google.cloud.vision.v1.Image;
import com.google.protobuf.ByteString;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import java.util.List;

import org.snu.ids.*;

public class GoogleVisionApi {
	public static void main(String[] args) throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		subDirList("D://test//");
	}

	public static void subDirList(String source) throws IOException, InterruptedException {
		OCRTest ocrtest = new OCRTest();
		Keyword keyword = new Keyword();

		String temp = null;													//OCRTest ����� ���� ����
		ArrayList<String> arrayNon = new ArrayList<>();						//OCR������� ���� �̹��� ����
		ArrayList<String> arraySuccess = new ArrayList<>();					//OCR������� �ִ� �̹��� ����
		File dir = new File(source);
		File[] fileList = dir.listFiles();

		try {
			System.out.println("ocrStart");
			for (File file : fileList) {									

				temp = ocrtest.ocr(source + file.getName());				//OCR ����
		
				/*if (temp.equals("")) {
					System.out.println("Non: \t ���� �̸�=" + file.getName());
					arrayNon.add(file.getName());
				} else {
					System.out.println("Success: \t ���� �̸�=" + file.getName());
					arraySuccess.add(file.getName());
				}*/
				System.out.println(temp);
				//keyword.keTest(temp);
			}
			
			System.out.println("ocrEnd");
//-------------------------------------------------------------------------------------------------------
			/*System.out.println("moveStart");
			for (File file2 : fileList) {
				for (String successPath : arraySuccess) {
					if (file2.getName().equals(successPath)) {
						file2.renameTo(new File("F://success_ocr//" + file2.getName()));
					}
				}
				for (String nonPath : arrayNon) {
					if (file2.getName().equals(nonPath)) {
						file2.renameTo(new File("F://non_ocr//" + file2.getName()));
					}
				}
			}*/

		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//System.out.println("moveEnd");
	}
}