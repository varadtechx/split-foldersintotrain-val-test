# pip install split-folders

import splitfolders

input_folder = 'path'

#train , val , test
splitfolders.ratio(input_folder , output = "" ,
                   seed=42 , ratio=(0.8,0.1,0.1),
                   group_prefix=None)

splitfolders.fixed(input_folder , output = "",
                    seed=42 ,fixed=( 100,100 ),
                    oversample=False , group_prefix=None)