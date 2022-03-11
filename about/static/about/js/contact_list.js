$( document ).ready(function() {
    $('#contact-1').show();
    $('#findByName').change(() => {
        let contact = $('#findByName').val();
        $('.contacts').hide();
        $('#' + contact).show();
    })
});