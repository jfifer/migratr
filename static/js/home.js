function getDate() {
    d = new Date();
    d.setMonth(d.getMonth() - 1);
    d.setHours(0, 0, 0);
    d.setMilliseconds(0);
    return d/1000;
}

function getMigrations(date, sortby, sorthow) {
    $('#result-body').html('');
    $.ajax({
        url: "/migrations/"+myDate+"/"+sortby+"/"+sorthow,
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
}

function doMigrationSort(myDate, el) {
      sortby = el.attr('id');
      if(el.hasClass('active')) {
        sortby = el.attr('id');
        if(el.hasClass('asc')) {
          el.removeClass('asc').addClass('desc');
          sorthow = 'desc';
        } else {
          el.removeClass('desc').addClass('asc');
          sorthow = 'asc';
        }
      } else {
        sortby = el.attr('id');
        sorthow = 'asc';
        $('.active').removeClass('active');
        el.addClass('active asc');
      }
      getMigrations(myDate, sortby, sorthow);
}

$(document).ready(function() {
    myDate = getDate();
    
    getMigrations(myDate, 'id', 'ASC');

    $('.sort-header').on('click', function(e) {
      e.preventDefault();
      doMigrationSort(myDate, $(this));
    });
});
