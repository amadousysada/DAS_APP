var form = {
    validated : false,
    fields : {},
    init : function(obj){
        form.that = obj; // storing form object
        // init fields with value and validation function
        $.each(form.that.serializeArray(), function(i, field) {
            form.fields[field.name] = { value : field.value, 'function' : 'valid_' + $('#id_' + field.name).attr('type')  + '_field'};
        });
        form.that.submit(form.submit);  // submit form handler
        form.blur(); // validation on blur handlers
    },
    blur: function() {
        form.that.find('dd :input').blur(form.valid_field); // checking validation
    },
    submit : function(e){
        e.preventDefault();
        form.valid(); // checking form

        if (form.validated){
            var values = {};
            for (var v in form.fields) {
                values[v] = form.fields[v].value;
            }
            $('#loadL').show();
            $.post(home_url, values, form.success, 'json');/*.error(form.error); */// making ajax post
//            $('#loadL').hide();
        }
    },
    valid : function (){ // checking values from client side
        form.validated = true; // assuming form is correct
        form.that.find('dd :input').each(form.valid_field);
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
        }
    },

    valid_text_field : function(field) {
        var error_message = '';
        if (form.fields[field].value === '') {
            error_message = 'Champ obligatoire.';
        }

        return {field: field, error_message : error_message};
    },
    valid_password_field : function(field) {
        var error_message = '';
        var value = form.fields[field].value;
        if (value === '') {
            error_message = 'Champ obligatoire.';
        }
        else if (value.length < 8) {
            error_message = "8 caractere au minimum.";
        }

        return {field: field, error_message : error_message};
    },
    display_error : function(e, error){
        var $dd = $('#id_' + e).parent().next('dd'); // get dd error field
        var $error_list = $('<ul/>', {'class' : 'errorlist'}); // create error list
        var $error_em = $('<li/>', {html : error}); // create error element
        $error_em.appendTo($error_list); // append error element to error list
        $dd.append($error_list); // append error list to dd error field
    },
    success : function(data, textStatus, jqXHR){
        if (!data['success'] && !data['error']){
            form.that.find('dl dd:last-child').empty();// empty old error messages
            var errors = data;
            for (var e in errors){ // iterating over errors
                var error = errors[e][0];
                form.display_error(e, error);
            }
        }
        if(data['error']){
            var $dd = $('#id_password').parent().next('dd'); // get dd error field
            var $error_list = $('<ul/>', {'class' : 'errorlist'}); // create error list
            var $error_em = $('<li/>', {html : 'Login ou password invalide'}); // create error element
            $error_em.appendTo($error_list); // append error element to error list
            $dd.append($error_list); // append error list to dd error field
            $('#loadL').hide();
        }

        if (data['success']) {

            window.location.href = data['success'];
            $('#loadL').hide();// redirection to success page
        }
    },
    error : function(jqXHR, textStatus, errorThrown){
        alert('error: ' + textStatus + errorThrown);
    }
};

$(function(){
    form.init($('#login')); // initialize form
            $('#loadL').hide();

});