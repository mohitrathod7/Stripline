// --------------------------------------- Nav Modal boxes ----------------------------------------
$("nav .notification-bell").click(function(){
    if( $("nav .modal#menu").hasClass("show") == true){
        $("nav .modal#menu").toggleClass("show");
    }
    
    $("nav .modal#notifications").toggleClass("show");
});


// ----------------------------------- For Footer Accordion ---------------------------------------
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++){
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        
        // Toggle list items
        if (panel.style.display === "block"){
            panel.style.display = "none";
        }
        else{
            panel.style.display = "block";
        }

        // Toggle arrow icon
        if(!!~jQuery.inArray("active", this.classList)){
            $(".accordion.active .material-icons").replaceWith("<span class='material-icons md-light'>expand_less</span>");
        }
        else{
            $(".accordion .material-icons").replaceWith("<span class='material-icons md-light'>expand_more</span>");
        }
    });
}


// ---------------------------------------- Sticky NavBar -----------------------------------------
window.onscroll = function(){
    fixNav()
};

var navbar = document.getElementsByTagName("nav")[0];
var dummyNav = document.getElementsByClassName("dummyNav")[0];

    // Get the offset position of the navbar
var sticky = navbar.offsetTop;

    // Add the sticky class to the navbar when you reach its scroll position. 
    // Remove "sticky" when you leave the scroll position
function fixNav() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        dummyNav.classList.remove("hide");
    }
    else{
        navbar.classList.remove("sticky");
        dummyNav.classList.add("hide");
    }
}
