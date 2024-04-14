import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Vector;

public class Main {

    public static void main(String[] args) {
        Random random = new Random();
        Vector<Integer> vector = new Vector<>(128);
        for(int i = 0; i < 128; i++){
            vector.add(random.nextInt(2));
        }
        try{
            FileWriter f = new FileWriter("C:\\Users\\natal\\isb_lab1\\lab_2\\generate\\gen_random1.txt");
            for(Integer num : vector){
                f.write(num.toString());
                System.out.print(num.toString());
            }
            f.close();
        } catch (IOException e){
            System.out.print("Что-то пошло не так. Ошибка при записи в файл.");
        }
    }
}
