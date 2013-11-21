function showEditForm(){
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
    var target = document.getElementById('spinner-div');
    var spinner = new Spinner(opts).spin(target);
    $("#fader").show();
    $("#spinner-div").show();
    event.preventDefault();
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
