var pontoazul = 0;
var pontobranco = 0;


function quiz() {


    
}





$(".btnwhite").on("click", function () {
    console.log('clicou')
    var ponto = parseInt(this.value)
    pontobranco  = pontobranco + ponto;
    console.log(pontobranco)

    if (pontobranco >= 0)  {
        
    
    $(".white").text(pontobranco)
    
    }else{

        $(".white").text(0)
    }
})


$(".btnblue").on("click", function () {
    console.log('clicou')
    var ponto = parseInt(this.value)
    pontoazul  = pontoazul + ponto;
    console.log(pontoazul)

    if (pontoazul >= 0)  {
        
    
    $(".bluee").text(pontoazul)
    
    }else{

        $(".bluee").text(0)
    }
})



setTimeout(() => {

    $(".center").animate({"opacity":"1"},500)

    
}, 1100);


setTimeout(() => {

    $(".quiz").animate({"opacity":"60%"},500)

    
}, 2100);