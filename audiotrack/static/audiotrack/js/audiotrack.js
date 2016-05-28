$(document).ready(function(){
    var btn = $('#add_track_to_playlist');
    var src = $('#audiotrack_data');
    var chooser = $('#choose_playlist');
    $('#result').hide();
    btn.click(function(){
        $.ajax({
               type: "POST",
               url: btn.data('url'),
               data: {'track_id': src.data('audiotrack-id'), 'csrfmiddlewaretoken': btn.data('token'),
                    'playlist_id':chooser.val()},
               dataType: "json",
               success: function(response) {
                    $('#result').text("Audiotrack added to " + $('#choose_playlist option:selected').text());
                     $('#result').show();
                },
                error: function(rs, e) {
                       alert(rs.responseText);
                }
          });
       })

});