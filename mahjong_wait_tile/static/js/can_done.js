function change(){
    const naki_1 = document.getElementById('naki_1');
    const naki_1_check = document.querySelector('input[name="naki_1_check"]');
    console.log(naki_1);
    naki_1.disabled = false;
}


function change1(ischecked){
    if(ischecked==true){
        document.getElementById('naki_1').disabled = false;
    }else{
        document.getElementById('naki_1').disabled = true;
    }
}



function change2(ischecked){
    if(ischecked==true){
        document.getElementById('naki_2').disabled = false;
    }else{
        document.getElementById('naki_2').disabled = true;
    }
}

function change3(ischecked){
    if(ischecked==true){
        document.getElementById('naki_3').disabled = false;
    }else{
        document.getElementById('naki_3').disabled = true;
    }
}

function change4(ischecked){
    if(ischecked==true){
        document.getElementById('naki_4').disabled = false;
    }else{
        document.getElementById('naki_4').disabled = true;
    }
}