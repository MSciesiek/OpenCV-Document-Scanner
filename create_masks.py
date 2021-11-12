import os
import cv2
import numpy as np
import argparse
from io import StringIO


def create_masks(im_dir, coor_dir, mask_dir, mask_suffix):
    coor_files_list = [f for f in os.listdir(coor_dir) if f.split('.')[-1] == 'txt']
    for coor_path in coor_files_list:
        base_name = coor_path.split('.')[0][:-len('_corners')]
        coor_path = os.path.join(coor_dir, coor_path)
        im_path = os.path.join(im_dir, base_name + '.jpg')
        save_path = os.path.join(mask_dir, base_name + f'{mask_suffix}.jpg')
        create_mask(im_path, coor_path, save_path)


def create_mask(im_path, coor_path ,save_path):
    im = cv2.imread(im_path)
    height, width = im.shape[:2]
    mask = np.zeros((height, width), np.uint8)
    with open(coor_path, 'r') as f:
        coor_str = f.read()
    coor = coor_str.replace(',', '\n').replace('[', '').replace(']', '')
    contours = np.loadtxt(StringIO(coor))

    cv2.fillPoly(mask, pts=np.int32([contours]), color=[255, 255, 255])
    cv2.imwrite(save_path, mask)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", help="Directory of images to be scanned")
    ap.add_argument("--save_dir", help="Path to folder where processed files are already saved", default='output')
    ap.add_argument("--mask_dir", help="Path to folder where masks will be saved", default='')
    ap.add_argument("--mask_suffix", help="Suffix for the mask files", default='_mask')

    args = vars(ap.parse_args())
    im_dir = args["images"]
    coor_dir = args['save_dir']
    mask_dir = args['mask_dir'] or coor_dir
    mask_suffix = args['mask_suffix']

    create_masks(im_dir, coor_dir, mask_dir, mask_suffix)
