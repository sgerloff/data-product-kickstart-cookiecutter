import logging
import hydra
import omegaconf

import {{cookiecutter.module_name}}

from script_utils import parse_overrides



def setup_mlflow_tags(params: omegaconf.DictConfig):
    mlflow_tags = parse_overrides(params.hydra_overrides)
    mlflow_tags["instruction"] = params.instruction_name
    mlflow_tags["version"] = {{cookiecutter.module_name}}.__version__
    return mlflow_tags

@hydra.main(version_base=None,
            config_path="instruction",
            config_name="default_instruction.yaml")
def main(params: omegaconf.DictConfig):
    logging.basicConfig(level=logging.INFO)

    mlflow_tags = setup_mlflow_tags(params)
    # Training can start ...
    pass


if __name__ == "__main__":
    main()
