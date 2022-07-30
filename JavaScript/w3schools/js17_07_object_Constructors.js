// OBJECT CONSTRUCTOR --------------------------------------------------
// It is a function that is used to create objects.
// Good practice to name constructor functions with an upper-case first letter.
// In a constructor function "this" refers to the newly created object.

//constructor function for Person objects:
class Person {
  constructor(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
  }
}

//create a Person object:
const myFather = new Person('Jose', 'Martinez', 71, 'brown');
const myMother = new Person('Elena', 'Moreno', 72, 'blue');

console.log('My father and mother names are: ' + myFather.firstName + ' ' + myFather.lastName + ' and ' + myMother.firstName + ' ' + myMother.lastName); // My father and mother names are: Jose Martinez and Elena Moreno

//adding a property to the object:
// myFather.nationality = 'Colombian';
console.log(myFather); // Person {firstName: "Jose Antonio", lastName: "Martinez", age: 71, eyeColor: "brown", nationality: "Colombian"}
