function getContextByCustomer(customerId) {
    $("#pbxSearchBox").val(null);
    $.ajax({
        url: '/pbx/'+customerId,
        type: 'GET',
        success: function(res) {
            var source  = [ ];
            var mapping = { };
            $.each(res, function(k, v) {
                source.push(v);
                mapping[v] = k;
            });
            console.log(source);
            $("#pbxSearchBox").autocomplete({
                source: source,
                select: function(e, ui) {
                    BRANCHID = mapping[ui.item.value];
                    $('#pbxSearchBox').val(BRANCHID);
                }
            });
        }, error: function(res) {
            console.log(res);
        }
    }); 
}

function doSearch(url, target) {
    $.ajax({
        url: url,
        type: 'GET',
        success: function(res) {
            var source  = [ ];
            var mapping = { };
            $.each(res, function(k, v) {
                source.push(v);
                mapping[v] = k;
            });
            target.autocomplete({
                source: source,
                select: function(e, ui) {
                    RESELLERID = mapping[ui.item.value];
                    target.val(RESELLERID);
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
        url = "/partner/"+$(this).val();
        doSearch(url, $(this));
    });
    $('#customerSearchBox').keyup(function(e) {
        e.preventDefault();
        resellerId = $('#resellerSearchBox').val();
        url = '/customer/'+resellerId+'/'+$(this).val();
        doSearch(url, $(this));
    }).click(function(e) {
        e.preventDefault();
        $('#pbxSearchBox').val('');
    });
    $('#pbxSearchBox').keyup(function(e) {
        e.preventDefault();
        resellerId = $('#resellerSearchBox').val();
        url = '/pbx/'+resellerId+'/'+$(this).val();
        doSearch(url, $(this));
    }).click(function(e) {
        e.preventDefault();
        $('#customerSearchBox').val('');
    });
});