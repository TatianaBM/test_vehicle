function filePreview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.div_image').empty();
            $('.div_image + img').remove();
            $('.div_image').after('<img src="'+e.target.result+'" width="200" height="200"/>');
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$(".file_image").change(function () {
    filePreview(this);
});