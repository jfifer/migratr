var RESELLERID;
var CUSTOMERID;
var BRANCHID;

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
                    RESELLERID = mapping[ui.item.value];
                    $('#resellerSearchBox').val(RESELLERID);
                }
            });
        }, error: function(res) {
            console.log(res);
        }
    });
}

function customerSearch(name) {
    $.ajax({
        url: '/customer/'+RESELLERID+'/'+name,
        type: 'GET',
        success: function(res) {
            var source  = [ ];
            var mapping = { };
            $.each(res, function(k, v) {
                source.push(v);
                mapping[v] = k;
            });
            $("#customerSearchBox").autocomplete({
                source: source,
                select: function(e, ui) {
                    CUSTOMERID = mapping[ui.item.value];
                    $('#customerSearchBox').val(CUSTOMERID);
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
    $('#customerSearchBox').keyup(function(e) {
        e.preventDefault();
        customerSearch($(this).val());
    });
});