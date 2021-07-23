(function(){"use strict";window.onload=function(){window.setTimeout(fadeout,500);}
function fadeout(){document.querySelector('.preloader').style.opacity='0';document.querySelector('.preloader').style.display='none';}
window.onscroll=function(){var header_navbar=document.getElementById("header_navbar");var sticky=header_navbar.offsetTop;var logo=document.querySelector('.navbar-brand img')
if(window.pageYOffset>sticky){header_navbar.classList.add("sticky");logo.src='assets/images/logo/logo-2.svg';}else{header_navbar.classList.remove("sticky");logo.src='assets/images/logo/logo.svg';}
var backToTo=document.querySelector(".back-to-top");if(document.body.scrollTop>50||document.documentElement.scrollTop>50){backToTo.style.display="block";}else{backToTo.style.display="none";}};let navbarToggler=document.querySelector(".navbar-toggler");navbarToggler.addEventListener('click',function(){navbarToggler.classList.toggle("active");})
var wow=new WOW({mobile:false});wow.init();})();