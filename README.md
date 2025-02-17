[![PyPI version](https://badge.fury.io/py/onediff.svg)](https://badge.fury.io/py/onediff)
[![Docker image build](https://github.com/Oneflow-Inc/onediff/actions/workflows/sd.yml/badge.svg)](https://github.com/Oneflow-Inc/onediff/actions/workflows/sd.yml)
[![Run examples](https://github.com/Oneflow-Inc/onediff/actions/workflows/examples.yml/badge.svg?event=schedule)](https://github.com/Oneflow-Inc/onediff/actions/workflows/examples.yml?query=event%3Aschedule)

# OneDiff

**An out-of-the-box acceleration library for diffusion models**  (especially for ComfyUI, HF diffusers, and Stable Diffusion web UI).

## State-of-the-art performance

Updated on Nov 6, 2023.

|     Device     | SD1.5 (512x512) | SD2.1 (512x512) | SDXL1.0-base（1024x1024） |
| -------------- | --------------- | --------------- | ------------------------- |
| RTX 3090       | 42.38it/s       | 42.33it/s       | 6.66it/s                  |
| RTX 4090       | 74.71it/s       | 73.57it/s       | 13.57it/s                 |
| A100-PCIE-40GB | 54.4it/s        | 54.06it/s       | 10.22it/s                 |
| A100-SXM4-80GB | 59.68it/s       | 61.91it/s       | 11.80it/s                 |

> **_NOTE:_** OneDiff Enterprise Edition delivers even higher performance and second-to-none deployment flexibility.

## Easy to use
- Acceleration for popular UIs/libs
  - [ComfyUI](https://github.com/Oneflow-Inc/onediff/tree/main/onediff_comfy_nodes)
  - [HF diffusers 🤗](https://github.com/Oneflow-Inc/onediff/tree/main/examples)
  - [Stable Diffusion web UI](https://github.com/Oneflow-Inc/onediff/tree/main/onediff_sd_webui_extensions)
- Acceleration for state-of-the-art Models
  - [SDXL](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_sdxl.py)
  - [SDXL Turbo](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_sdxl_turbo.py)
  - [SD 1.5/2.1](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image.py)
  - [LoRA (and dynamic switching LoRA)](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_sdxl_lora.py)
  - [ControlNet](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_controlnet.py)
  - [LCM](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_lcm.py) and [LCM LoRA](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_lcm_lora_sdxl.py)
  - [Stable Video Diffusion](https://github.com/Oneflow-Inc/onediff/blob/8a35a9e7df45bbfa5bb05011b8357480acb5836e/onediff_comfy_nodes/_nodes.py#L169)
  - [DeepCache](https://github.com/Oneflow-Inc/onediff/blob/8a35a9e7df45bbfa5bb05011b8357480acb5836e/onediff_comfy_nodes/_nodes.py#L414)
- Out-of-the-box acceleration
  - [ComfyUI Nodes](https://github.com/Oneflow-Inc/onediff/tree/main/onediff_comfy_nodes)
  - [Acceleration with oneflow_compile](https://github.com/Oneflow-Inc/onediff/blob/a38c5ea475c07b4527981ec5723ccac083ed0a9c/examples/text_to_image_sdxl.py#L53)
- Multi-resolution input
- Compile and save the compiled result offline, then load it online for serving
  - [Save and Load](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_sdxl_save_load.py)
  - [Change device to do multi-process serving](https://github.com/Oneflow-Inc/onediff/blob/main/examples/text_to_image_sdxl_mp_load.py)

## Need help or talk
- [Discord of OneDiff](https://discord.gg/RKJTjZMcPQ)
- GitHub issues

## Business inquiry on OneDiff Enterprise Edition

If you need **unrestricted multiple resolutions**, **quantization**, **dynamic batch size** support or any other more advanced features, please send an email to business@siliconflow.com . Tell us about your **use case, deployment scale, and requirements**.

|                      | OneDiff Community   | OneDiff Enterprise|
| -------------------- | ------------------- | ----------- |
| diffusers            | Yes                 | Yes         |
| UNet/VAE/ControlNet Compilation | Yes      | Yes         |
| LoRA                 | Limited             | Yes         |
| LCM                  | Limited             | Yes         |
| Multiple Resolutions | Limited             | Yes         |
| ComfyUI              | Community           | Yes         |
| Stable Diffusion web UI | Community           | Yes         |
| Technical Support    | Community           | Yes         |
| Quantization         |                     | Yes         |
| Source Code Access   |                     | Yes         |

## Install from source or Using in Docker
> **_NOTE:_** We only support Linux and NVIDIA GPUs for the moment. If you want to use OneDiff on Windows, please use it under WSL.
### Install from source

1. Install OneFlow(For CUDA 11.8)
```
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/community/cu118
```
<details>
<summary> Click to get OneFlow packages for other CUDA versioins. </summary>
CUDA 12.1

```bash
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/community/cu121
```

CUDA 12.2

```bash
python3 -m pip install --pre oneflow -f https://oneflow-pro.oss-cn-beijing.aliyuncs.com/branch/community/cu122
```

</details>


2. Install torch and diffusers
```
python3 -m pip install "torch" "transformers==4.27.1" "diffusers[torch]==0.19.3"
```

3. Install OneDiff
```
git clone https://github.com/Oneflow-Inc/onediff.git
cd onediff && python3 -m pip install -e .
```

4. (Optional)Login huggingface-cli

```
python3 -m pip install huggingface_hub
 ~/.local/bin/huggingface-cli login
```

### Docker
```bash
docker pull oneflowinc/onediff:20231106
```
