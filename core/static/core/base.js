/**
 * Created by lida on 13.04.17.
 */
$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load().attr('data-url');
        });

//дополнение
        //на всем документе проверяем типы просто
        $(document).on('submit', '.ajaxblog', function () {
            //то что будет происходить
            var form = $(this);
            $.post(
                form.attr('action'),
                form.serialize(), function (data) {
                    if (data == 'OK') {
                        document.location.href = document.location.href;
                    }
                    form.html(data);
                });
            return false;
        });

        $(".buton").click(function () {
            $("#basicModal").modal();
            $('.modal-body').load($(this).attr('href'));
            return false;
        });

        $(document).on('submit', '.ajaxpost', function () {
            //то что будет происходить
            var form = $(this);
            $.post(
                form.attr('action'),
                form.serialize(), function (data) {
                    if (data == 'OK') {
                        document.location.href = document.location.href;
                    }
                    form.html(data);
                });
            return false;
        });



        function updateComments() {
            $('#likecount').each(function () {
                $(this).load($(this).data('post-url'));
            });
        }



        function updateLikes() {
            $('.ajaxlike').each(function () {
                $(this).load($(this).data('url'));
            });
        }
        updateLikes();
        window.setInterval(updateLikes, 1000);

        $(".ajaxlike").click(function () {
            var url = $(this).data('url');
            var element = $(this);
            $.post(url, function (data) {
                element.html(data);
            })
        });

        $("#tags").chosen();



        $(document).ready(
            function () {

                function csrfSafeMethod(method) {
                    // these HTTP methods do not require CSRF protection
                    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                }

                $.ajaxSetup({
                    beforeSend: function (xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                        }
                    }
                });

            }
        );

        $(document).ready(
            window.setInterval(
            function () {
                $(".commentsdiv").each(function () {
                    $(this).load($(this).data('url'))
                })
            }, 5000)
        )


    });
//autoload = элемент который будет загружаться
//data-url = url с которого булу загружаться данные параметры