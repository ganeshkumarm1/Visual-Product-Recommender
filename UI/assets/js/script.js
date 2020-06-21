/*
* @Author: GaNeShKuMaRm
* @Date:   2017-02-07 17:57:44
* @Last Modified by:   GaNeShKuMaRm
* @Last Modified time: 2017-02-13 21:53:33
*/

'use strict';

$(document).ready(function() {
    var baseURL = 'http://127.0.0.1:5000/'
    $('#image-file').change(function() {
        var output = document.getElementById('preview');
        output.src = URL.createObjectURL(event.target.files[0]);
        $('#preview').cropper({
            crop: function(e) {
                $('input[name=x]').val(e.x);
                $('input[name=y]').val(e.y);
                $('input[name=w]').val(e.width);
                $('input[name=h]').val(e.height);
            }
        }); //cropper
    }); //#image-file

    $('#image-upload-form').on('submit', function() {
            var formData = new FormData($(this)[0]);
             $.ajax({
                url: baseURL + 'search',
                type: 'POST',
                data: formData,
                async: false,
                success: function(data) {
                    window.location.reload();
                    var win = window.open(data, '_blank');
                    if (win) {
                        win.focus();
                    }
                    else {
                        alert('Please allow popups for this website');
                    }
                },
                error: function(data) {
                    alert(data);
                },
                cache: false,
                contentType: false,
                processData: false
    });
    return false;
    }); //#submit
}); //document.ready
