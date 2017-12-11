var ride = function(formSelector) {
    var url = "/ride"; // the script where you handle the form input.
    $.ajax({
       type: "POST",
       url: url,
       data: $(formSelector).serialize(), // serializes the form's elements.
       success: function(res) {
           console.log(res);
           $('#res-status-alert').html(res.message);
           $('#res-status-alert').fadeIn();
       },
       error: function (e) {
           $('#res-status-alert').html("Error while submitting ride request.");
           $('#res-status-alert').fadeIn();
       }
     });

    return false;
}