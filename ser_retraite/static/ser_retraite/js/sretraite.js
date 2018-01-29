$(function(){





$('#engIdretraite').click(function(){
    var sp = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
    $('#opt').html(sp);
    $('#opt').load('/accueil/retraite/search/'+$('.matricule_ids').attr('id')+"/b");

});
$("#stats").click(function(){
    $('#'+$(this).attr('page')).load("/accueil/loadpage/stats");
    });

$('#dretraite').click(function(){

$('#opt').load("/accueil/service/feng");
//        alert('oppps|');
});
$('#eng').click(function(){
    var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
    $('#retcontent').html(sp2);
    $('#retcontent').load("/accueil/loadpage/leng");
//       alert('oppps|');
});


//$('#47p').click(function(){
//        $('.modal-body').load("/accueil/service/feng");
////alert('opps');
//    });
    var valeur;
    $('.form').submit(function(){
        valeur=$('#cherche_id').val();
        $('.errr').removeClass('errr');
        if(valeur == ""){
            $('#cherche_id').addClass('errr');
        }
        else{
            var sp = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
            $('#retcontent').html(sp);
            $('#retcontent').load('/accueil/retraite/search/'+valeur+"/a");

        }
return false;
    });
});
