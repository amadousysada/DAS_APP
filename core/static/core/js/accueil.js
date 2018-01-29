$(function(){
/* ----------------------------------------------------------------------- */
    $("#sm").click(function(){
        $('#contenu').load("/accueil/service/sm");
    });
    $("#sr").click(function(){
        $('#contenu').load("/accueil/service/sr");
    });
    $("#logoutBtn").click(function(){
        window.location.href='/logout/';
    });
$('#bd').hide();


$('#btnER').click(function(){
//alert('tttt');
    if($(this).hasClass('va')){
        $(this).removeClass('va')
        $(this).addClass('na');

        $('#bd').hide();
    }
    else {
        $(this).removeClass('na');
        $(this).addClass('va');
        $('#bd').show();
    }
//    return false;
});

});