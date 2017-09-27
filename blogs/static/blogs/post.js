/**
 * Created by lida on 28.06.17.
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

    });
