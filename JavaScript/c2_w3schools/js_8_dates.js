// "new Date()" creates a new Date object with the current date and time.
const d = new Date(); //constructor
console.log('Current date: ' + d);


// "new Date(year, month, day, hours, minutes, seconds, milliseconds)" creates a new Date object with the specified date and time.
const d2 = new Date(1981, 3, 25, 11, 30, 0, 0);
console.log('Specified date: ' + d2);
const d2_2 = new Date(81, 3);
console.log('Year and month: ' + d2_2);


// "new Date(dateString)" creates a new Date object from a date string.
const d3 = new Date('April 25, 1981');
console.log('Date string: ' + d3);


// "new Date(milliseconds)" creates a new Date object from the specified number of milliseconds.
const d4 = new Date(86400000);
console.log('Milliseconds: ' + d4);


// Displaying Dates
// "toString()" returns a string representing the specified date.
const d5 = new Date();
console.log('toString(): ' + d5.toString());

// "toDateString()" converts a date to a more readable format.
const d6 = new Date();
console.log('toDateString(): ' + d6.toDateString());

// "toUTCString()" converts a date to a UTC (Universal Coordinated Time) date string.
const d7 = new Date();
console.log('toUTCString(): ' + d7.toUTCString());

// "toISOString()" converts a date to an ISO 8601 string.
const d8 = new Date();
console.log('toISOString(): ' + d8.toISOString());


// Short Dates
const d9 = new Date('04/25/1981');
console.log('Short date: ' + d9);


// Long Dates
const d10 = new Date('25 April 1981');
console.log('Long date: ' + d10);


// Date Input - Parsing Dates
// "Date.parse()" parses a date string and returns the number of milliseconds since January 1, 1970, 00:00:00 UTC.
let msec = Date.parse('April 25, 1981');
console.log('Date.parse(): ' + msec);

// Convert milliseconds to date:
const d11 = new Date(msec);
console.log('Convert milliseconds to date: ' + d11.toDateString());



// GET DATE METHODS:

// "getTime()" returns the number of milliseconds elapsed since 1 January 1970 00:00:00 UTC.
const d12 = new Date();
console.log('getTime(): ' + d12.getTime());


// "getFullYear()" returns the year of the specified date according to local time.
const d13 = new Date();
console.log('getFullYear(): ' + d13.getFullYear());


// "getMonth()" returns the month of a date as a number (0-11).
const d14 = new Date();
console.log('getMonth(): ' + d14.getMonth());
//e.g. use an array of names for months:
const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
let month = months[d14.getMonth()];
console.log('getMonth(): ' + month);


// "getDate()" returns the day of a date as a number (1-31).
const d15 = new Date();
console.log('getDate(): ' + d15.getDate());


// "getDay()" returns the day of a date as a number (0-6).
const d16 = new Date();
console.log('getDay(): ' + d16.getDay());
//e.g. use an array of names for days:
const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
let day = days[d16.getDay()];
console.log('getDay(): ' + day);


// "getHours()" returns the hour of a date as a number (0-23).
const d17 = new Date();
console.log('getHours(): ' + d17.getHours());


// "getMinutes()" returns the minutes of a date as a number (0-59).
const d18 = new Date();
console.log('getMinutes(): ' + d18.getMinutes());


// "getSeconds()" returns the seconds of a date as a number (0-59).
const d19 = new Date();
console.log('getSeconds(): ' + d19.getSeconds());


// "getMilliseconds()" returns the milliseconds of a date as a number (0-999).
const d20 = new Date();
console.log('getMilliseconds(): ' + d20.getMilliseconds());



// SET DATE METHODS:

// "setFullYear()" sets the year of a date object.
const d21 = new Date();
console.log('setFullYear(): ' + d21.setFullYear(1981));

// "setMonth()" sets the month of a date object.
const d22 = new Date();
console.log('setMonth(): ' + d22.setMonth(3));

// "setDate()" sets the day of a date object.
const d23 = new Date();
let addDays = d23.setDate(d23.getDate() + 50);
console.log('setDate(): ' + addDays);

// "setHours()" sets the hours of a date object.
// "setMinutes()" sets the minutes of a date object.
// "setSeconds()" sets the seconds of a date object.
// "setMilliseconds()" sets the milliseconds of a date object.


// Compare Dates
let text = '';
const today = new Date();
const someday = new Date();

someday.setFullYear(2100, 0, 14);
if (someday > today) {
  text = 'Today is before January 14, 2100.';
} else {
  text = 'Today is after January 14, 2100.';
}
console.log(text);

// someday.setFullYear(someday.getFullYear() + 1);
// if (today.getTime() < someday.getTime()) {
//     text = 'Today is before the future.';
// } else {
//     text = 'Today is after the future.';
// }
// console.log(text);
