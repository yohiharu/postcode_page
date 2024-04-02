$(function(){
	$('.top-btn').hide();
	$(window).scroll(function(){
		if($(this).scrollTop() > 150 ){
			$('.top-btn').fadeIn();
		}else{
			$('.top-btn').fadeOut();
		}
	});
});
