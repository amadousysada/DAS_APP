$(function(){
	$("#ajpeler_id").click(function(){
	var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#socontonie').html(sp2);
        $('#socontonie').load("/accueil/loadpage/sajnp");
    });
    $('#close').click(function(){
        var sp2P = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#socontonie').html(sp2P);
        $('#socontonie :last-child').remove();
        });
});