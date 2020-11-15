var $target = $('#target')
var $preview = $('#preview')

var imgHeight = 300
var thumbnailWidth = 200
var thumbnailHeight = 100

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {

            resetCanvas(e);

            var jcrop_api = $target.Jcrop({

                onChange: handleJCrop,
                onSelect: handleJCrop,
                onRelease: hidePreview,
                aspectRatio: thumbnailWidth / thumbnailHeight,
                boxHeight: imgHeight
            });
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

function resetCanvas(e) {

    // Show crop text
    $('.crop-text').css("display", "block").show()

    // Reset image container
    $('#image-container').empty();

    var img = $('<img id="target">');
    img.attr('src', e.target.result);
    img.appendTo('#image-container');
    $target = $('#target')

    // Reset image container
    $('#preview-container').empty();

    var img = $('<img id="preview">');
    img.attr('src', e.target.result);
    img.appendTo('#preview-container');
    $preview = $('#preview')

    // Change target image dimensions
    $target.css({
        width: 'auto',
        height: imgHeight + 'px'
    }).show()

    // Change preview container dimensions
    $('#preview-container').css({
        width: thumbnailWidth + 'px',
        height: thumbnailHeight + 'px'
    }).show()
    
}

$("#file").change(function(){
    readURL(this);
});

function handleJCrop(c)
{
    showPreview(c)
    showCoords(c)
}


function showPreview(coords)
{
    if (parseInt(coords.w) > 0)
    {
        var rx = thumbnailWidth / coords.w;
        var ry = thumbnailHeight / coords.h;

        $preview.css({
            width: Math.round(rx * $target.width()) + 'px',
            height: Math.round(ry * imgHeight) + 'px',
            marginLeft: '-' + Math.round(rx * coords.x) + 'px',
            marginTop: '-' + Math.round(ry * coords.y) + 'px'
        }).show();
    }
}

function hidePreview()
{
    $preview.stop().fadeOut('fast');
}

function showCoords(c)
{
    $('#x').val(c.x);
    $('#y').val(c.y);
    $('#x2').val(c.x2);
    $('#y2').val(c.y2);
    $('#w').val(c.w);
    $('#h').val(c.h);
}