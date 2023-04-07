$(document).ready(function() {
  $('#id_isbn').on('blur', function() {
    var isbn = $(this).val();
    $.ajax({
      url: '/obter_informacoes_livro/',
      type: 'GET',
      data: {'isbn': isbn},
      success: function(data) {
        $('#id_titulo').val(data.titulo);
        $('#id_autor').val(data.autor);
        // Atualize os outros campos com as informações relevantes
      },
      error: function(xhr, status, error) {
        // Lida com erros de requisição, se necessário
      }
    });
  });
});