
$(document).ready(function(){
    	$("#h4pb").click(function(){
           //$("#main").css("visibility","visible");
            $('.main-section').toggleClass("open-more");
            });

    });
$(document).ready(function(){
    	$("#botpic").click(function(){
           //$("#main").css("visibility","visible");
            $('.main-section').toggleClass("open-more");
            });

    });
//when the page is loading chat window is hidden
$(document).ready(function(){
    	$(".fa-minus").click(function(){
            $('.main-section').toggleClass("open-more");
        });
    });
//clicking on - toggle the chat window

$(document).ready(function(){
    	$(".fa-times").click(function(){
           $("#main").css("visibility","hidden");
        });
    });
//close the chat window

$(document).ready(function(){
    	$("#headBar").click(function(){
            $('.main-section').toggleClass("open-more");
        });
    });

