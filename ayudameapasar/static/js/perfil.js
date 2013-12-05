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


function showEditForm(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: "",
        type: "GET",
        url: "/cuentas/get_edit/",
        success: function(data) {
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            response = data.response;
            if(response=="OK"){
                result = data.result;
                $("#user-data-div").html(result);
            }
            else{
                $("#user-data-div").html("<p>Error</p>");
            }
        },
        error: function(data){
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            $("#user-data-div")[0].innerHTML = "<p>Error</p>";
        },
    });
}





function submitUserForm(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: $("#user-data-form").serialize(),
        type: $("#user-data-form").attr('method'),
        url: $("#user-data-form").attr('action'),
        success: function(data) {
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            response = data.response;
            if(response=="OK"){
                result = data.result;
                $("#user-data-div")[0].innerHTML = result;
            }
            else{
                $("#user-data-div")[0].innerHTML = "<div class=\"alert alert-warning top-spaced\"><strong>Error en ingreso de datos.</strong> Verifica tu información nuevamente.</div>" + result;
            }
        },
    });
}


function evaluar(tipo, ident){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.get( "/evaluacion/getform/evaluacion_" + tipo + "/" + ident, function( data ) {
        $("#fader").hide();
        $("#spinner-div").hide();
        spinner.stop();
        response = data.response;
        if(response=="OK"){
            result = data.result;
            $("#evalDialog")[0].innerHTML = result;
        }
        else{
            $("#evalDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced\"><strong>No se pudo ejecutar la acción.</div>";
        }
        $("#evalDialog").dialog('open');
    });
}


function denunciar(tipo, ident){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.get( "/evaluacion/getform/abuso_" + tipo + "/" + ident, function( data ) {
        $("#fader").hide();
        $("#spinner-div").hide();
        spinner.stop();
        response = data.response;
        if(response=="OK"){
            result = data.result;
            $("#evalDialog")[0].innerHTML = result;
        }
        else{
            $("#evalDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced\"><strong>No se pudo ejecutar la acción.</div>";
        }
        $("#evalDialog").dialog('open');
    });
}



function sendEval(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: $("#evaluationForm").serialize(),
        type: $("#evaluationForm").attr('method'),
        url: $("#evaluationForm").attr('action'),
        success: function(data) {
            $("#evalDialog").dialog('close');
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            response = data.response;
             if(response=="OK"){
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-success top-spaced right-spaced left-spaced\"> <strong>Evaluación enviada correctamente.</strong></div>";
            }
            else{
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced right-spaced left-spaced\"><strong>No se pudo ejecutar la acción.</strong></div>";
                console.log(data.result);
            }
            $("#resultDialog").dialog('open');
        },
    });
}


function sendReport(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: $("#reportForm").serialize(),
        type: $("#reportForm").attr('method'),
        url: $("#reportForm").attr('action'),
        success: function(data) {
            $("#evalDialog").dialog('close');
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            response = data.response;
            if(response=="OK"){
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-success top-spaced right-spaced left-spaced\"><strong>Reporte enviado correctamente.</strong></div>";
            }
            else{
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced right-spaced left-spaced\"><strong>No se pudo ejecutar la acción.</strong></div>";
            }
            $("#resultDialog").dialog('open');
        },
    });
}


function aceptarSolicitud(ident){
    $('#confirmarSolicitudForm').attr('action', '/ayudantias/solicitud/' + ident + "/");
    $("#confirmarSolicitudDialog").dialog('open');
}


function confirmarSolicitudAyudantia(){
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    $.ajax({
        data: $("#confirmarSolicitudForm").serialize(),
        type: $("#confirmarSolicitudForm").attr('method'),
        url: $("#confirmarSolicitudForm").attr('action'),
        success: function(data) {
            $("#fader").hide();
            $("#spinner-div").hide();
            spinner.stop();
            $("#confirmarSolicitudDialog").dialog('close');
            response = data.response;
            if(response=="OK"){
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-success top-spaced right-spaced left-spaced\"><strong>Solicitud aceptada correctamente.</strong></div>";
            }
            else{
                $("#resultDialog")[0].innerHTML = "<div class=\"alert alert-warning top-spaced right-spaced left-spaced\"><strong>No se pudo ejecutar la acción.</strong></div>";
            }
            $("#resultDialog").dialog('open');
        },
    });
}
