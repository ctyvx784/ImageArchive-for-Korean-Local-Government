package api;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.google.cloud.vision.v1.AnnotateImageRequest;
import com.google.cloud.vision.v1.AnnotateImageResponse;
import com.google.cloud.vision.v1.BatchAnnotateImagesResponse;
import com.google.cloud.vision.v1.EntityAnnotation;
import com.google.cloud.vision.v1.Feature;
import com.google.cloud.vision.v1.Image;
import com.google.cloud.vision.v1.ImageAnnotatorClient;
import com.google.cloud.vision.v1.Feature.Type;
import com.google.protobuf.ByteString;

public class ThreadOCR extends Thread{
	
	private String inputPath;
	private String outputStr;
	
	public ThreadOCR(String inputPath) {
		this.inputPath = inputPath;
	}
	
	public void setPath(String inputPath)
	{
		this.inputPath = inputPath;
	}
	
	public String getStr()
	{
		return this.outputStr;
	}
	public void ocr() throws FileNotFoundException, IOException, InterruptedException {
		String str = "";
		List<AnnotateImageRequest> requests = new ArrayList<>();
		ByteString imgBytes = ByteString.readFrom(new FileInputStream(this.inputPath));

		Image img = Image.newBuilder().setContent(imgBytes).build();
		Feature feat = Feature.newBuilder().setType(Type.TEXT_DETECTION).build();
		AnnotateImageRequest request = AnnotateImageRequest.newBuilder().addFeatures(feat).setImage(img).build();
		requests.add(request);

		try (ImageAnnotatorClient client = ImageAnnotatorClient.create()) {
			BatchAnnotateImagesResponse response = client.batchAnnotateImages(requests);
			List<AnnotateImageResponse> responses = response.getResponsesList();

			for (AnnotateImageResponse res : responses) {
				if (res.hasError()) {
					System.out.printf("Error: %s\n", res.getError().getMessage());
					return;
				}
				for (EntityAnnotation annotation : res.getTextAnnotationsList()) {
					str = str + annotation.getDescription();
				}

				// System.out.println(str);
				/*
				 * for (int i = 0; i < res.getTextAnnotationsCount(); i++) { str = str +
				 * res.getTextAnnotations(i).getDescription(); } System.out.println(str);
				 */

				// For full list of available annotations, see http://g.co/cloud/vision/docs
				/*
				 * for (EntityAnnotation annotation : res.getTextAnnotationsList()) { // str =
				 * str + annotation.getDescription(); System.out.printf("Text: %s\n",
				 * annotation.getDescription());
				 * 
				 * // System.out.println(annotation); temp.add(annotation.getDescription());
				 * 
				 * // System.out.printf("Position : %s\n", annotation.getBoundingPoly()); }
				 * 
				 * System.out.println("--------------------------------------------------------"
				 * );
				 */

				// keTest(str);
			}
		}
		this.outputStr = str;
	}
	
	public void run() 
	{
		try {
			ocr();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
