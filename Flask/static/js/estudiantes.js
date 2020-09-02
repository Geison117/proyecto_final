
$( document ).ready(function() {

    var now = new Date();

    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);

    var today = now.getFullYear()+"-"+(month)+"-"+(day) ;
    $("#fecha").attr('max', today);

});

$(function () {
    $("#fecha").datepicker({
        firstDay: 1,
        monthNames: ['Enero', 'Febrero', 'Marzo',
        'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre',
        'Octubre', 'Noviembre', 'Diciembre'],
        dayNamesMin: ['DO', 'LU', 'MA', 'MI', 'JU', 'VI', 'SA'],
        changeMonth: true,
        changeYear: true,
        dateFormat: 'yy-mm-dd',
        monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
        'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    });
});

