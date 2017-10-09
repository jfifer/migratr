function doPortalCnxTest() {
    $.ajax({
        url: "/migration/preflight/"+portal,
        method: "GET",
        success: function(res) {
           console.log(res);
        }
    });
}

function lookupMigration(id) {
    $.ajax({
        url: '/migration/preflight/'+id,
        method: 'GET',
        success: function(res) {
           $('#resellerName').html(res[0]);
           $('#customerName').html(res[1]);
           $('#contextName').html(res[2]);
           $('#src_server').html(res[3]);
           $('#dst_server').html(res[4]);

           doPortalCnxTest();
        } 
    });
}

$(document).ready(function() {
    migrationId = $('#migrationId').val();
    lookupMigration(migrationId);
});
