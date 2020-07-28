#Preprocessing
os.mkdir('./dataset')
df=pd.read_csv('metadata.csv') #contains info about the dataset
covid=df[(df['finding']=='COVID-19') & (df['modality']=='X-ray')] 
covid_positive= covid[covid['view']=='PA']
print(covid_positive.shape)



#Obtaining the COVID dataset
path=r"C:\Users\Ambika Sadhu\Desktop\covid chest\images"
dest=r"C:\Users\Ambika Sadhu\Desktop\covid chest\dataset\covid"
if not os.path.exists(dest):
    os.mkdir(dest)
for img in covid_positive.filename:
    if  img not in os.listdir(dest):
        src= os.path.join(path,img)
        shutil.copy(src,dest)


#Obtaining the positive dataset

kaggle_path =r"C:\Users\Ambika Sadhu\Desktop\chest_xray"
dest=r"C:\Users\Ambika Sadhu\Desktop\covid chest\dataset\normal"
if not os.path.exists(dest):
    os.mkdir(dest)
path1=os.path.join(kaggle_path,r"train\NORMAL")
path2= os.path.join(kaggle_path,r"val\NORMAL")
for img in os.listdir(path1):
    src1= os.path.join(path1,img)
    shutil.copy(src1,dest)
for img in os.listdir(path2):
    src2= os.path.join(path2,img)
    shutil.copy(src2,dest)