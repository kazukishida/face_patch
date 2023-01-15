import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
import face_recognition


def face_patch(file):
  im = Image.open(file)
  kaomoji = Image.open('./kaomoji.png')

  image = np.asarray(im)
  face_bboxes = face_recognition.face_locations(image, model="hog")   # (top, right, bottom, left)

  im1 = ImageDraw.Draw(im)
  for t, r, b, l in face_bboxes:
    im1.rectangle([(l, t), (r, b)], outline=(255, 0, 0), width=10)
    im.paste(kaomoji.resize((r - l, b - t)), (l, t))

  image = np.asarray(im)
  return im


def main(file=None):
  st.title("Face Patch")
  file = st.file_uploader("ファイルアップロード", type='jpg')

  if st.button("変換", key=0):
    if file is not None:
      im = face_patch(file)
      st.image(im, caption='patched', use_column_width=True)
    else:
      st.write('please upload a image.')
  

if __name__ == '__main__':
  main()
