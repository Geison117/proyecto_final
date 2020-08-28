$(function () {       
        $('.confirm').click(function () {
            var edit = $(this).siblings()
            var href = edit[0].getAttribute('href') 
            href = href.split('s')
            var confirmacion = confirm('¿Está seguro que desea eliminar la institución? \n Todos los cursos y especializacones ofrecidos por la institución se eliminarán');
            if (confirmacion) {      
                location.href= '/elim_ins'+href[1]           
            }
        });          
});