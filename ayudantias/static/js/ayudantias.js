var opts = {
  lines: 13, // The number of lines to draw
  length: 12, // The length of each line
  width: 8, // The line thickness
  radius: 20, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#000', // #rgb or #rrggbb or array of colors
  speed: 1, // Rounds per second
  trail: 60, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: 'auto', // Top position relative to parent in px
  left: 'auto' // Left position relative to parent in px
};

function pedirHora(ident){
    $('#solicitarHoraForm').attr('action', '/ayudantias/hora/' + ident + "/");
    $("#solicitarHoraDialog").dialog('open');    
}


function confirmarSolicitud(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: $("#solicitarHoraForm").serialize(),
        type: $("#solicitarHoraForm").attr('method'),
        url: $("#solicitarHoraForm").attr('action'),
        success: function(data) {
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            $("#solicitarHoraDialog").dialog('close');
            response = data.response;
            if(response=="OK"){
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-success top-spaced right-spaced left-spaced\"><strong>Solicitud enviada correctamente.</strong></div>";
            }
            else{
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced right-spaced left-spaced\"><strong>No se pudo ejecutar la acción.</strong></div>";
                console.log(data.result);
            }
            $("#resultDialog").dialog('open');
        },
    });
}
