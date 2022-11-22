let addressNumber = "009";
let addressStreet = "lan09";
let country = "US";

let globaladdress = addressNumber+addressStreet+country;

console.log(globaladdress);

let birthYear = "1998";
let futureYear = "2099"
let age = futureYear -birthYear;

console.log("i will be " + age + " in "+ futureYear);

let pets = ["cat", "dog", "fish","rabbit","cow"];
console.log("dog") 

pets[3] = "horse"
console.log(pets)


let favorite = "pasta"
let meal = "dinner"
console.log("i will have "+ favorite + " for "+ meal);

let myWatchedSeries = ["money heist","black mirror", "big bang"];
let serieslength = [0,1,2];

console.log("The series i have watched " + myWatchedSeries);


let celsius = "90"

let fahrenheit =  celsius * 9 / 5 +32;

console.log(fahrenheit);

let c;
let a = 34;
let b = 21;

console.log(a+b);

a = 2;
console.log(a+b);

console.log(3 +4 + '5');

console.log(typeof(15));
console.log(typeof(5.5));
console.log(typeof(NaN));
console.log("johnny" - 5);
console.log(99 * "hello")
console.log(1 === "1");

console.log(1 === "1");
console.log(5 - "4");
console.log(10 % 5);
console.log(5 % 10);
console.log("Java" + "Script");
console.log(" " + " ");
console.log(" " + 0);
console.log(true + true);
console.log(false + true);
console.log("Bob" - "bill");

let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(' '));


const num1 = parseInt(prompt('Enter the first number '));
const num2 = parseInt(prompt('Enter the second number '));
const sum = num1 + num2;

// display the sum
console.log(`The sum of ${num1} and ${num2} is ${sum}`);
alert(`The sum of ${num1} and ${num2} is ${sum}`);


let fruits = ["Apples", "Oranges", "Blueberries","Banana"];
fruits.shift()
fruits.sort();
console.log(fruits);

