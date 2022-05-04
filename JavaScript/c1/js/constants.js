export const PI = Math.PI;

export let user = 'Juan';

const password = '123';
// export default password;

export default function saludar() {
  console.log('Hola ' + user);
}

export class Saludar {
  constructor(nombre) {
    this.nombre = nombre;
  }

  saludar() {
    console.log(`Hola como estas ${this.nombre}`);
  }
}