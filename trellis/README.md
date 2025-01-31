## Trellis install and run

in conda on windows 10 ，according to [this post](https://https://github.com/microsoft/TRELLIS/issues/3#issuecomment-2524713914) on github ，when proocessed till installing diffoctreerast :
`$pip install ./tmp/extensions/diffoctreerast`

encounter  cuda version error : The detected CUDA version (11.7) mismatches the version that was used to compile
PyTorch (12.4). Please make sure to use the same CUDA versions.

check CUDA version in conda :

`$nvcc --version`

it shows current version used in conda is 11.7

![](assets/20250130_145422_image.png)

install CUDA 12.4 in conda :

`$pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`

then re-install diffoctreerast , still failed. We found in conda env :

`$nvcc --version`

still 11.07 , so this not work in conda. conda still find CUDA path&version in windows system variables.

So , we need to install a CUDA of version 12.4 on windows system not in conda , downalod from nvidia website & install it,
after installation , in windows system path will be changed to 12.4 .

![](assets/20250131_080831_image.png)

now , **close and re-open terminal(make the variable&path change valid)** ， enter conda env again

`$conda activate trellis`

then check nvcc version again

`$nvcc --version `

now, it's version 12.4

![](assets/20250131_081201_image.png)

then , continue trellis installation again :

`$pip install ./tmp/extensions/diffoctreerast`

![alt text](image.png)

then , in this step
`$cp -r ./extensions/vox2seq ./tmp/extensions/vox2seq`

should be fixed as **use explorer to copy entire vox2seq folder to ./tmp/extensions/**
(since we are in conda on windows system) ，then install it

`$pip install ./tmp/extensions/vox2seq`

After successfully insatlled , start trellis web interface and test , encounter error below :

**RuntimeError: FlashAttention only supports Ampere GPUs or newer**

change attn_flash to xformer :
$set ATTN_BACKEND=xformers

then re-launch trellis to test ， 