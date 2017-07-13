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

function partnerSearch(name) {
    $.ajax({
        url: '/partner/'+name,
        type: 'GET',
        success: function(res) {
            var source  = [ ];
            var mapping = { };
            $.each(res, function(k, v) {
                source.push(v);
                mapping[v] = k;
            });
            
            $("#resellerSearchBox").autocomplete({
                source: source,
                select: function(e, ui) {
                    resellerId = mapping[ui.item.value];
                    $('#resellerSearchBox').val(resellerId);
                    customerSearch(resellerId);
                }
            });
        }, error: function(res) {
            console.log(res);
        }
    });
}

$(document).ready(function() {
    $('#resellerSearchBox').keyup(function(e) {
        e.preventDefault();
        partnerSearch($(this).val());
    });
});