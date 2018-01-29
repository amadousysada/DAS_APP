function afficherPopupConfirmationLien(question, val) {
    // crée la division qui sera convertie en popup
    $('body').append('<div id="popupconfirmation" title="Confirmation"></div>');
    $("#popupconfirmation").html(question);

    // transforme la division en popup
    var popup = $("#popupconfirmation").dialog({
        autoOpen: true,
        width: 400,
        dialogClass: 'dialogstyleperso',
        hide: "fade",
        buttons: [
            {
                text: "Oui",
                class: "ui-state-question",
                click: function () {
                    $(this).dialog("close");
//                    var hrefdefini = false;
//
//                    if (lien != null) {
//                        if ($(lien).attr("href") != undefined) {
//                            hrefdefini = true;
//                            // affiche la page de l'attribut href
//                            window.location.href = $(lien).attr("href");
//                        }
//                    }
//
//                    if (!hrefdefini) {
//                        // réaffiche la page actuelle
//                        window.location.reload();
//                    }
var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
$('#smedContenu').load("/accueil/medicale/delete/pc/"+val);

                    $("#popupconfirmation").remove();

                }
            },
            {
                text: "Non",
                class: "ui-state-question",
                click: function () {
                    $(this).dialog("close");
                    $("#popupconfirmation").remove();
                }
            }
        ]
    });

    $("#popupconfirmation").prev().addClass('ui-state-question');

    return popup;
}
function generer_pdf(id,type){
    if(type =='fc'){
    alert('fiche circulaire n'+id);
    }

}
function set_display(first, last) {
  $('tbody').children().hide();
  $('tbody').children().slice(first, last).show();
}

function previous(){
    if($('.active').prev('.page_link').length) go_to_page(current_page - 1);
}

function next(){
    if($('.active').next('.page_link').length) go_to_page(current_page + 1);
}

function go_to_page(page_num){
  current_page = page_num;
  start_from = current_page * show_per_page;
  end_on = start_from + show_per_page;
  set_display(start_from, end_on);
  $('.active').removeClass('active');
  $('#id' + page_num).addClass('active');
}
$(function(){
//$('#lprise').DataTable();
  var number_of_pages = Math.ceil($('tbody').children().length / show_per_page);
  var nav = '<ul class="pagination"><li><a href="javascript:previous();">&laquo;</a>';
  var i = -1;
  while(number_of_pages > ++i){

    nav += '<li class="page_link'
    if(!i) nav += ' active';
    nav += '" id="id' + i +'">';
    nav += '<a href="javascript:go_to_page(' + i +')">'+ (i + 1) +'</a>';
  }
  nav += '<li><a href="javascript:next();">&raquo;</a></ul>';
  $('#page_navigation4').html(nav);
  set_display(0, show_per_page);
  $(".boutonsupprimer").click(function(event) {

  event.preventDefault();
        var val=$(".boutonsupprimer").attr('id');
//        alert(val);
//var retVal = confirm("Do you want to continue ?");
//               if( retVal == true ){
//                  document.write ("User wants to continue!");
//                  return true;
//               }
//               else{
//                  document.write ("User does not want to continue!");
//                  return false;
//               }
afficherPopupConfirmationLien('Désirez-vous vraiment supprimer cet archive ?', val);

    });
});
