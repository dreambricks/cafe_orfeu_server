import os
import zipfile
import io


def create_zip_of_images(folder_path):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:

        for root, dirs, files in os.walk(folder_path):
            for file in files:

                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    zip_buffer.seek(0)

    return zip_buffer
