$(function () {       
    $('.confirm').click(function () {
        var edit = $(this).siblings()
        var href = edit[0].getAttribute('href') 
        href = href.split('p')
        var confirmacion = confirm('¿Está seguro que desea eliminar la especialización? \n La especialización no estará más disponible para los estudiantes');
        if (confirmacion) {      
            location.href= '/elim_esp'+href[1]           
        }
    });          
});