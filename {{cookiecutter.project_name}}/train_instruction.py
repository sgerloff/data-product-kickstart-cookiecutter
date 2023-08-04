import logging
import hydra
import omegaconf
import re
import mlflow
import sys


def _clean_tags(tag: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._\-/ ]", "", tag)


def _process_command_line_arguments():
    """
    Infers and processes the commandline arguments passed to the script.
    Each commandline argument passed to hydra is decomposed into key and
    value and return as a map.

    :return: dictionary mapping from instruction key to overriden value
    """
    argument_map = dict(instruction="default_instruction.yaml")
    for arg in sys.argv:
        _arg_split = arg.split("=")
        if not len(_arg_split) == 2:
            continue
        if _arg_split[0] == "--config-name":
            _arg_split[0] = "instruction"

        argument_map[_clean_tags(_arg_split[0])] = _arg_split[1].strip()
    return argument_map


def setup_mlflow(params: omegaconf.DictConfig):
    mlflow.set_tracking_uri(params.mlflow_logger.tracking_uri)
    mlflow.set_experiment(params.mlflow_logger.experiment)


def log_run(params: omegaconf.DictConfig):
    override_instruction_arguments = _process_command_line_arguments()
    mlflow.set_tags(override_instruction_arguments)
    mlflow.log_dict(
        omegaconf.OmegaConf.to_container(params),
        "instruction.yaml"
    )


@hydra.main(version_base=None,
            config_path="instruction",
            config_name="default_instruction.yaml")
def main(params: omegaconf.DictConfig):
    logging.basicConfig(level=logging.INFO)
    setup_mlflow(params)
    with mlflow.start_run(run_name=params.mlflow_logger.run_name) as _:
        log_run(params)
        # Training can start ...
        pass


if __name__ == "__main__":
    main()
