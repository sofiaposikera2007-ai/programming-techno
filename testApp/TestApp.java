public class TestApp {
    public static void main(String[] args) {
      double a = 10;
      double b = 5;

      SimpleCalc sc = new SimpleCalc(a, b);


      System.out.println("a*b=" + sc.getMult());

      System.out.println("a/b=" + sc.getDiv());

    }
}