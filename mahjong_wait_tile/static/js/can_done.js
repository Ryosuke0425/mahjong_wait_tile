function change(){
    const naki_1 = document.getElementById('naki_1');
    const naki_1_check = document.querySelector('input[name="naki_1_check"]');
    console.log(naki_1);
    naki_1.disabled = false;
}


function change1(ischecked){
    document.getElementById('naki_1').disabled = !ischecked;
    nakiTrue = nakiCheck();
    const tsumo = document.getElementById('is_tsumo').checked;
    changeCheck(tsumo,nakiTrue);
}


function change2(ischecked){
    document.getElementById('naki_2').disabled = !ischecked;
    nakiTrue = nakiCheck();
    const tsumo = document.getElementById('is_tsumo').checked;
    changeCheck(tsumo,nakiTrue);
}


function change3(ischecked){
    document.getElementById('naki_3').disabled = !ischecked;
    nakiTrue = nakiCheck();
    const tsumo = document.getElementById('is_tsumo').checked;
    changeCheck(tsumo,nakiTrue);
}


function change4(ischecked){
    document.getElementById('naki_4').disabled = !ischecked;
    nakiTrue = nakiCheck();
    const tsumo = document.getElementById('is_tsumo').checked;
    changeCheck(tsumo,nakiTrue);
}


function tsumoRonClick(tsumo){
        var nakiTrue = nakiCheck();
        changeCheck(tsumo,nakiTrue);
}

function nakiCheck(){
    const naki = document.getElementsByClassName('naki_check');
    var result = false;
    for(var i = 0;i < naki.length;i++){
        result = result || naki[i].checked;
    }
    return result;
}

//暗槓以外の鳴きならtrue,暗槓ならfalseを返す    
//function kanFalseCheck(){
//    var result = false;
//    for(var i = 0;i < 4;i++){
//        const naki = document.getElementById('nakicheck' + String(i+1)).checked;
//        const kanFalse = document.querySelector('input[name=naki_' + String(i+1) + ']:checked').value == 'kan_false';
//        result = result || (naki && !kanFalse);
//    }
//    return result;
//}


//暗槓のみtrueを返す
function kanFalseCheck1(){
    var result = false;
    for(var i = 0;i < 4;i++){
        const naki = document.getElementById('nakicheck' + String(i+1)).checked;
        const kanFalse = document.querySelector('input[name=naki_' + String(i+1) + ']:checked').value == 'kan_false';
        result = result || (naki && kanFalse);
    }
    return result;
}



//暗槓以外の鳴きをしている際にtrueを返す
function nakiOtherThanKanFalseCheck(){
    const naki = document.getElementsByClassName('naki_check');
    var result = false;
    for(var i = 0;i < naki.length;i++){
        const kanFalse = document.querySelector('input[name=naki_' + String(i+1) + ']:checked').value == 'kan_false';
        result = result || (naki[i].checked && !kanFalse);
    }
    return result;
}

function changeCheck(tsumo,nakiTrue){
    const isRiichi = document.getElementById('is_riichi').checked;
    const isDaburuRiichi = document.getElementById('is_daburu_riichi').checked;
    var isIppatsu = document.getElementById('is_ippatsu').checked;
    const isHaitei = document.getElementById('is_haitei').checked;
    const isHoutei = document.getElementById('is_houtei').checked;
    const isRinshan = document.getElementById('is_rinshan').checked;
    const isChankan = document.getElementById('is_chankan').checked;

    const isFirst = document.getElementById('is_first').checked;

    const kanFalse = kanFalseCheck1();
    const nakiOtherThanKanFalse = nakiOtherThanKanFalseCheck();
    const isNotFirst = isRiichi || isDaburuRiichi || isIppatsu || isHaitei || isHoutei || isRinshan || isChankan;



    //document.getElementById('is_riichi').disabled = !(!nakiTrue && !isDaburuRiichi && !isFirst);
    //document.getElementById('is_daburu_riichi').disabled = !(!nakiTrue && !isRiichi && !isFirst);
    //document.getElementById('is_ippatsu').disabled = !(!nakiTrue && (isRiichi || isDaburuRiichi) && !isRinshan && !isFirst);
    //document.getElementById('is_haitei').disabled = !(tsumo && !isRinshan && !isFirst);
    //document.getElementById('is_houtei').disabled = !(!tsumo && !isChankan && !isFirst);
    //document.getElementById('is_rinshan').disabled = !(tsumo && !isIppatsu && !isHaitei && !isFirst)
    //document.getElementById('is_chankan').disabled = !(!tsumo && !isHoutei && !isFirst)
    //document.getElementById('is_tenhou').disabled = !(tsumo && !nakiTrue && !isChiihou && !isNotFirst);
    //document.getElementById('is_renhou').disabled = !(!tsumo && !nakiTrue && !isNotFirst);
    //document.getElementById('is_chiihou').disabled = !(tsumo && !nakiTrue && !isTenhou && !isNotFirst);
    //document.getElementById('is_riichi').disabled = !(!kanFalse && !isDaburuRiichi && !isFirst);

    //document.getElementById('is_riichi').disabled = !((!nakiTrue || kanFalse) && !isDaburuRiichi && !isFirst);
    document.getElementById('is_riichi').disabled = !(!nakiOtherThanKanFalse && !isDaburuRiichi && !isFirst);

    //document.getElementById('is_daburu_riichi').disabled = !(!kanFalse && !isRiichi && !isFirst && !(isIppatsu && (isHaitei || isHoutei || isChankan || !kanFalse)));
    //document.getElementById('is_daburu_riichi').disabled = !((!nakiTrue || kanFalse) && !isRiichi && !isFirst && !(isIppatsu && (isHaitei || isHoutei || isChankan || kanFalse)));
    document.getElementById('is_daburu_riichi').disabled = !(!nakiOtherThanKanFalse && !isRiichi && !isFirst && !(isIppatsu && (isHaitei || isHoutei || isChankan || kanFalse)));




    //document.getElementById('is_ippatsu').disabled = !(!kanFalse && (isRiichi || isDaburuRiichi) && !isRinshan && !isFirst && !(isDaburuRiichi && (isHaitei || isHoutei || isChankan || !kanFalse)));
    //document.getElementById('is_ippatsu').disabled = !((!nakiTrue || kanFalse) && (isRiichi || isDaburuRiichi) && !isRinshan && !isFirst && !(isDaburuRiichi && (isHaitei || isHoutei || isChankan || kanFalse)));
    document.getElementById('is_ippatsu').disabled = !(!nakiOtherThanKanFalse && (isRiichi || isDaburuRiichi) && !isRinshan && !isFirst && !(isDaburuRiichi && (isHaitei || isHoutei || isChankan || kanFalse)));
    //if(document.getElementById('is_ippatsu').disabled == true){
    //   document.getElementById('is_ippatsu').checked = false;
    //    isIppatsu = false
    //}

    //console.log(!(isDaburuRiichi && (isHaitei || isHoutei || isChankan)));
    //console.log(isIppatsu);

    document.getElementById('is_haitei').disabled = !(tsumo && !isRinshan && !isFirst && !(isDaburuRiichi && isIppatsu));
    document.getElementById('is_houtei').disabled = !(!tsumo && !isChankan && !isFirst && !(isDaburuRiichi && isIppatsu));
    document.getElementById('is_rinshan').disabled = !(tsumo && !isIppatsu && !isHaitei && !isFirst)
    document.getElementById('is_chankan').disabled = !(!tsumo && !isHoutei && !isFirst && !(isDaburuRiichi && isIppatsu));
    //document.getElementById('is_tenhou').disabled = !(tsumo && !nakiTrue && !isChiihou && !isNotFirst && isEast);
    //document.getElementById('is_renhou').disabled = !(!tsumo && !nakiTrue && !isNotFirst);
    //document.getElementById('is_chiihou').disabled = !(tsumo && !nakiTrue && !isTenhou && !isNotFirst && !isEast);
    document.getElementById('is_first').disabled = !(tsumo && !nakiTrue && !isNotFirst);
    deleteCheck();
}


function yakuCheck(){
    const nakiTrue = nakiCheck();
    const tsumo = document.getElementById('is_tsumo').checked;
    changeCheck(tsumo,nakiTrue);
}


function deleteCheck(){
    yakus = document.getElementsByClassName('yaku');
    for(var i = 0;i < yakus.length; i++){
        if(yakus[i].checked==true && yakus[i].disabled==true){
            yakus[i].checked = false;
        }
    }
}


function check(){
    let text = "";
    const man = document.getElementById('man').value;
    const pin = document.getElementById('pin').value;
    const sou = document.getElementById('sou').value;
    const honors = document.getElementById('honors').value;
    const win_tile_num = document.getElementById('win_tile_num').value;
    const naki1 = document.getElementById('win_tile_num').value;
    const melds = document.getElementsByClassName('naki_check');
    let all = man + pin + sou + honors + win_tile_num;
    if (isNaN(man)){
        text += "萬子:半角数値のみを入力してください。\n";
    }
    if (isNaN(pin)){
        text += "筒子:半角数値のみを入力してください。\n";
    }
    if (isNaN(sou)){
        text += "索子:半角数値のみを入力してください。\n";
    }
    if (isNaN(honors)){
        text += "字牌:半角数値のみを入力してください。\n";
    }else if(honorsCheck(honors)){
        text += "字牌:字牌は1~7を入力してください。\n";
    }
    if (win_tile_num==""){
        text += "上がり牌:入力してください。 \n";
    }else{
        if (isNaN(win_tile_num)){
            text += "上がり牌:半角数値のみを入力してください。\n";
        }
    }

    for(var i = 0;i<melds.length;i++){
        const naki_i = document.getElementsByName('naki_' + String(i+1));
        if(melds[i].checked==true){
            const naki_i_num = document.getElementById('naki_' + String(i+1) + '_num').value;
            if(naki_i[0].checked){
                text += chiCheck(i,naki_i_num);
                all += naki_i_num;
            }else if(naki_i[1].checked){
                text += ponCheck(i,naki_i_num);
                all += naki_i_num;
            }else if(naki_i[2].checked || naki_i[3].checked){
                text += kanCheck(i,naki_i_num);
                all += naki_i_num.slice(0,3);
            }
        }
    }
    if(all.length != 14){
        text +="牌の合計枚数が合いません\n";
    }
    text += countCheck();
    if(text.length != 0){
        //alert(text.length);
        alert(text);
    }
    countCheck();
    return text.length==0;
}



function countCheck(){
    let text = "";
    let tf = false;
    const types = ['man','pin','sou','honors'];
    var array = {'man':'','pin':'','sou':'','honors':''};

    array[document.querySelector('input[name=win_tile_type]:checked').value] += document.getElementById('win_tile_num').value;

    for(var i =0; i < 4;i++){
        if(document.getElementById('nakicheck' + String(i+1)).checked==true){
            array[document.querySelector('input[name=naki_' + String(i+1) + '_type]:checked').value] += document.getElementById('naki_'+String(i+1)+'_num').value;
        }
    }
    for(var i = 0;i < types.length;i++){
        array[types[i]] += document.getElementById(types[i]).value + document.getElementById('dora_' + types[i]).value;
        array[types[i]] = array[types[i]].replace(/0/g,'5');
    }

    for(var i = 0;i<9;i++){
        for(var j = 0;j < types.length; j++){
            if(array[types[j]].split(String(i+1)).length > 5){
                return "同じ牌は5枚以上入力できません\n";
            }
        }
    }
    return '';
}







function chiCheck(i,value){
    let text = "";
    if(document.querySelector('input[name=naki_' + String(i+1) + '_type]:checked').value == 'honors'){
        text += "字牌チーはできません。\n";
    }else if (value.length!=3){
        text += "3枚の牌を入力してください。\n";
    }else{
        if(isNaN(value)){
            text += "半角数値のみを入力してください。\n";
        }else{
            value = value.replace(/0/g,"5");
            chi = value.split('').sort();
            if(!(chi[0] == chi[1] - 1 && chi[1] == chi[2] - 1)){
                text += "連続した3枚を入力してください。\n"
            }
        }
    }
    if(text.length != 0){
        text = "鳴き" + String(i+1) +" : " + text;
    }
    return text;
}

function ponCheck(i,value){
    let text = "";
    const isHonors = document.querySelector('input[name=naki_' + String(i+1) + '_type]:checked').value == 'honors';
    if (value.length!=3){
        text += "3枚の牌を入力してください。\n";
    }else{
        if(isNaN(value)){
            text += "半角数値のみを入力してください。\n";
        }else if(isHonors&&honorsCheck(value)){
            //console.log(isHonors);
            text += "字牌は1~7を入力してください。\n";
        }else{
            pon = value.replace(/0/g,"5");
            console.log(pon);
            if(!(pon[0] == pon[1] && pon[1] == pon[2] )){
                text += "3枚同じ牌を入力してください。\n"
            }
        }
    }
    if(text.length != 0){
        text = "鳴き" + String(i+1) +" : " + text;
    }
    return text;
}

function kanCheck(i,value){
    let text = "";
    //この鳴きが字牌かどうか
    const isHonors = document.querySelector('input[name=naki_' + String(i+1) + '_type]:checked').value == 'honors';
    if (value.length!=4){
        text += "4枚の牌を入力してください。\n";
    }else{
        if(isNaN(value)){
            text += "半角数値のみを入力してください。\n";
        }else if(isHonors&&honorsCheck(value)){
            //console.log(isHonors);
            text += "字牌は1~7を入力してください。\n";
        }else{
            kan = value.replace(/0/g,"5");
            if(!(kan[0] == kan[1] && kan[1] == kan[2] && kan[2] == kan[3])){
                text += "4枚同じ牌を入力してください。\n"
            }
        }
    }
    if(text.length != 0){
        text = "鳴き" + String(i+1) +" : " + text;
    }
    return text;
}

function honorsCheck(value){
    return value.includes('8') || value.includes('9') || value.includes('0');
}

function ChiPonClick(n){
    document.getElementById('naki_' + String(n) + '_num').maxLength = 3;
    document.getElementById('naki_' + String(n) + '_num').value = "";
    yakuCheck();

}

function KanClick(n){
    document.getElementById('naki_' + String(n) + '_num').maxLength = 4;
    document.getElementById('naki_' + String(n) + '_num').value = "";
    yakuCheck();
}