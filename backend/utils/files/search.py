def files_in_directory(directory): 
    index={}
    for (dirname,dirs,files) in os.walk(directory):
        for filename in files:
            #if (filename.endswith(".JPG")):
            fullpath=join(dirname,filename)
            index[fullpath]=features(fullpath)

    return index