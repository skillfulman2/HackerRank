abstract class Animal {
    abstract void sayHello();

    public static void main (String [] args) {
        Animal animal = new Animal();
        System.out.println("hello");
        animal.sayHello();
    }
}

