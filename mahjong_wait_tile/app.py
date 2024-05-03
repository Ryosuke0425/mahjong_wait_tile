from flask import Flask,render_template,request,redirect
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten




app = Flask(__name__,static_folder="./templates/img")

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
        #SIZE = 4
        shanten = Shanten() 
        man = request.form.get('man')
        pin = request.form.get('pin')
        sou = request.form.get('sou')
        honors = request.form.get('honors')
        if (len(man)+len(pin) + len(sou) + len(honors)) != 14: return render_template("error.html")
        try:
            tiles = TilesConverter.string_to_34_array(man=man,pin=pin,sou=sou,honors=honors)
            result = shanten.calculate_shanten(tiles)
        except (ValueError,AssertionError,IndexError):
            return render_template("error.html")
        if result == -1:
            print('あがれる形です!')
        else:
            print('まだあがることができません!')
        return render_template('can_done_result.html',result=result)




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