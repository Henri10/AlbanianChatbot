$(document).ready(function() {
    $("#chat-widget-button").on("click", function(){
        $("#chat-widget").toggleClass("d-none");
    });

    $("#chat-widget-close-button").on("click", function(){
        $("#chat-widget").addClass("d-none");
    });

    $("#chat-widget-input").keypress(function(event){
        if(event.which === 13){
            let userMessage = $("#chat-widget-input").val();
            $("#chat-widget-input").val("");

            $("#chat-widget-messages").append("<div><strong>You: </strong> " + userMessage + "</div>");

            $.ajax({
                type: "POST",
                url: "/webhook",
                contentType: "application/json",
                data: JSON.stringify({message: userMessage}), // Change "messages" to "message"
                success: function(data){
                    let botResponse = data.response;

                    $("#chat-widget-messages").append("<div><strong>Bot:</strong> " + botResponse + "</div>");
                },
                error: function(){
                    // Handle error
                }
            });
        }
    });
});
