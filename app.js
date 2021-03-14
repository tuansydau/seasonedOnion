let model;
(async function() {
    model = await tf.loadModel('http://localhost:81/tfjs_model/model.json');
    $('progress-bar').hide();
})();
$("generate-button").click(async function () {

});
