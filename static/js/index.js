jQuery.expr[':'].icontains = function (a, i, m) {
    return jQuery(a).text().toUpperCase()
            .indexOf(m[3].toUpperCase()) >= 0;
};

$(document).ready(function () {
//     $('#carousel-example-generic').carousel({
//   interval: 2000
// })
    $('#searchPlatform').on('input', function (e) {
        var text = $(this).val().trim();
        refreshDataList(text)

    });
    $('.searchTags span').click(function (e) {
         var text = $(this).text().trim();
         $('#searchPlatform').val(text);
         refreshDataList(text);
    });
    $('.logTrace').click(function (e) {
        var areaType=$(this).data('area');
        var target=$(this).data('target');
        var propertyData=$(this).data('propertydata');
// $.ajax({url:'/minibond/log/'+areaType+"/"+target+"/"+propertyData+"/",async:true});
         $.ajax({
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            type: 'GET',
            async:true,
            url: '/minibond/log/'+areaType+"/"+target+"/"+propertyData+"/"
        });
    });

    function refreshDataList(text) {
        if ("" === text || "全部"===text) {
            $(".bs-callout").removeClass('hidden');
        }
        else{
            $(".bs-callout:not(:icontains(" + text + "))").addClass('hidden');
            $(".bs-callout:icontains(" + text + ")").removeClass('hidden');
        }

    }
});