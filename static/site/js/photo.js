
    $(function() {
        $('.add-photo').click(function(ev){
            ev.preventDefault();
            var count = parseInt($('#id_gallery_set-TOTAL_FORMS').attr('value'), 10);
            var tmplMarkup = $('#gallery-template').html();
            var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count)
            console.log(compiledTmpl);
            $('div.gallery').append(compiledTmpl);
            $('#id_gallery_set-TOTAL_FORMS').attr('value', count + 1);
        });
    });


   $( function() {
     $( "#id_birth_date, #id_member_since, #id_member_start_date, #id_member_end_date" ).attr("placeholder", "mm/dd/yyyy").datepicker();
   } );



   $(document).ready( function() {

        $("#mycarousel").carousel( { interval: 2000 } );
              $("#carousel-pause").click(function(){
            $("#mycarousel").carousel('pause');
        });

        $("#carousel-play").click(function(){
            $("#mycarousel").carousel('cycle');
        });



    });

