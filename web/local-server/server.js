let express = require("express");
let app = express();
const tf = require("@tensorflow/tfjs-node");
const n = tf.tensor;

app.use(function(req, res, next) {
    console.log(`${new Date()} - ${req.method} request for ${req.url}`);
    next();
});

app.use(express.static("../static"));

app.listen(100, function() {
    console.log("Serving static on 81");
})