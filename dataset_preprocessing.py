import matplotlib.pyplot as plt
import numpy as np
import cv2
import os


'''
Preprocessing to the images generated by the optical flow transformation.
The dimensions of the generated images are modified
since only the information related to eye movement is required.

There are movements with a larger displacement than others, 
that is why a list of sizes is included in which the images will fit in a square LxL shape.
the sizes are:
[350,450,550,650,750,850,950,1050,1100,1170,1190,1200,1250]
'''

'''
Input requirements
carpeta_origen= folder where the images of the optical flux transformation are located
carpeta_destino= final folder where the dataset will be stored.
'''
carpeta_origen= '/home/rtx3060a/Desktop/Alea/res/'  #Place here your folder
carpeta_destino='/home/rtx3060a/Desktop/Alea/gazecom/'  #Place here your folder


lista_tamaños=[350,450,550,650,750,850,950,1050,1100,1170,1190,1200,1250]
ent_input_dir_img = carpeta_origen
input_img_paths = sorted(

    
        os.path.join(ent_input_dir_img, fname)
        for fname in os.listdir(ent_input_dir_img) 
        if fname.endswith(".png")
    
)

for n in range(0,len(input_img_paths)):
    image = plt.imread(input_img_paths[n])
    tamaños=[]
    for i in range(image.shape[0]):
            if np.sum(image[i,:,:])> 0:
                #print(i)
                tamaños.append(i)

                #break
    print(tamaños[0],tamaños[-1])
    if tamaños[0] < 20:
        inicio_y=tamaños[0]
    else:
        inicio_y=tamaños[0] -20
    if tamaños[-1] ==720:
        fin_y=tamaños[-1]
    else:
        fin_y=tamaños[-1]+20

    #......................
    tamaños_x=[]
    for i in range(image.shape[1]):
            if np.sum(image[:,i,:])> 0:
                tamaños_x.append(i)
    print(tamaños_x[0],tamaños_x[-1])
    if tamaños_x[0] < 20:
        inicio_x=tamaños_x[0]
    else:   
        inicio_x=tamaños_x[0]-20
    if tamaños_x[-1] == 1280:
        fin_x=tamaños_x[-1]
    else:    
        fin_x=tamaños_x[-1]+20

    #---------------------
    image_2=image[inicio_y:fin_y,inicio_x:fin_x]

    #----------------------------------------
    if image_2.shape[1] !=0 and image_2.shape[0] !=0:
        print(n,'-',input_img_paths[n])

        if image_2.shape[1] > 350 or image_2.shape[0] > 350:
            for tamaño in lista_tamaños:
                if tamaño> image_2.shape[1] and tamaño> image_2.shape[0]:
                    s=tamaño
                    break
                else:
                    continue             
        else: 
            s=350

        s2=s//2
        size=(s,s)

        Lienzo = np.zeros((s,s,3))

        y= image_2.shape[0]//2
        x= image_2.shape[1]//2

        if image_2.shape[0]%2 !=0 and image_2.shape[1]%2 !=0:
            Lienzo[s2-y:s2+y+1,s2-x:s2+x+1]=image_2[:,:,:]

        elif image_2.shape[0]%2 !=0 :
            Lienzo[s2-y:s2+y+1,s2-x:s2+x]=image_2[:,:,:]

        elif image_2.shape[1]%2 !=0:
            Lienzo[s2-y:s2+y,s2-x:s2+x+1]=image_2[:,:,:]
        else:
            Lienzo[s2-y:s2+y,s2-x:s2+x]=image_2[:,:,:]

        plt.imsave(carpeta_destino + input_img_paths[n][37:], Lienzo,vmin=0,vmax=1)

print('Dataset Transformation and Preprocessing Done')
   