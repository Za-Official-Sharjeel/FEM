## Facial Expressions/Attributes Manipulation (FEM) via Stylegan2-ada-pytorch

It is in the works so be patient! I will upload the whole implementation soon.


So far the setup is something like this:
#### `SETUP`
Download the official CelebA-img_align dataset from their official website and preprocess it usnig the code given in PreprocessingDataset/pre_process.ipynb
<!-- COMMENT -->
  `Note: Go to stylegan2-ada-pytorch to setup your environment according to that`<br>
  ```
  git clone https://github.com/NVlabs/stylegan2-ada-pytorch.git
  cd stylegan2-ada-pytorch
  
  pip install dlib torch torchvision torchaudio opencv-python Pillow dlib face-alignment skimage
  ```
