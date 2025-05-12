package Activities.a10.Q2;
// interface Animal {

//   void makeSound();
// }

// abstract class Mammal {
//   String name;

//   public Mammal(String name) {
//     this.name = name;
//   }

//   public String getName() {
//     return name;
//   }
// }

// class Dog extends Mammal implements Animal {
//   public Dog(String name) {
//     super(name);
//   }

//   @Override
//   public void makeSound() {
//     System.out.println("Bark");
//   }
// }

// Main class to test the implementation
public class q2 {
  public static void main(String[] args) {
    Dog dog = new Dog("Buddy");
    System.out.println("Dog's name is: " + dog.getName());
    dog.makeSound();
  }
}