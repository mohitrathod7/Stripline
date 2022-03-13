/* Display Nav */
function openNav(){
    $(".sideNav").css("width", "250px");
    $(".fa-bars").css("display", "none");
    $("nav .fa-times").css("display", "block");
    $("body").css("pointer-events", "none");
    $("nav .fa-times").css("pointer-events", "all");
    $(".sideNav").css("pointer-events", "all");
}

const sideNav = gsap.timeline({ defaults: {duration: 1} });

$('nav .fa-bars').click(function(){
    openNav();

    sideNav
        .from('.sideNav-item', { ease: 'power2.in', duration: 0.4, x: -300, stagger: 0.15 })
})


$('nav .fa-times').click(function(){        
    function hidepanel() {
        $(".sideNav").css("width", "0");
        $(".fa-bars").css("display", "block");
        $("nav .fa-times").css("display", "none");
        $("body").css("pointer-events", "all");
        $(".sideNav").css("pointer-events", "all");
    }

    sideNav
        .to('.sideNav-item', { ease: 'power2.in', duration: 0.4, x: -300, stagger: 0.15 })
        .to('.sideNav-item', { ease: 'power2.in', duration: 0.4, x: 0 })
    
    setTimeout(hidepanel, 1000);
})