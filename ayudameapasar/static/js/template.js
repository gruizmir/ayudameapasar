function showList(from, target){
	
	if(!$(from).hasClass("open")){
		$(from).addClass('open');
	}else{
		$(from).removeClass('open');
	}

    $('#' + target).toggle('fast');
}

/* --- ON READY JS --- */
$(document).ready(function(){
	// Estilos para money-field
	$('.money-field').each(function(){
		/* TODO MONEY CHANGE */
	});

});
