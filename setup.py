import os
import re

from setuptools import find_packages, setup

def get_version():
    with open(os.path.join("src", "llmtuner", "__init__.py"), "r", encoding="utf-8") as f:
        file_content = f.read()
        pattern = r"{0}\W*=\W*\"([^\"]+)\"".format("__version__")
        (version,) = re.findall(pattern, file_content)
        return version

def get_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines


extra_require = {
    "metrics": ["nltk", "jieba", "rouge-chinese"],
    "deepspeed": ["deepspeed>=0.10.0"],
    "bitsandbytes": ["bitsandbytes>=0.39.0"],
    "vllm": ["vllm>=0.4.0"],
    "galore": ["galore-torch"],
    "badam": ["badam"],
    "gptq": ["optimum>=1.16.0", "auto-gptq>=0.5.0"],
    "awq": ["autoawq"],
    "aqlm": ["aqlm[gpu]>=1.1.0"],
    "qwen": ["tiktoken", "transformers_stream_generator"],
    "modelscope": ["modelscope"],
    "quality": ["ruff"],
}


def main():
    setup(
        name="llmtuner",
        version=get_version(),
        description="Easy-to-use LLM fine-tuning framework",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        keywords=["LLaMA", "BLOOM", "Falcon", "LLM", "ChatGPT", "transformer", "pytorch", "deep learning"],
        license="Apache 2.0 License",
        package_dir={"": "src"},
        packages=find_packages("src"),
        python_requires=">=3.8.0",
        install_requires=get_requires(),
        extras_require=extra_require,
        entry_points={"console_scripts": ["sft-cli = llmtuner.cli:main"]},
    )


if __name__ == "__main__":
    main()
