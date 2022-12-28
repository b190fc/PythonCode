import java.io.File;
import java.util.*;
import java.util.stream.*;


public class novels {
    static File DownloadDirectory;
    static File NovelDirectory;

    public static Set<String> listFilesUsingJavaIO(String dir) {
        return Stream.of(new File(dir).listFiles())
          .filter(file -> !file.isDirectory())
          .map(File::getName)
          .collect(Collectors.toSet());
    }

    public static void main(String[] args) {
        // system vairables
        System.out.println(args.length);

        if (args.length == 2) {


        }
        else {
            DownloadDirectory = new File("D:\\henry\\Files\\Desktop\\book buffer\\test");
            NovelDirectory = new File("D:\\henry\\Files\\Desktop\\book buffer\\test2");
        }
        
        //System.out.println(Arrays.toString(DownloadDirectory.listFiles()));
        //System.out.println(Arrays.toString(NovelDirectory.listFiles()));
        File[] testing1 = DownloadDirectory.listFiles();
        Object[] testing2 =  (Stream.of(DownloadDirectory.listFiles())
                        .filter(file -> !file.isDirectory())
                        .toArray());
         

        
        System.out.println("bbuffer");

        System.out.println(Stream.of(DownloadDirectory.listFiles())
                        .filter(file -> !file.isDirectory()).collect(Collectors.toList()));
                        // create a list of files
                        // filter files with isDirectory
                        // collect back into a list to use

                        //create code in java for novels
        
    }
        
}