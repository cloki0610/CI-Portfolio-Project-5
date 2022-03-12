function handleEnableDisable(itemId) {
    let currentValue = parseInt($(`.qty_${itemId}`).val());

    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 98;

    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.qty_input');
for (let i = 0; i < allQtyInputs.length; i++) {
    let itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function () {
    let itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function (e) {
    e.preventDefault();
    let itemId = $(this).data('item_id');
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    let currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue + 1);
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function (e) {
    e.preventDefault();
    let itemId = $(this).data('item_id');
    let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    let allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
    let currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue - 1);
    handleEnableDisable(itemId);
});