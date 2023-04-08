jQuery(document).ready(function($) {
  const $cepField = $('#id_cep');
  const $enderecoField = $('#id_endereco');
  const $bairroField = $('#id_bairro');
  const $cidadeField = $('#id_cidade');
  const $estadoField = $('#id_estado');

  $cepField.on('blur', function() {
    const cep = $(this).val();
    if (cep.length === 8) {
      const url = `https://viacep.com.br/ws/${cep}/json/`;
      $.ajax({
        url: url,
        dataType: 'json',
        success: function(data) {
          $enderecoField.val(data.logradouro);
          $bairroField.val(data.bairro);
          $cidadeField.val(data.localidade);
          $estadoField.val(data.uf);
        }
      });
    }
  });
});