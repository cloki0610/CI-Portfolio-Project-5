$( document ).ready(function() {
    $('#contact-1').show();
    $('#findByName').change(() => {
        let contact = $('#findByName').val();
        $('.contacts').fadeOut(1500);
        $('#findByName').fadeOut(1500, () => {
            $('#findByName').fadeIn(2500);
        });
        $('#' + contact).delay(1500).fadeIn(1500);
    })
});