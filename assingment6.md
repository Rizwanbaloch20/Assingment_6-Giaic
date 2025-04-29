 Traditional OOP Practice Series: Build, Compose, and Decorate
Part 1: Basic Class & Object Creation
Focus: Class blueprint, attributes, methods, creating objects.

Example: Create a Car class with brand, model, and a drive() method.

Exercises:

Create a Book class.

Create a Student class that can enroll in courses.

Part 2: Encapsulation: Protecting Data
Focus: Private attributes, getter/setter methods.

Example: Make balance private in a BankAccount class, and allow deposits/withdrawals through methods.

Exercises:

Create a PasswordManager class that hides passwords internally.

Create a Profile class with private email and phone.

Part 3: Inheritance: Reusing Code
Focus: Parent (Base) classes and Child (Derived) classes.

Example:

Animal → Dog, Cat

Base class defines breathe(), child classes define sound().

Exercises:

Vehicle → Car, Bike, Truck

Employee → Manager, Engineer, Intern

Part 4: Polymorphism: One Interface, Many Forms
Focus: Method overriding, dynamic behavior.

Example:

Shape class with area() method → overridden in Circle, Square, Rectangle.

Exercises:

Payment method overridden in CreditCardPayment, PaypalPayment.

Notification class → EmailNotification, SMSNotification.

Part 5: Abstract Classes and Interfaces
Focus: Forcing child classes to implement common methods.

Example:

Abstract class Appliance with an abstract method turn_on().

Exercises:

Abstract class Document with methods save() and load().

Abstract class Animal with move() and eat().

Part 6: Composition: Building with Components (HAS-A Relationship)
Focus: One class owns objects of another class.

Example:

Car HAS-A Engine.

House HAS-A Room.

Exercises:

Computer HAS-A CPU, GPU.

Library HAS-A list of Book objects.

Part 7: Decorator Pattern: Adding Functionality Dynamically
Focus: Classic design pattern to "decorate" objects.

Example:

Create a Coffee class, and add Milk, Sugar, WhippedCream dynamically using decorators.

Exercises:

Create a Pizza class with decorators for Cheese, Olives, Pepperoni.

