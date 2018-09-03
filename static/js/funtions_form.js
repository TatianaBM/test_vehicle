function confirm_submit_form(form, content, title){

    $.confirm({
        title: title,
        content: content,
        buttons: {
            confirm: function () {
                $(form).submit()
            },
            cancel: function () {
                $.alert('Canceled!');
            }
        }
    });
}