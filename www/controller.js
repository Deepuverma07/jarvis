$(document).ready(function () {

    // Display Speak Message

    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
        // textillate for text animate then agian reset so use start
    }

    // Display Hood
eel.expose(ShowHood)
function ShowHood() {
    $("#Oval").attr("hidden", false);
    $("#Siriwave").attr("hidden", true);
}
});





