package Activities.a10.Q2;

public class Dog extends Mammal implements Animal {
  public Dog(String name) {
    super(name);
  }

  @Override
  public void makeSound() {
    System.out.println("Bark");
  }
}
