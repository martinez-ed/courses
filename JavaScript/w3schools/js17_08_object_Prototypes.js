// OBJECT PROTOTYPES ---------------------------------------------------
// The Object.prototype in on the top of the prototipe inheritance chain: Date objects, Array objects and Person objects inherit from Object.prototype.


//use the prototype property to add properties:
Person.prototype.nationality = 'English';
console.log('The nationality of my father is '+ myFather.nationality)


//use the prototype property to add new methods:
Person.prototype.name = function() {
  return this.firstName + ' ' + this.lastName;
};
console.log('My father is ' + myFather.name());
