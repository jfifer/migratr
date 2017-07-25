$(document).ready(function() {
    now = (new Date).getTime();
    $.ajax({
        url: "/migrations/"+now,
        type: 'GET',
        success: function(res) {
            console.log(res);
        }, error: function(res) {
            console.log("error", res);
        }
    });
});