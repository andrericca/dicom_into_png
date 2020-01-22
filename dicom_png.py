import pydicom
import os
import matplotlib.pyplot as plt

# Path where dicom files are stored
LOCAL_DICOMS = "/Users/dicom"
# Path where .png will be created and stored
LOCAL_PNG = "/hdd/teste"

for file_name in os.listdir(LOCAL_DICOMS):
    if file_name.endswith(".dcm"):
        filename, file_extension = os.path.splitext(file_name)
        dicom_meta = pydicom.dcmread(LOCAL_DICOMS+ "/" + file_name, force=True)
        image_dcim = dicom_meta.pixel_array
        im_path = os.path.join(LOCAL_PNG, filename + ".png")
        if dicom_meta.data_element("PhotometricInterpretation").value == "MONOCHROME1":
            plt.imsave(im_path, image_dcim, cmap="gray_r")
        elif dicom_meta.data_element("PhotometricInterpretation").value == "MONOCHROME2":
            plt.imsave(im_path, image_dcim, cmap="gray")
        with open('convert.txt', 'a') as the_file:
            the_file.write(im_path + '\n')
    else:
        continue
