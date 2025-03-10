DATASET_PATHS = [


	dict(
        real_path='/content/UniversalFakeDetect/CNN/progan',     
        fake_path='/content/UniversalFakeDetect/CNN/progan',
        data_mode='wang2020',
        key='progan'
    ),

    dict(
        real_path='/content/UniversalFakeDetect/CNN/cyclegan',   
        fake_path='/content/UniversalFakeDetect/CNN/cyclegann',
        data_mode='wang2020',
        key='cyclegan'
    ),

    dict(
        real_path='/content/UniversalFakeDetect/CNN/biggan/',   # Imagenet 
        fake_path='/content/UniversalFakeDetect/CNN/biggan/',
        data_mode='wang2020',
        key='biggan'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/stylegan',    
        fake_path='/content/UniversalFakeDetect/CNN/stylegan',
        data_mode='wang2020',
        key='stylegan'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/gaugan/0_real',    # It is COCO 
        fake_path='/content/UniversalFakeDetect/CNN/gaugan/1_fake',
        data_mode='wang2020',
        key='gaugan'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/stargan/0_real',  
        fake_path='/content/UniversalFakeDetect/CNN/stargan/1_fake',
        data_mode='wang2020',
        key='stargan'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/deepfake/0_real',   
        fake_path='/content/UniversalFakeDetect/CNN/deepfake/1_fake',
        data_mode='wang2020',
        key='deepfake'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/seeingdark/0_real',   
        fake_path='/content/UniversalFakeDetect/CNN/seeingdark/1_fake',
        data_mode='wang2020',
        key='sitd'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/san/0_real',   
        fake_path='/content/UniversalFakeDetect/CNN/san/1_fake',
        data_mode='wang2020',
        key='san'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/crn/0_real',   # Images from some video games
        fake_path='/content/UniversalFakeDetect/CNN/crn/1_fake',
        data_mode='wang2020',
        key='crn'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/CNN/imle/0_real',   # Images from some video games
        fake_path='/content/UniversalFakeDetect/CNN/imle/1_fake',
        data_mode='wang2020',
        key='imle'
    ),
    

    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/imagenet',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/guided',
        data_mode='wang2020',
        key='guided'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/ldm_200',
        data_mode='wang2020',
        key='ldm_200'
    ),

    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/imagenet',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/ldm_200_cfg',
        data_mode='wang2020',
        key='ldm_200_cfg'
    ),

    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/ldm_100',
        data_mode='wang2020',
        key='ldm_100'
     ),


    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/glide_100_27',
        data_mode='wang2020',
        key='glide_100_27'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/glide_50_27',
        data_mode='wang2020',
        key='glide_50_27'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/glide_100_10',
        data_mode='wang2020',
        key='glide_100_10'
    ),


    dict(
        real_path='/content/UniversalFakeDetect/diffusion_datasets/laion',
        fake_path='/content/UniversalFakeDetect/diffusion_datasets/dalle',
        data_mode='wang2020',
        key='dalle'
    ),
]
