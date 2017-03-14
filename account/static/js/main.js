/**
 * Created by Anit on 8/22/2016.
 */
    if (window.addEventListener) window.addEventListener('DOMMouseScroll', wheel, false);
window.onmousewheel = document.onmousewheel = wheel;

function wheel(event) {
    var delta = 0;
    if (event.wheelDelta) delta = event.wheelDelta / 120;
    else if (event.detail) delta = -event.detail / 3;

    handle(delta);
    if (event.preventDefault) event.preventDefault();
    event.returnValue = false;
}

function handle(delta) {
    var time = 2000;
	var distance = window.innerHeight;

    $('html, body').stop().animate({
        scrollTop: $(window).scrollTop() - (distance * delta)
    }, time, "easeOutBack");
}

$(document).ready(function(){
   $("#chevron").click(function(){
       $('html, body').stop().animate({
        scrollTop: 1000
    }, 3000, "easeOutBack");
   });
});

$(document).ready(function(){
   $("#ser").click(function(){
       $('html, body').stop().animate({
        scrollTop: 1000
    }, 3000, "easeOutBack");
   });

    if (window.outerWidth > 768) {
        $(".signupl").click(function () {
            var a = window.outerWidth - 140;
            $(".signupl").css({
                "width": a,
            });
            $(".signinl").css({
                "width": 70,
            });
            $(".signupl > p").text("");
            $(".whyusl > p").text(">");
            $(".signinl > p").text("<");
        });
        $(".whyusl > p").text("");

        $(".signinl").click(function () {
            var a = window.outerWidth - 180;
            $(".signupl").css({
                "width": a + 40,
            });
            $(".signinl").css({
                "width": a,
            });
            $(".signupl > p").text(">");
            $(".whyusl > p").text(">");
            $(".signinl > p").text("");
        });

        $(".whyusl").click(function () {
            $(".signupl").css({
                "width": 70,
            });
            $(".signinl").css({
                "width": 70,
            });
            $(".signupl > p").text("<");
            $(".whyusl > p").text("");
            $(".signinl > p").text("<");
        })
    }
});

$(document).ready(function(){
    $("#register").click(function(){
        $.ajax({
            url: "/accounts/register/",
            type:"POST",
            async: true,
            data:  $("#registerform").serialize(),

            success: function(result){
                $(".signup").html(result);
             }});
    });

    $("#members").click(function(){
        $(".post").slideUp();
        $(".events").slideUp();
        $(".photos").slideUp();
        $(".videos").slideUp();
        $(".members").slideDown();
    });

    $("#post").click(function(){
        $(".members").slideUp();
        $(".events").slideUp();
        $(".photos").slideUp();
        $(".videos").slideUp();
        $(".post").slideDown();
    });

    $("#events").click(function(){
        $(".post").slideUp();
        $(".members").slideUp();
        $(".photos").slideUp();
        $(".videos").slideUp();
        $(".events").slideDown();
    });

    $("#photos").click(function(){
        $(".post").slideUp();
        $(".events").slideUp();
        $(".members").slideUp();
        $(".videos").slideUp();
        $(".photos").slideDown();
    });

    $("#videos").click(function(){
        $(".post").slideUp();
        $(".events").slideUp();
        $(".photos").slideUp();
        $(".members").slideUp();
        $(".videos").slideDown();
    })

    $("#writepostb").click(function(){
        $.ajax({
            url: "/dreamsgroup/writepost/",
            type:"GET",
            async: true,
            data:  $("#writepost").serialize(),

            success: function ola(result){
                if (result=="Empty")
                {
                    $(".empty").text(result).slideDown()
                    setTimeout(reload, 3000);
                }
                else location.reload(true);
             }});
    });

    $("#post-list12").click(function(){
       $("#post-list2").toggle(500);
         $("#post-list1").hide(250);
         $("#post-list3").hide(250);
    });
    $("#post-list11").click(function(){
       $("#post-list1").show(500);
         $("#post-list2").hide(250);
         $("#post-list3").hide(250);
    });
     $("#post-list13").click(function(){
       $("#post-list3").show(500);
         $("#post-list1").hide(250);
         $("#post-list2").hide(250);
    });

     $("#post-image").submit(function(){
        $.ajax({
            url: this.url,
            type:"POST",
            async: true,
            data:  $("#post-image").serialize(),

            success: function(result){
                setTimeout(reload, 3000);
             }});
    });
});

function reload()
{
    location.reload(true);
}






