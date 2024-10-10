model_configs = [
# config idx = 0
{
    "session_id": "",
    "images": 1,
    "steps": 15,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "oil on canvas, (modernism:1.0), earthy tones, pastels artwork, portrait, high quality, high resolution, oil painting art style, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, intricate detailing, adds depth and dimension, dynamic compositions, innovative technique, cultural significance",
    "negativeprompt": "reddish tones, closed eyes, low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "juggernautXL_juggXIByRundiffusion",
    "width": 1024,
    "height": 1024,
    "sampler": "dpmpp_sde",
    "refinervae": "vaeFtMse840000EmaPruned_vaeFtMse840k",
    "refinercontrolpercentage": 0.2,
    "refinermethod": "PostApply",
    "refinerupscalemethod": "pixel-lanczos",
    "seed": 440794203,  # Set to None for random seed generation
    "loras": "OIL_ON_CANVAS_v3",
    "loraweights": 1.0,
    "controlnetimageinput": "",
    "controlnetpreprocessor": "CannyEdgePreprocessor",
    "controlnetmodel": "controlnetxlCNXL_saiCanny",
    "controlnetstrength": 0.6,
    "initimage": "",
    "initimagecreativity": 0.4,
    "maskblur": 4,
    "automaticvae": True
},

# config idx = 1
{
    "session_id": "",
    "images": 1,
    "steps": 10,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "portrait, oil on canvas, open eyes, modernism, bright earthy colors, limited color pallete, high quality, high resolution, oil painting art style, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, intricate detailing, adds depth and dimension, innovative technique, cultural significance, pastels artwork, rich colors, vibrant hues, impasto painting art style, thick and textured brushwork, vibrant colors, tactile quality, expressive strokes, bold contrasts, dramatic lighting effects, immersive texture, creates visual interest, cubism art style, fragmented forms, geometric shapes",
    "negativeprompt": "reddish tones, closed eyes, low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "juggernautXL_juggXIByRundiffusion",
    "width": 1024,
    "height": 1024,
    "sampler": "dpmpp_sde",
    "refinervae": "vaeFtMse840000EmaPruned_vaeFtMse840k",
    "refinercontrolpercentage": 0.2,
    "refinermethod": "PostApply",
    "refinerupscalemethod": "pixel-lanczos",
    "seed": 440794203,  # Set to None for random seed generation
    "loras": "OIL_ON_CANVAS_v3",
    "loraweights": 0.9,
    "controlnetimageinput": "",
    "controlnetpreprocessor": "CannyEdgePreprocessor",
    "controlnetmodel": "controlnetxlCNXL_saiCanny",
    "controlnetstrength": 1.5,
    "initimage": "",
    "initimagecreativity": 0.65,
    "maskblur": 4,
    "automaticvae": True
},

# config idx = 2
{
    "session_id": "",
    "images": 1,
    "steps": 10,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "portrait, oil on canvas, open eyes, modernism, bright earthy colors, limited color pallete, high quality, high resolution, oil painting art style, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, intricate detailing, adds depth and dimension, innovative technique, cultural significance, pastels artwork, rich colors, vibrant hues, impasto painting art style, thick and textured brushwork, vibrant colors, tactile quality, expressive strokes, bold contrasts, dramatic lighting effects, immersive texture, creates visual interest, cubism art style, fragmented forms, geometric shapes",
    "negativeprompt": "reddish tones, closed eyes, low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "juggernautXL_juggXIByRundiffusion",
    "width": 1024,
    "height": 1024,
    "sampler": "dpmpp_sde",
    "refinervae": "vaeFtMse840000EmaPruned_vaeFtMse840k",
    "refinercontrolpercentage": 0.2,
    "refinermethod": "PostApply",
    "refinerupscalemethod": "pixel-lanczos",
    "seed": 440794203,  # Set to None for random seed generation
    "loras": "OIL_ON_CANVAS_v3",
    "loraweights": 0.9,
    "controlnetimageinput": "",
    "controlnetpreprocessor": "CannyEdgePreprocessor",
    "controlnetmodel": "controlnetxlCNXL_saiCanny",
    "controlnetstrength": 1,
    "initimage": "",
    "initimagecreativity": 0.7,
    "maskblur": 4,
    "automaticvae": True
},

# config idx = 3
{
    "session_id": "",
    "images": 1,
    "steps": 50,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "oil on canvas, (art by candido portinari:1.0), modernism, cubism, earthy tones, pastels artwork, portrait, high quality, high resolution, oil painting art style, rich colors, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, vibrant hues, intricate detailing, adds depth and dimension, cubism art style, fragmented forms, geometric shapes, dynamic compositions, vibrant colors, innovative technique, cultural significance",
    "negativeprompt": "low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "juggernautXL_juggXIByRundiffusion",
    "width": 1024,
    "height": 1024,
    "sampler": "dpmpp_sde",
    "refinervae": "vaeFtMse840000EmaPruned_vaeFtMse840k",
    "refinercontrolpercentage": 0.2,
    "refinermethod": "PostApply",
    "refinerupscalemethod": "pixel-lanczos",
    "seed": 440794203,  # Set to None for random seed generation
    "loras": "OIL_ON_CANVAS_v3",
    "loraweights": 1,
    "controlnetimageinput": "",
    "controlnetpreprocessor": "CannyEdgePreprocessor",
    "controlnetmodel": "controlnetxlCNXL_saiCanny",
    "controlnetstrength": 0.6,
    "initimage": "",
    "initimagecreativity": 0.6,
    "maskblur": 4,
    "automaticvae": True
},

# config idx = 4
{
    "session_id": "",
    "images": 1,
    "steps": 10,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "oil on canvas, (art by candido portinari:1.0), modernism, cubism, earthy tones, pastels artwork, portrait, high quality, high resolution, oil painting art style, rich colors, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, vibrant hues, intricate detailing, adds depth and dimension, cubism art style, fragmented forms, geometric shapes, dynamic compositions, vibrant colors, innovative technique, cultural significance",
    "negativeprompt": "low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "OfficialStableDiffusion/sd_xl_base_1.0",
    "width": 1024,
    "height": 1024,
    "seed": 440794203,  # Set to None for random seed generation
},

# config idx = 5
{
    "session_id": "",
    "images": 1,
    "steps": 8,  # Number of diffusion steps
    "cfg_scale": 7,  # Classifier-free guidance scale
    "prompt": "oil on canvas, (art by candido portinari:1.0), modernism, cubism, earthy tones, pastels artwork, portrait, high quality, high resolution, oil painting art style, rich colors, lush textures, expressive brushwork, blendable layers, dynamic compositions, professional-grade finish, versatile medium, timeless elegance, immersive depth, vibrant hues, intricate detailing, adds depth and dimension, cubism art style, fragmented forms, geometric shapes, dynamic compositions, vibrant colors, innovative technique, cultural significance",
    "negativeprompt": "low quality, signature, watermark, photo, photorealistic, realism, ugly, off-center, deformed, 35mm film, dslr, cropped, frame, worst quality, low quality, lowres, JPEG artifacts",
    "model": "sd_xl_turbo_1.0",
    "width": 512,
    "height": 512,
    "sampler": "dpmpp_sde",
    #"refinervae": "vaeFtMse840000EmaPruned_vaeFtMse840k",
    #"refinercontrolpercentage": 0.2,
    #"refinermethod": "PostApply",
    #"refinerupscalemethod": "pixel-lanczos",
    "seed": 440794203,  # Set to None for random seed generation
    #"loras": "OIL_ON_CANVAS_v3",
    #"loraweights": 1,
    "controlnetimageinput": "",
    "controlnetpreprocessor": "CannyEdgePreprocessor",
    "controlnetmodel": "controlnetxlCNXL_saiCanny",
    "controlnetstrength": 0.6,
    "initimage": "",
    "initimagecreativity": 0.6,
    "maskblur": 4,
    "automaticvae": True
},

]