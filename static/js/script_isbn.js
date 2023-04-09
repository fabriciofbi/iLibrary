jQuery(document).ready(function($) {
  const $isbnField = $('#id_isbn');
  const $tituloField = $('#id_titulo');
  const $anoField = $('#id_ano');
  const $editoraField = $('#id_editora');
  const $autorField = $('#id_autor');

  $isbnField.on('blur', function() {
    const isbn = $(this).val();
    if (isbn.length === 13) {
      const url = `https://openlibrary.org/isbn/${isbn}.json`;
      $.ajax({
        url: url,
        dataType: 'json',
        success: function(data) {
          $tituloField.val(data.title);
          // Extrai apenas o ano da data de publicação
          var publishDate = data.publish_date;
          var year = publishDate.split(', ')[1]; // Obtém o ano (segunda parte da string após a vírgula)
          $anoField.val(year);
          $editoraField.val(data.publishers[0]);
          // Obtém o ID do autor
          var authorId = data.authors[0].key.replace('/authors/', '');
          // Faz uma nova chamada AJAX para obter os detalhes do autor
          $.ajax({
            url: `https://openlibrary.org/authors/${authorId}.json`,
            dataType: 'json',
            success: function(authorData) {
              // Define o valor do campo 'id_autor' com o nome do autor obtido do AJAX
              $autorField.val(authorData.name);
            }
          });
        }
      });
    }
  });
});