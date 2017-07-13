function login() {
    $.ajax({
        url: '/login',
        data: $('.form-signin').serialize(),
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function partnerSearch() {
    $.ajax({
        url: '/partnerSearch',
        data: $('#partnerSearch').serialize(),
        type: 'POST',
        success: function(res) {
            console.log(res);
        }, error: function(res) {
            console.log(res);
        }
    });
}

$(document).ready(function() {
    $('#targetPartnerSearch').click(function(e) { e.preventDefault(); partnerSearch(); });
});