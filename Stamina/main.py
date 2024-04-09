import zipfile
import numpy as np
import os

def read_zip_file(zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            file_names = zip_ref.namelist()  # Get list of file names in the zip file
            file_data = {}
            for file_name in file_names:
                with zip_ref.open(file_name, 'r') as file:
                    file_data[file_name] = file.read()  # Read binary data from the file
        return file_data
    except FileNotFoundError:
        print(f"Error: File '{zip_file_path}' not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def binary_to_integers(binary_data):
    integers = []
    for byte in binary_data:
        integer_value = byte  # No conversion needed for bytes
        integers.append(integer_value)
    return integers

def reshape_to_2d(pixel_array, width):
    height = len(pixel_array) // width
    # Ensure that the length of pixel_array is divisible by width
    if len(pixel_array) % width != 0:
        raise ValueError("Length of pixel_array is not divisible by width")
    reshaped_pixel = np.array(pixel_array).reshape((height, width))
    return reshaped_pixel

# Example usage:
zip_file_path = 'ngrok.zip'  # Example zip file path
file_data = read_zip_file(zip_file_path)
size_byte = os.path.getsize(zip_file_path)
integers = binary_to_integers(file_data)
print(size_byte)
if file_data:
    for file_name, binary_data in file_data.items():
        pixel_array = binary_to_integers(binary_data)
        d_reshape = reshape_to_2d(pixel_array, 2)
        print(d_reshape)





