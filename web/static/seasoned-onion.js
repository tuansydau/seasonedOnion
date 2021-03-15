
/*
function* enumerate(it, start = 0) {
    let i = start
    for (const x of it)
        yield [i++, x]
}
*/

import tf from "@tensorflow/tfjs-node";

let model;
(async function () {
    model = await tf.loadModel('http://localhost:81/tfjs_model/model-2.json');
    $('progress-bar').hide();
})();

var content = document.getElementById("input-text").value;

var button = document.getElementById("generate-button");
/*
var chars = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "=", ">", "?", "@", "[ ]", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
var dict = [];
*/

/*
for (var j = 0; j < 61; j++) {
    dict.push({
        key: chars[j],
        value: j
    });
}
*/
button.onclick = function () {
    let next_char = tf.constant(['test']);
    let result = [next_char];

    for (let i = 0; i < 1000; i++) {
        next_char, states = model.generate_one_step(next_char, states = None);
        result = result.concat(next_char);
    }
    result = tf.strings.join(result)
    console.log(result);
}
/*

for i in range(400):
    x_pred = np.zeros((1, maxlen, len(chars)))
    print(x_pred)
    for t, char in enumerate(sentence):
        x_pred[0, t, char_indices[char]] = 1.0
    preds = model.predict(x_pred, verbose=0)[0]
#        print(preds)
    next_index = sample(preds, diversity)
    next_char = indices_char[next_index]
    sentence = sentence[1:] + next_char
    generated += next_char

print("...Generated: ", generated)
print()


})();
*/