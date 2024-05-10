from flask import Flask,render_template,request,redirect,url_for
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld
from mahjong.constants import EAST, SOUTH, WEST, NORTH




app = Flask(__name__,static_folder="./static")

SIZE = 14

@app.route('/')
def index():
        return render_template('index.html')

#jihai = ["東","南","西","北","白","發","中"]
#kinds = ["萬子","筒子","索子","字牌"]

@app.route('/can_done',methods=['GET','POST'])
def can_done():
    if request.method == 'GET':
        return render_template('can_done.html')
    else:
        calculator = HandCalculator()
        man = request.form.get('man')
        pin = request.form.get('pin')
        sou = request.form.get('sou')
        honors = request.form.get('honors')

        if '0' in (man+pin+sou+honors):
            has_aka_dora = True
        else:
            has_aka_dora = False
        
        print(has_aka_dora)

        tiles = TilesConverter.string_to_136_array(man=man, pin=pin, sou=sou,honors=honors,has_aka_dora=has_aka_dora)
        dora_man = request.form.get('dora_man')
        dora_pin = request.form.get('dora_pin')
        dora_sou = request.form.get('dora_sou')
        dora_honors = request.form.get('dora_honors')
        doras = TilesConverter.string_to_136_array(man=dora_man, pin=dora_pin, sou=dora_sou,honors=dora_honors)
        dora_indicators = []
        for dora in doras:
            dora_indicators.append(dora)








        melds = []
        for i in range(1,5):
            naki_i_check = request.form.get('naki_'+str(i)+'_check')
            if  naki_i_check == 'on':
                naki_i = request.form.get("naki_" + str(i))
                naki_i_type = request.form.get("naki_" + str(i) + "_type")
                naki_i_num = request.form.get("naki_" + str(i) + "_num")
                melds.append(make_melds(naki_i,naki_i_type,naki_i_num))
                print(naki_i,naki_i_check,naki_i_num,naki_i_type)
        

        is_tumo = request.form.get("is_tumo")
        is_tumo = bool(int(is_tumo))

        win_tile_type = request.form.get('win_tile_type')
        win_tile_num = request.form.get('win_tile_num')
        win_tile = make_win_tile(win_tile_type,win_tile_num)

        round_wind = request.form.get('round_wind')
        round_wind = return_wind(round_wind)
        player_wind = request.form.get('player_wind')
        player_wind = return_wind(player_wind)

        has_open_tanyao = on_to_true(request.form.get('has_open_tanyao'))

        is_riichi = on_to_true(request.form.get('is_riichi'))
        is_daburu_riichi = on_to_true(request.form.get('is_daburu_riichi'))
        #is_riichi = True if is_riichi == "on" else False
        is_ippatsu = on_to_true(request.form.get('is_ippatsu'))
        #is_ippatsu = True if is_ippatsu == "on" else False
        is_haitei = on_to_true(request.form.get('is_haitei'))
        #is_haitei = True if is_haitei == "on" else False
        is_houtei = on_to_true(request.form.get('is_houtei'))
        #is_houtei = True if is_houtei == "on" else False 
        is_chankan = on_to_true(request.form.get('is_chankan'))
        #is_chankan = True if is_chankan == "on" else False      
        is_tenhou = on_to_true(request.form.get('is_tenhou'))
        is_renhou = on_to_true(request.form.get('is_renhou'))
        is_chiihou = on_to_true(request.form.get('is_chiihou')) 

        result = calculator.estimate_hand_value(tiles, win_tile, melds=melds,dora_indicators=dora_indicators,
    config=HandConfig(is_riichi=is_riichi, is_daburu_riichi=is_daburu_riichi, is_tsumo=is_tumo, is_ippatsu=is_ippatsu, is_haitei=is_haitei,is_houtei=is_houtei,
                      is_tenhou=is_tenhou,is_renhou=is_renhou,is_chiihou=is_chiihou,
                      player_wind=player_wind, round_wind=round_wind,
                      options=OptionalRules(has_open_tanyao=has_open_tanyao,has_aka_dora=has_aka_dora)))
        print(type(has_open_tanyao))
        print(result.yaku)

        return render_template('can_done_result.html')










        #if (len(man)+len(pin) + len(sou) + len(honors)) != 14: return render_template("error.html")
        #try:
        #    tiles = TilesConverter.string_to_34_array(man=man,pin=pin,sou=sou,honors=honors)
        #    result = shanten.calculate_shanten(tiles)
        #except (ValueError,AssertionError,IndexError):
        #    return render_template("error.html")
        #if result == -1:
        #    print('あがれる形です!')
        #else:
        #    print('まだあがることができません!')
        #return render_template('can_done_result.html',result=result)




@app.route('/win_tile',methods=['GET','POST'])
def win_tile():
    if request.method == 'GET':
        return render_template('win_tile.html')
    else:
        result_1 = []
        shanten = Shanten()
        man = request.form.get('man')
        pin = request.form.get('pin')
        sou = request.form.get('sou')
        honors = request.form.get('honors')
        if (len(man)+len(pin) + len(sou) + len(honors)) != 13: return render_template("error.html")


        for i in range(4):
            for j in range(9):
                man_j,pin_j,sou_j,honors_j = man,pin,sou,honors

                if i == 0:
                    man_j = man + str(j+1)
                elif i == 1:
                    pin_j = pin + str(j+1)
                elif i == 2:
                    sou_j = sou + str(j+1)
                elif (i == 3) and (j < 7):
                    honors_j = honors + str(j+1)  
                try:
                    tiles = TilesConverter.string_to_34_array(man=man_j,pin=pin_j,sou=sou_j,honors=honors_j)
                    if shanten.calculate_shanten(tiles) == -1:
                        result_1.append((str(i),str(j+1)))
                except (ValueError,AssertionError,IndexError):
                    return render_template("error.html")
        #result_2 = convert_num_list(result_1)
        #result_1 = make_path_list(result_1)
        #print(result)      
        return render_template('win_tile_result.html',result_1=result_1,ran=len(result_1))

def find_tenpais(man,pin,sou,honors):
    result = []
    for i in range(len(man) - 1):
        result.append(find_tenpai(man=man[:i]+man[i+1:],pin=pin,sou=sou,honors=honors))
    if len(man) != 0: result.append(find_tenpai(man=man[:-1],pin=pin,sou=sou,honors=honors))
    for i in range(len(pin)-1):
        result.append(find_tenpai(man=man,pin=pin[:i]+pin[i+1:],sou=sou,honors=honors))
    if len(pin) != 0: result.append(find_tenpai(man=man,pin=pin[:-1],sou=sou,honors=honors))    
    for i in range(len(sou)-1):
        result.append(find_tenpai(man=man,pin=pin,sou=sou[:i]+sou[i+1:],honors=honors))
    if len(sou) != 0: result.append(find_tenpai(man=man,pin=pin,sou=sou[:-1],honors=honors))
    for i in range(len(honors)-1):
        result.append(find_tenpai(man=man,pin=pin,sou=sou,honors=honors[:i]+honors[i+1:]))
    if len(honors) != 0: result.append(find_tenpai(man=man,pin=pin,sou=sou,honors=honors[:-1]))            
    return result
    
def find_tenpai(man,pin,sou,honors):
    result = []
    shanten = Shanten()
    for i in range(4):
        for j in range(9):
            man_j,pin_j,sou_j,honors_j = man,pin,sou,honors
            if i == 0:
                man_j = man + str(j+1)
            elif i == 1:
                pin_j = pin + str(j+1)
            elif i == 2:
                sou_j = sou + str(j+1)
            elif (i == 3) and (j < 7):
                honors_j = honors + str(j+1)

            tiles = TilesConverter.string_to_34_array(man=man_j,pin=pin_j,sou=sou_j,honors=honors_j)
            if shanten.calculate_shanten(tiles) == -1:
                result.append((str(i),str(j+1)))

    return result    






@app.route('/what_to_discard',methods=['GET','POST'])
def what_to_discard():
    if request.method == 'GET':
        return render_template("what_to_discard.html")
    else:
        man = request.form.get('man')
        pin = request.form.get('pin')
        sou = request.form.get('sou')
        honors = request.form.get('honors')
        if (len(man)+len(pin) + len(sou) + len(honors)) != 14: return render_template("error.html")
        print(find_tenpais(man=man,pin=pin,sou=sou,honors=honors))
        try:
            result_1 = find_tenpais(man=man,pin=pin,sou=sou,honors=honors)
            result_2 = make_path(man=man,pin=pin,sou=sou,honors=honors)
        except (ValueError,AssertionError,IndexError):
            return render_template("error.html")
        return render_template("what_to_discard_result.html",result_1=result_1,result_2=result_2)



def make_win_tile(win_tile_type,win_tile_num):
    man = ''
    pin = ''
    sou = ''
    honors = ''
    if win_tile_type == 'man':
        man += win_tile_num
    elif win_tile_type == 'pin':
        pin += win_tile_num
    elif win_tile_type == 'sou':
        sou += win_tile_num
    elif win_tile_type == 'honors':
        honors += win_tile_num 
    return TilesConverter.string_to_136_array(man=man,pin=pin,sou=sou,honors=honors)[0]


def return_wind(wind):
    if wind == "east":
        return EAST
    elif wind == "south":
        return SOUTH
    elif wind == "west":
        return WEST
    elif wind == "north":
        return NORTH
        
def on_to_true(s):
    result = True if s == "on" else False
    return result









def make_melds(naki,naki_type,naki_num):
    man = ''
    pin = ''
    sou = ''
    honors = ''
    if naki_type == 'man':
        man += naki_num
    elif naki_type == 'pin':
        pin += naki_num
    elif naki_type == 'sou':
        sou += naki_num
    elif naki_type == 'honors':
        honors += naki_num 
    if '0' in naki_num:
        aka_dora = True
    else:
        aka_dora = False
    
    if naki == 'chi':
        return Meld(meld_type=Meld.CHI, tiles=TilesConverter.string_to_136_array(man=man,pin=pin,sou=sou,honors=honors,has_aka_dora=aka_dora))
    elif naki == 'pon':
        return Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(man=man,pin=pin,sou=sou,honors=honors,has_aka_dora=aka_dora))
    elif naki == 'kan_false':
        return Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=man,pin=pin,sou=sou,honors=honors,has_aka_dora=aka_dora),opened=False)
    elif naki == 'kan_true':
        return Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=man,pin=pin,sou=sou,honors=honors,has_aka_dora=aka_dora))




#def convert_num_list(l):
#    result = []
#    for pair in l:
#        if pair[0] == 3:
#            result.append(kinds(pair[0])) + " " + jihai(pair[1])
#        else:
#            result.append(kinds(pair[0])) + " " + str(pair[1])
#    return result








def make_path(man,pin,sou,honors):
    result = []
    for m in man:
        result.append(('0',m))
    for p in pin:
        result.append(('1',p))
    for s in sou:
        result.append(('2',s))
    for h in honors:
        result.append(('3',h))    
    return result





#def make_path_list(l):
#    return list(map(make_path,l))



#def make_path(pair):
#    return str(pair[0]) + str(pair[1])

#def calculate_shanten(inputs,nums):
#    shanten = Shanten() 
##    man = ''
#    pin = ''
#    sou = ''
#    honors = ''
#    for i in range(SIZE):
#        if inputs[i] == 'man':
#            man += nums[i]
#        elif inputs[i] == 'pin':
#            pin += nums[i]
#        elif inputs[i] == 'sou':
#            sou += nums[i]
#        elif inputs[i] == 'honors':
#            honors += nums[i]
#    tiles = TilesConverter.string_to_34_array(man=man,pin=pin,sou=sou,honors=honors)
#   result = shanten.calculate_shanten(tiles)
#    return result



if __name__ == "__main__":
    app.run(debug=True)