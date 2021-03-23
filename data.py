
# importing the necessary dependency
from flask import Flask, request, render_template
from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
import os


app = Flask(__name__) # initializing a flask app
#model = pickle.load(open('cement.pkl', 'rb'))


@app.route('/')
def prediction():
    return render_template('home.html')
@app.route('/intro')
def my_home():
    return render_template('newhome.html')
@app.route('/aug')
def aug():
    return render_template('index6.html')
@app.route('/predict',methods=['POST']) # route to show the predictions in a web UI
def index():
    try:
        if request.method=='POST':
            #print("inside index function")
            #  reading the inputs given by the use
            rotation_range=float(request.form['rotation_range'])
            width_shift_range=float(request.form['width_shift_range'])
            height_shift_range=float(request.form['height_shift_range'])
            shear_range=float(request.form['shear_range'])
            zoom_range=float(request.form['zoom_range'])
            horizontal_flip=request.form['horizontal_flip']
            fill_mode=request.form['fill_mode']
            num=int(request.form['num'])
            prefix=request.form['prefix']
            pd=request.form['pd']
            fn=request.form['fn']
            x=[rotation_range,width_shift_range,height_shift_range,
            shear_range,zoom_range,horizontal_flip,fill_mode]
            print(x)
            
              
            # Path 
            path = os.path.join(pd, fn) 
              
            # Create the directory 
            # 'GeeksForGeeks' in 
            # '/home / User / Documents' 
            os.mkdir(path) 
            
            datagen = ImageDataGenerator(
                rotation_range=x[0],
                width_shift_range=x[1],
                height_shift_range=x[2],
                shear_range=x[3],
                zoom_range=x[4],
                horizontal_flip=x[5],
                fill_mode=x[6])
            f=request.files['file'] #requesting the file
            basepath=os.path.dirname('__file__')#storing the file directory
            filepath=os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
            f.save(filepath)#saving the file
            print(filepath)
            img = load_img(filepath)
                 #load and reshaping the image
            x1=img_to_array(img)#converting image to array
            x1 = x1.reshape((1,) + x1.shape)#changing the dimensions of the image

            print(str(fn))
            i=0
            for batch in datagen.flow(x1, batch_size=1,
                              save_to_dir= str(fn), save_prefix=prefix, save_format='jpg'):
                i += 1
                if i > num:
                    break 
        
        return ("Data agumentation is done. Check your results in "+ str(fn) +" folder")
    except:
        return ("Create a preview folder or fill all the fields and try again!!!!!!!!!!")

if __name__ == "__main__":
    #app.run('0.0.0.0',8000)
    #app.run(host='127.0.0.1', port=8001, debug=True)
    #app.run(debug=False) # running the app
     app.run(debug=False) #local host 5000
     
