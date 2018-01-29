$(function(){
    $('#close').click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#socontonie').html(sp2);
        $('#socontonie :last-child').remove();
        });
});