import copy
import requests
import json
import base64
import os
from deepface import DeepFace
from model_configs import model_configs
import time

class StableSwarmAPI:
    def __init__(self, api_url, base_folder):
        self.api_url = api_url
        self.base_folder = base_folder
        self.session_id = self.get_session_id()
        self.deepface = DeepFace
        self.last_gender = ""
        self.last_age = -1

    def get_deepface(self, img_path):
        #obj = self.deepface.analyze(img_path, actions=['age', 'gender', 'race', 'emotion'])
        obj = self.deepface.analyze(img_path, actions=['age', 'gender'])
        #obj = DeepFace.analyze(img_path, actions=['gender'])
        print("deepface:", obj)
        return obj[0]

    def get_gender_string(self, df):
        gender = ""
        if df['gender']['Man'] > 80.0:
            gender = "Man"
        elif df['gender']['Woman'] > 80.0:
            gender = "Woman"
        self.last_gender = gender
        return gender

    def get_age_string(self, df):
        result = ""
        if 'age' in df:
            result = f"{df['age']} years old"
            self.last_age = df['age']
        return result

    def get_add_info(self, img_path):
        self.last_gender = ""
        self.last_age = -1
        try:
            df = self.get_deepface(img_path)
            prompt = ""
            gender = self.get_gender_string(df)
            if gender != "":
                print(f"is {gender}")
                prompt = gender + ", "

            age = self.get_age_string(df)
            if age != "":
                print(age)
                #prompt = prompt + age + ", "

            return prompt
        except ValueError:
            return ""


    def get_session_id(self):
        resource = "/API/GetNewSession"
        headers = {
            "Content-Type": "application/json"
        }

        payload = {}

        url = self.api_url + resource

        response = requests.post(url, headers=headers, json=payload)
        print(response.text)

        if response.status_code != 200:
            print("Error! " + response.text)
            return ""

        data = json.loads(response.text)
        return data["session_id"]


    def generate_image(self, config_idx, image_filename):
        start_time = time.time()
        resource = "/API/GenerateText2Image"
        url = self.api_url + resource
        headers = {
            "Content-Type": "application/json"
        }

        image_input = self.img_to_base64(image_filename)

        # Define the payload with the parameters for image generation
        payload = copy.copy(model_configs[config_idx])
        payload["session_id"] = self.session_id
        payload["prompt"] = self.get_add_info(image_filename) + payload["prompt"]
        payload["controlnetimageinput"] = image_input
        payload["initimage"] = image_input

        #print(payload)
        response = requests.post(url, headers=headers, json=payload)
        print(response.text)  # Print the error message from the API

        if response.status_code == 200:
            # Extract image data from the response
            image_data = response.json()["images"]  # Assuming the response returns a base64-encoded image
            image_filename = image_data[0].replace("View/", "Output/")
            image_filename = os.path.join(self.base_folder, image_filename)
            #print(image_filename)
            # Decode the base64-encoded image and save it as a file
            #image_bytes = base64.b64decode(image_data)

            #with open("swarm_generated_image.png", "wb") as img_file:
            #    img_file.write(image_bytes)

            #print("Image generated successfully and saved as swarm_generated_image.png")
            elapsed_time = time.time() - start_time
            print(f"Total generation time: {elapsed_time} seconds")
            return image_filename
        else:
            print(f"Failed to generate image. Status code: {response.status_code}")


    def img_to_base64(self, image_filename):
        encoded_string = ""
        with open(image_filename, "rb") as img:
            encoded_string = base64.b64encode(img.read()).decode('utf-8')
        return encoded_string
