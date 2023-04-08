jQuery(document).ready(function($) {
  const $isbnField = $('#id_isbn');
  const $tituloField = $('#id_titulo');

  $isbnField.on('blur', function() {
    const isbn = $(this).val();
    if (isbn.length === 13) {
      const url = `https://openlibrary.org/isbn/${isbn}.json`;
      $.ajax({
        url: url,
        dataType: 'json',
        success: function(data) {
          $tituloField.val(data.title);
        }
      });
    }
  });
});