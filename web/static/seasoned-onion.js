let model;
function* enumerate (it, start = 0)
{ let i = start
  for (const x of it)
    yield [i++, x]
}

(async function() {
    model = await tf.loadModel('http://localhost:81/tfjs_model/model.json');
    $('progress-bar').hide();
})();

var content = document.getElementById("input-text").value;
var button = document.getElementById("generate-button");
var chars = ["", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+" , "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "=", ">", "?", "@", "[ ]", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
button.onclick = function(){
    let generated = "";
    let sentence = "blah"; // textbox
    
    for ( let i = 0; i < 400; i++) {
        let x_pred = nj.zeros([1, 40, 61]);
        for (const[i, x] of enumerate(sentence)){
            console.log(i,x);
            x_pred[0, x, ]
            let preds = model.predict(x_pred, verbose=0)[0]
        }
    }
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