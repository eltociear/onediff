# OneFlow diffusers

OneFlow backend support for diffusers

## Getting started

Please refer to this [wiki](https://github.com/Oneflow-Inc/diffusers/wiki/How-to-Run-OneFlow-Stable-Diffusion)

## More about OneFlow

OneFlow's main [repo](https://github.com/Oneflow-Inc/oneflow)

## Development

### Setup

- (optional) If you were using the the oneflow fork of diffusers before

  1. uninstall transformers and diffusers

  ```
  python3 -m pip uninstall tranformers -y
  python3 -m pip uninstall diffusers -y
  ```

  2. install transformers and diffusers

  ```
  python3 -m pip install "transformers>=4.26"
  python3 -m pip install "diffusers[torch]"
  python3 -m pip uninstall accelerate -y
  ```

  3. delete the main first:

  ```
  git branch -D main
  git fetch
  ```

- clone and dev install

```
git clone https://github.com/Oneflow-Inc/diffusers.git onediff
cd onediff
python3 -m pip install -e .
```

## Run demo

```
python3 -m onediff.demo
```

## More examples

There is a directory for [examples](/examples/)

## Release

- run examples to check it works

  ```bash
  python3 examples/text_to_image.py
  python3 examples/text_to_image_dpmsolver.py
  ```

- bump version in [this file](src/onediff/__init__.py)
- build wheel

  ```
  python3 setup.py bdist_wheel
  ```

- upload to pypi

  ```bash
  twine upload dist/*
  ```
