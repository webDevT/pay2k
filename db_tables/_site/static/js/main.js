$(function(){
  // ------ start mobil menu---
$('.btn_menu').click(function(){
		$('.menu ul').toggleClass('active');
		$('.btn_menu').toggleClass('active');
    $('.top-header').toggleClass('active');
    $('.download-header').toggleClass('active');

    
	})


  // ------end mobil menu---

  $('.slider').slick({
prevArrow: $('.prev'),
nextArrow: $('.next'),
slidesToShow: 3,
centerMode: true,
centerPadding: '40px',

responsive: [
   {
    breakpoint: 690,
    settings: {
      slidesToShow: 2,
      centerPadding: '125px'
    }
  },
 {
    breakpoint: 626,
    settings: {
      slidesToShow: 2,
      centerPadding: '100px'
    }
  },
  {
    breakpoint: 570,
    settings: {
      slidesToShow: 2,
      centerPadding: '70px'
    }
  },
  {
    breakpoint: 520,
    settings: {
    slidesToShow: 2
    }
  },
  {
    breakpoint: 480,
    settings: {
    	slidesToShow: 1,
    	centerPadding: '125px'

    }
  },
   {
    breakpoint: 450,
    settings: {
      slidesToShow: 1,
      centerPadding: '220px'

    }
  },
   {
    breakpoint: 430,
    settings: {
      slidesToShow: 1,
      centerPadding: '200px'

    }
  },
  {
    breakpoint: 400,
    settings: {
      slidesToShow: 1,
      centerPadding: '150px'

    }
  },
   {
    breakpoint: 350,
    settings: {
      slidesToShow: 1,
      centerPadding: '105px'

    }
  },


  ]

});
$('.slider').slick("setPosition");




});







$(function(){
	$('.question-item').click(function(){
		$(this).toggleClass('active');
		$(this).find('p').slideToggle();
		$(this).find('.btn-close').toggleClass('active');
		


	});
});

var ignored_first_lang_select = false;
$('#leng-select').ddslick({
onSelected: function(data){

if (!ignored_first_lang_select) {
ignored_first_lang_select = true;
return;
}
document.getElementById('language').value = data.selectedData.value;
document.getElementById('redirect').value = '/' + data.selectedData.value + location.pathname.substr(3);
document.getElementById('lang-form').submit();
}
});

 if($(window).width() < 700) {
$(function(){

var target = $('#scroll-position');
var targetPos = target.offset().top;
var winHeight = $(window).height();
var scrollToElem = targetPos - winHeight;
$(window).scroll(function(){
  var winScrollTop = $(this).scrollTop();
  if(winScrollTop > scrollToElem){
     $('.download__button-wrapper-fixed').hide();
  }
  else {
    $('.download__button-wrapper-fixed').show();
  }
});

});
}
if($(window).width() < 768) {
checkFontSize();


function checkFontSize() {
  var elems = document.querySelectorAll(".gameName");
  
  [].forEach.call(elems, function(el) {
    scaleFontSize(el);
  });  

}

function scaleFontSize(element) {
    element.style.fontSize = "230%";
    if (element.scrollWidth > element.clientWidth) {
        element.style.letterSpacing = "-0.05em";
    }
    if (element.scrollWidth > element.clientWidth) {
        element.style.letterSpacing = "0";
        element.style.fontSize = "130%";
    }
 
}

checkFontSize2();


function checkFontSize2() {
  var elems = document.querySelectorAll(".devName");
  
  [].forEach.call(elems, function(el) {
    scaleFontSize2(el);
  });  

}

function scaleFontSize2(element) {
    element.style.fontSize = "140%";
    if (element.scrollWidth > element.clientWidth) {
        element.style.letterSpacing = "-0.05em";
    }
    if (element.scrollWidth > element.clientWidth) {
        element.style.letterSpacing = "0";
        element.style.fontSize = "80%";
    }
 
}
}