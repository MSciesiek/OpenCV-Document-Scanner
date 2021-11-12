# Document Scanner and annotator

Forked from https://github.com/andrewdcampbell/doc_scanner

### Usage
```
python scan.py (--images <IMG_DIR> | --image <IMG_PATH>) --save_dir <SAVE_DIR> [-i]
```
* The `-i` flag enables interactive mode, where you will be prompted to click and drag the corners of the document. For example, to scan a single image with interactive mode enabled:
```
python scan.py --image sample_images/desk.JPG --save_dir <SAVE_DIR> -i
```
* Alternatively, to scan all images in a directory without any input:
```
python scan.py --images sample_images
```
You can ommit the `--save_dir` parameter to save the output into a default 'output' directory of the repository.

You can continue from the last image that you were processing by using a `-skip_processed` flag.