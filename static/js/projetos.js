$(document).ready(function () {
	$('#projeto_thumbnail').awesomeCropper(
		{ width: 200, height: 200 }
	);
});
$(".btn_file").on('click', function() {
   $('.input_file').click();
});

/*
=====================
 EXCLUIR PROJETO
=====================
*/

$(".excluir_projeto").click(function() {
  var mensagem_confirma = 'Tem certeza que deseja excluir esse projeto?';
  if(confirm(mensagem_confirma)) {
    var id_projeto = this.id;
    var url = urlExcluiProjeto+id_projeto;
    window.location.replace=url;
  }
});

function openProject(url){
	//console.log(url.toString());
	window.location.href = url.toString();
}

$('.main-list').on('click', function(e) {
    url = this.getAttribute("data-url");
		openProject(url);
		//console.log(url);
		//console.log(this);
}).on('click', '.excluir_projeto', function(e) {
    e.stopPropagation();
});
