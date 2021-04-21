$(function() {
    $("#unbook-form").submit(function(event) {
        // Stop form from submitting normally
        event.preventDefault();
        var unbookForm = $(this);
        // Send the data using post
        var posting = $.post( unbookForm.attr('action'), unbookForm.serialize() );
        // if success:
        posting.done(function(data) {
            console.log("Successfully cancelled")
            
        });
        // if failure:
        posting.fail(function(data) {
            console.log("Failed to cancel")
        });
    });
});

$("#exampleModal").prependTo("body");