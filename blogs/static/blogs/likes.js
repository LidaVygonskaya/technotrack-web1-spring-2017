/**
 * Created by lida on 16.04.17.
 */
      $(document).ready(function () {
            var ids = Array();
            function updateLikes() {
                $('.likecount').each(function () {
                    ids.push($(this).data('post-id'));
                });

                $.getJSON('/blogs/posts/likes/', {ids: ids.join(',')}, function () {

                });
            }
            window.setInterval(updateLikes, 5000)
        });