window.onload = function () {
    const message = document.querySelector(".system-message");
    if (message) {
        setTimeout(() => message.remove(), 3000);
    }
};


$('.delete-btn').on('click', function () {
    const trackId = parseInt($(this).attr('id').replace("track-", ""));
    $.ajax({
        url: deleteUploadUrl,
        headers: {
            "X-CSRFToken": csrfMiddlewareToken,
        },
        type: "POST",
        data: {
            "track_id": trackId,
        },
        dataType: 'json',
        success: function (response) {
            console.log(trackId + 'deleted.');
            $(`#track-${trackId}-div`).remove();
        },
        error: function (response) {
            console.log('ERRPR');
            console.log(response.responseText);
        }
    })
})

$(function () {
    $('div', '.songs').each(function (index, element) {
        const taskId = $(element).data('task-id');
        const url = $(element).data('url');
        const status = $(element).find('.status');
        console.log(index, taskId, status);
        if (status.text() === 'CHECKING' || status.text() === 'PENDING') {
            var step = 0;
            var interval = setInterval(function () {
                $.ajax({
                    url: url,
                    success: function (response) {
                        console.log(response);
                        status.text(response.state + ' : ' + step);
                        if (response.state === "SUCCESS") {
                            status.text(response.state);
                            clearInterval(interval);
                        }
                    }
                })
                step++;
            }, 1000);
        }
    })
})
