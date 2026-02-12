function fact(num) {
    let facto = 1;
    for (let x = 2; x <= num; x++) {
        facto *=x
    }
    console.log(facto);
}
let n = prompt("Enter a number")
fact(n)