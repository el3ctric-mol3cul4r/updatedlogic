function vowels(word) {
    let letters = word.split("");
    let count = 0;

    for (let x of letters) {
        if (["a", "e", "i", "o", "u"].includes(x)) {
            count = count + 1;
            continue;
        } else {
            continue;
        }
    }

    console.log(count);
}

let w = prompt("Give me a word:");
vowels(w)
