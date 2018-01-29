var mois;
var annee;
$(function(){
$('#statsform').change(function () {
        if ($("#radio_1").is(":checked")) {
            $("#id_mois").attr('disabled', true);
            $("#id_annee").attr('disabled', true);
        }
        else if ($("#radio_2").is(":checked")) {
            $("#id_mois").attr('disabled', false);
            $("#id_annee").attr('disabled', false);
        }
        else{
            $("#id_mois").attr('disabled', true);
            $("#id_annee").attr('disabled', false);
        }

    });


    $('#aff_id').click(function(e){
        e.preventDefault();
        if ($("#radio_1").is(":checked")) {
                var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
                $('#statContenu').html(sp2);
                $('#statContenu').load("/accueil/stats/00/00/tous");
        }
        else if ($("#radio_2").is(":checked")) {
            mois=$("#id_mois").val();
            annee=$("#id_annee").val();
            var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
            $('#statContenu').html(sp2);
            $('#statContenu').load("/accueil/stats/"+mois+"/"+annee+"/mois");
        }
        else{
             annee=$("#id_annee").val();
             var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
             $('#statContenu').html(sp2);
             $('#statContenu').load("/accueil/stats/00/"+annee+"/annee");
        }

    });

});