// 1. Importacion de modulos
import saludar, { Saludar, PI, user } from './constants.js';
import { arithmetic as ari } from './arithmetic.js';

// 2. Declaracion de variables

// 3. declaración de funciones
// 4. Ejecución de código - Inicialización de funciones
console.log('Archivos modules.js');
console.log(PI, user);
// console.log(arithmetic.add(1, 2));
// console.log(arithmetic.substract(1, 2));
console.log(ari.add(1, 2));
console.log(ari.substract(1, 2));

saludar();

let saludo = new Saludar('Juan');
saludo.saludar();