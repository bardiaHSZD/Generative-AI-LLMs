const person = {
  name: 'Max',
  age: 29,
  greet() {
    console.log('Hi, I am ' + this.name + '. I am ' + this.age + ' yrs old.');
  }
};

person.greet();
console.log('// ---------------------------------------------------------------------------')

const hobbies = ['Sports', 'Cooking'];
for (let hobby of hobbies) {
    console.log(hobby);
}
console.log(hobbies.map(hobby => 'Hobby: ' + hobby));
console.log(hobbies);
hobbies.push('programming')
console.log(hobbies)

console.log('// ---------------------------------------------------------------------------')

const copiedPerson = { ...person };
console.log(copiedPerson);

const copiedArray = [...hobbies];
console.log(copiedArray);

const toArray = (...args) => {
  return args;
};

console.log(toArray(1, 2, 3, 4));

console.log('// ---------------------------------------------------------------------------')

const printName = ({ name }) => {
  console.log(name);
};
printName(person);

const { name, age } = person;
console.log(name, age);

const [hobby1, hobby2] = hobbies;
console.log(hobby1, hobby2);