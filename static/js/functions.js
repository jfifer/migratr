var RESELLERID, CUSTOMERID, BRANCHID, SERVERID;

function getContextByCustomer(customerId) {
    $("#pbxSearchBox").val(null);
    $.ajax({
        url: '/pbx/'+customerId,
        type: 'GET',
        success: function(res) {
            BRANCHID = res.branchId;
            findServersByBranch(BRANCHID);
        }, error: function(res) {
            console.log(res);
        }
    }); 
}

function doSearch(url, target, type) {
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
                    id = mapping[ui.item.value];
                    switch(type) {
                        case 'reseller':
                            RESELLERID = id;
                            break;
                        case 'customer':
                            CUSTOMERID = id;
                            BRANCHID = null;
                            break;
                        case 'pbx':
                            BRANCHID = id;
                            CUSTOMERID = null;
                            break;
                        case 'server':
                            SERVERID = id;
                            break;
                        default:
                            break;
                    }
                    target.val(id);
                }
            });
        }, error: function(res) {
            console.log(res);
        }
    });
}

$(document).ready(function() {
    $('#fsSearchBox').keyup(function(e) {
        e.preventDefault();
        url = "/server/"+$(this).val();
        doSearch(url, $(this), 'server');
    });
    $('#resellerSearchBox').keyup(function(e) {
        e.preventDefault();
        url = "/partner/"+$(this).val();
        doSearch(url, $(this), 'reseller');
    });
    $('#customerSearchBox').keyup(function(e) {
        e.preventDefault();
        resellerId = $('#resellerSearchBox').val();
        url = '/customer/'+RESELLERID+'/'+$(this).val();
        doSearch(url, $(this), 'customer');
    }).click(function(e) {
        e.preventDefault();
        $('#pbxSearchBox').val('');
    });
    $('#pbxSearchBox').keyup(function(e) {
        e.preventDefault();
        resellerId = $('#resellerSearchBox').val();
        url = '/pbx/'+RESELLERID+'/'+$(this).val();
        doSearch(url, $(this), 'pbx');
    }).click(function(e) {
        e.preventDefault();
        $('#customerSearchBox').val('');
    });
});