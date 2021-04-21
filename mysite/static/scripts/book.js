//triggered when modal is about to be shown
$('#exampleModal').on('show.bs.modal', function(e) {

    //get data-id attribute of the clicked element
    var offeringId = $(e.relatedTarget).data('id');

    $("#offering-id").val(offeringId);
    //populate the textbox
    console.log("FOUND ID: " + offeringId);
    var fee = $(e.relatedTarget).data('fee');
    if (fee > 0){
        $("#paymentArea").show();
        $("#freeOffering").hide();

        console.log("FEE: " + fee);
    } else {
        console.log("FREE")
        $("#paymentArea").hide();
        $("#freeOffering").show();
    }
});
console.log("page loaded")

$("#exampleModal").prependTo("body");
$("#addOfferingModal").prependTo("body");

$(function() {
    $("#book-form").submit(function(event) {
        $('#status-message').hide();
        // Stop form from submitting normally
        event.preventDefault();
        var unbookForm = $(this);
        // Send the data using post
        var posting = $.post( unbookForm.attr('action'), unbookForm.serialize() );
        // if success:
        posting.done(function(data) {
            console.log("booked!!");
            // $('#exampleModal').modal('hide');
           showSuccessMessage();

            
        });
        // if failure:
        posting.fail(function(data) {

            showFailureMessage();
        });
    });
});

function reloadPage(){
    location.reload();
}

function showFailureMessage() {
    $('#status-message').removeClass('alert-success');
    $('#status-message').addClass('alert-danger');
    $('#status-message').text = "Failed to cancel";
    $('#status-message').show();
}

function showSuccessMessage() {
    $('#status-message').removeClass('alert-danger');
    $('#status-message').addClass('alert-success');
    $('#status-message').text = "Book successful";
    $('#status-message').show();
}