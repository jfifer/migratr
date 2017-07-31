$(document).ready(function() {
    d = new Date();
    d.setMonth(d.getMonth() - 1);
    d.setHours(0, 0, 0);
    d.setMilliseconds(0);
    myDate = d/1000;
    $.ajax({
        url: "/migrations/"+myDate,
        type: 'GET',
        success: function(res) {
            el = $('#result-body');
            $.each(res, function(k,v) {
              a = "<a href='#' id='"+v.id+"' class='migrationId'>"+v.id+"</a>";
              newEl = "<tr><td>"+a+"</td><td>"+v.src_server+"</td><td>"+v.dst_server+"</td><td>"+v.context+"</td><td>"+v.customer+"</td><td>"+v.reseller+"</td><td>"+v.run_at+"</td><td>"+v.state+"</td></tr>";
              el.append(newEl); 
            });
        }, error: function(res) {
            console.log("error", res);
        }
    });
});
