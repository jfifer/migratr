var RESELLERID, CUSTOMERID, BRANCHID, SERVERID, SRCSERVERID;

function getContextByCustomer(customerId) {
    $("#pbxSearchBox").val(null);
    $.ajax({
        url: '/pbx/'+customerId,
        type: 'GET',
        success: function(res) {
            console.log(res);
            BRANCHID = res[0];
            getSourceServer(BRANCHID)
            $('#pbxSearchBox').val(res[1]);
            $('#branchId').val(BRANCHID);
            //findServersByBranch(BRANCHID);
        }, error: function(res) {
            console.log(res);
        }
    }); 
}

function getCustomerByContext(branchId) {
    $("#customerSearchBox").val(null);
    $.ajax({
        url: '/customer/'+branchId,
        type: 'GET',
        success: function(res) {
            console.log(res);
            CUSTOMERID = res.customerId;
            $('#customerSearchBox').val(res[1]);
            //findServersByBranch(BRANCHID);
        }, error: function(res) {
            console.log(res);
        }
    });
}

function getServerGroups(id) {
  $.ajax({
    url: '/server/reseller/'+id,
    type: 'GET',
    success: function(res) {
      $('#serverGroupSearch option').remove();
      $.each(res, function(k,v) {
        el = "<option value='"+k+"'>"+v+"</option>";
        $('#serverGroupSearch').append(el).prop('disabled', false);
      });
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
                    fsStatus = false;
                    switch(type) {
                        case 'reseller':
                            getServerGroups(id);
                            RESELLERID = id;
                            $('#resellerId').val(id);
                            break;
                        case 'customer':
                            CUSTOMERID = id;
                            getContextByCustomer(id);
                            $('#customerId').val(id);
                            //BRANCHID = null;
                            break;
                        case 'pbx':
                            BRANCHID = id;
                            //getCustomerByContext(id);
                            CUSTOMERID = null;
                            break;
                        case 'server':
                            SERVERID = id;
                            $('#dst_server_id').val(id);
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

function getServersByGroup(serverGroupId) {
    $.ajax({
        url: '/server/group/'+serverGroupId,
        type: "GET",
        success: function(res) {
          $.each(res, function(k, v) {
            console.log(v);
          });
        }
    });
}

function getSourceServer(branchId) {
    $.ajax({
        url: '/server/src/'+branchId,
        type: 'GET',
        success: function(res) {
          srcServer = res[1];
          SRCSERVERID = res[0];
          $('#sourceServer').html(srcServer);
          $('#src_server_id').val(SRCSERVERID);
        }
    });
}

function createMigration(resellerId, branchId, customerId, serverId, srcServerId) {
    $.ajax({
        url: '/migration/new/'+parseInt(resellerId)+'/'+parseInt(branchId)+'/'+parseInt(customerId)+'/'+parseInt(serverId)+'/'+parseInt(srcServerId),
        type: 'POST',
        success: function(res) {
 
        }
    });
}

$(document).ready(function() {
    $('#fsSearchBox').keyup(function(e) {
        if($(this).val() !== '') {
            e.preventDefault();
            fsClosed = "1";
            if($('#fsServerStatus')[0].checked) { fsClosed = "2"; }
            if($('#serverGroupSearch').val() === '') {
              url = "/server/"+$(this).val()+"/"+fsClosed;
            } else {
              url = "/server/group/"+$('#serverGroupSearch').val()+"/"+$(this).val()+"/"+fsClosed;
            }
            doSearch(url, $(this), 'server');
        }
    });
    $('#resellerSearchBox').keyup(function(e) {
        if($(this).val() !== '') {
            e.preventDefault();
            url = "/partner/"+$(this).val();
            doSearch(url, $(this), 'reseller');
        }
    });
    $('#serverGroupSearch').change(function(e) {
        doSearch('/server/group/'+$(this).val(), $('#fsSearchBox'), 'server');
    });
    $('#customerSearchBox').keyup(function(e) {
        if($(this).val() !== '') {
            e.preventDefault();
            resellerId = $('#resellerSearchBox').val();
            url = '/customer/'+RESELLERID+'/'+$(this).val();
            doSearch(url, $(this), 'customer');
        }
    }).click(function(e) {
        e.preventDefault();
        $('#pbxSearchBox').val('');
    });
    $('#pbxSearchBox').keyup(function(e) {
        if($(this).val() !== '') {
            e.preventDefault();
            resellerId = $('#resellerSearchBox').val();
            url = '/pbx/'+RESELLERID+'/'+$(this).val();
            doSearch(url, $(this), 'pbx');
        }
    }).click(function(e) {
        e.preventDefault();
        $('#customerSearchBox').val('');
    });
    /* $('#new_migration').click(function(e) {
        e.preventDefault();
        //console.log(RESELLERID, CUSTOMERID, BRANCHID, SERVERID);
        //createMigration(RESELLERID, BRANCHID, CUSTOMERID, SERVERID, SRCSERVERID);
    }); */
});
