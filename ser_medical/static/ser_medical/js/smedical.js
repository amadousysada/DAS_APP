$(function(){
	$("#pcm").click(function(){
        $('#smedContenu').load("/accueil/loadpage/smpcm");
    });
    $("#pc").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/smpc");
    });
    $("#lpc").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/smlpc");
    });
    $("#lc").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/lc");
    });
    $("#ajc").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/ajc");
    });
    $("#aor").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/aor");
    });
    $("#lor").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/lor");
    });
    $("#lpcm").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/loadpage/lpcm");
    });
    $("#stats").click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#smedContenu').html(sp2);
        $('#smedContenu').load("/accueil/stats/00/00/accu");
    });

});