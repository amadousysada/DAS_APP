var form = {
    validated : false,
    fields : {},
    init : function(obj){
        form.that = obj; // storing form object
        // init fields with value and validation function
        $.each(form.that.serializeArray(), function(i, field) {
            form.fields[field.name] = { value : field.value, 'function' : 'valid_' + $('#id_' + field.name).attr('name')  + '_field'};
        });
        form.that.submit(form.submit);  // submit form handler
        form.blur(); // validation on blur handlers
    },
    blur: function() {
        form.that.find('dl :input').blur(form.valid_field); // checking validation
    },
    submit : function(e){
        e.preventDefault();
        form.valid(); // checking form

        if (form.validated){
            var values = {};
            for (var v in form.fields) {
                values[v] = form.fields[v].value;
            }
            $.post($('#engFor_id').attr('action'), values, form.success, 'json'); // making ajax post
        }
    },
    valid : function (){ // checking values from client side
        form.validated = true; // assuming form is correct
        form.that.find('dl :input').each(form.valid_field);
    },
    valid_field : function() {
        $(this).parent().next('dd').empty(); // empty error field
        var to_valid = $(this).attr('name'); // get field name
        form.fields[to_valid].value = $(this).val(); // updating values
        if (typeof(window['form'][form.fields[to_valid]['function']]) === 'function') {
            var validated = window['form'][form.fields[to_valid]['function']](to_valid);
            if (validated['error_message']) {
                form.validated = false;
                form.display_error(validated['field'], validated['error_message']);
            }
            else{
            $('#id_'+to_valid).removeClass('errr');
            }
        }
    },
    valid_date_en_field : function(field) {
        var error_message = '';
        if (form.fields[field].value === '') {
            error_message = 'Ce Champs est invalide.';
        }

        return {field: field, error_message : error_message};
    },
    valid_montant_field : function(field) {
        var error_message = '';
        if (form.fields[field].value === '') {
            error_message = 'Ce Champs est invalide.';
        }

        return {field: field, error_message : error_message};
    },

    valid_matricule_field : function (field){
        var error_message = '';
        if (form.fields[field].value === '') {
            error_message = '*';
        }
        if ($('#employe :last-child').text()=='Pas d\'employe a ce matricule'){error_message = '*';}

        return {field: field, error_message : error_message};
    },

    valid_type_field : function (field){
        var error_message = '';
        if (form.fields[field].value === '') {
            error_message = 'Ce Champs est invalide.';
        }
        return {field: field, error_message : error_message};
    },
    display_error : function(e, error){
            $('#id_'+e).addClass('errr');
    },
    success : function(data, textStatus, jqXHR){
        if (!data['success']){
            form.that.find('dl dd:last-child').empty();// empty old error messages
            var errors = data;
            for (var e in errors){ // iterating over errors
                var error = errors[e][0];
                form.display_error(e, error);
            }
        }
        else {
            var v=$('#id_matricule').val()
            var sp2 = 'AJOUT AVEC SUCCES';
            $('#ctnAlerte').html(sp2);
            $(".alert").show("slow");
            $(".modal .close").click()

            var sp = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
            $('#opt').html(sp);
            $('#opt').load('/accueil/retraite/search/'+v+"/b");


        }
    },
    error : function(jqXHR, textStatus, errorThrown){
        alert('error: ' + textStatus + errorThrown);
    }

};

$(function(){
    form.init($('#engFor_id')); // initialize form
    var value3;
    $('#id_matricule').blur(function(){
            value3=$('#id_matricule').val();
            if (value3.length<2){
                $('#employe :last-child').empty();
            }
            else{
            $('#employe').load("/accueil/retraite/search/"+value3+"/a");
            }
        });
    $('#close').click(function(){
        var sp2 = '<span class="col-sm-offset-3 col-sm-4"><h1>Loading ...</h1></span>';
        $('#retcontent').html(sp2);
        $('#retcontent').load("/accueil/loadpage/leng");
        });
});