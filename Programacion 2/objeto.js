const unObjeto = {fullName: "Ricardo Gonzalo Mathias",
                  frutas:["pera", "manzana", "melon"],
                  age: 20, city: "Buenos Aires", pesoEnKg: 70.4, soltero: true, hijos:null };
const jsonInString = JSON.stringify(unObjeto);

console.log("Hola el resultado es : " + jsonInString);

