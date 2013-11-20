function showList(from, target){
	
	if(!$(from).hasClass("open")){
		$(from).addClass('open');
	}else{
		$(from).removeClass('open');
	}

    $('#' + target).toggle('fast');
}
