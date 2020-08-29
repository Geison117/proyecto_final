$(function () {       
    $('.confirm').click(function () {
        var edit = $(this).siblings()
        var href = edit[0].getAttribute('href') 
        href = href.split('r')
        var confirmacion = confirm('¿Está seguro que desea eliminar el curso? \n El curso no estará más disponible para los estudiantes ni para las especializaciones');
        if (confirmacion) {      
            location.href= '/elim_cur'+href[1]           
        }
    });          
});