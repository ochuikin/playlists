$(document).ready(function(){
//todo    get by class, no tag
    var btn = $('#like');
    btn.click(function(){
        $.ajax({
               type: "POST",
               url: btn.data('url'),
               data: {'slug': $(this).attr('name'), 'csrfmiddlewaretoken': btn.data('token')},
               dataType: "json",
               success: function(response) {
                      $('#showl').text(response.likes_count)
                },
                error: function(rs, e) {
                       alert(rs.responseText);
                }
          });
       })

});