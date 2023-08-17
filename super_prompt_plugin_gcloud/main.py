import os
import logging
import typing
import configparser
import datetime

import isodate

import super_prompt.types

logger = logging.getLogger("gcloud_plugin")

ACTIVE_CONFIG_FILE = os.path.expanduser("~/.config/gcloud/active_config")
CONFIG_LOCATION_TEMPLATE = os.path.expanduser("~/.config/gcloud/configurations/config_{}")
ADC_CREDENTIAL_FILE = os.path.expanduser("~/.config/gcloud/application_default_credentials.json")

COLOR_ADC_INVALID = 31


import sys
def _raise(exc):
    raise exc

def available_configurations() -> typing.Iterable[super_prompt.types.ConfigHint]:
    return [
        super_prompt.types.ConfigHint(
            "adc_notice_time",
            "An ISO8601 duration that, if application default credentials (ADC) age is longer than the value, the G will turn red.",
            "PT8H",
            str
        )
    ]


def main(config: dict) -> typing.Optional[super_prompt.types.PluginResponse]:
    if not os.path.exists(ACTIVE_CONFIG_FILE):
        logger.info("Path %s does not exist", ACTIVE_CONFIG_FILE)
        return

    with open(ACTIVE_CONFIG_FILE) as active_config_fd:
        active_config = active_config_fd.read().strip()

    logger.info("Active config is %s", active_config)

    if not os.path.exists(CONFIG_LOCATION_TEMPLATE.format(active_config)):
        logger.info("Path %s does not exist", os.path.exists(CONFIG_LOCATION_TEMPLATE.format(active_config)))
        return

    gcloud_config = configparser.ConfigParser()
    gcloud_config.read(CONFIG_LOCATION_TEMPLATE.format(active_config))
    current_project = gcloud_config.get("core", "project", fallback=None)

    if current_project is None:
        return

    if not os.path.exists(ADC_CREDENTIAL_FILE):
        return super_prompt.types.PluginResponse("G", current_project, COLOR_ADC_INVALID)
    adc_too_old = isodate.parse_duration(config.get("adc_notice_time", "PT8H"))
    adc_age = datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(os.stat(ADC_CREDENTIAL_FILE).st_mtime)
    return super_prompt.types.PluginResponse("G", current_project, COLOR_ADC_INVALID if adc_age > adc_too_old else None)


if __name__ == "__main__":
    print(main({}))
