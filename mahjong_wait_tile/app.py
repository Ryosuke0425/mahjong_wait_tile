from flask import Flask,render_template,request,redirect
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.shanten import Shanten




app = Flask(__name__)

SIZE = 14

@app.route('/')
def index():
        return render_template('index.html')



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
        tiles = TilesConverter.string_to_34_array(man=man,pin=pin,sou=sou,honors=honors)
        result = shanten.calculate_shanten(tiles)
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
        result = []
        shanten = Shanten()
        man = request.form.get('man')
        pin = request.form.get('pin')
        sou = request.form.get('sou')
        honors = request.form.get('honors')


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
                        result.append((i,j+1))
        print(result)      
        return render_template('win_tile_result.html',result=result)









def calculate_shanten(inputs,nums):
    shanten = Shanten() 
    man = ''
    pin = ''
    sou = ''
    honors = ''
    for i in range(SIZE):
        if inputs[i] == 'man':
            man += nums[i]
        elif inputs[i] == 'pin':
            pin += nums[i]
        elif inputs[i] == 'sou':
            sou += nums[i]
        elif inputs[i] == 'honors':
            honors += nums[i]
    tiles = TilesConverter.string_to_34_array(man=man,pin=pin,sou=sou,honors=honors)
    result = shanten.calculate_shanten(tiles)
    return result



if __name__ == "__main__":
    app.run(debug=True)