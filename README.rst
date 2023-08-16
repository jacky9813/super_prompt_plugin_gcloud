######################################
Super Prompt - Google Cloud SDK Plugin
######################################

.. _Super Prompt: https://github.com/jacky9813/super_prompt

A plugin for `Super Prompt`_ that indicates the id of the selected project in current gcloud context, just like
what the prompt is in Cloud Shell of Google Cloud.


System Requirements
===================

.. _Google Cloud SDK: https://cloud.google.com/sdk/docs/install

- Python 3.7+
- `Super Prompt`_
- `Google Cloud SDK`_


Install
=======

Super Prompt - Google Cloud SDK Plugin has not been published to PyPI yet.

Thus, you can install from this Git repo:

.. code-block:: shell

    pip3 install git+https://github.com/jacky9813/super_prompt_plugin_gcloud
    super-prompt config enable-plugin gcloud


Configuration
=============

+--------------------------------+---------------+--------------------------------------------------------------------+
| Option Name                    | Default Value | Description                                                        |
+================================+===============+====================================================================+
| plugins.gcloud.adc_notice_time | PT8H          | An duration in ISO8601 format that, if the application default     |
|                                |               | credentials (ADC) has not been updated for the period, the G       |
|                                |               | will trun red to notice the user.                                  |
|                                |               |                                                                    |
|                                |               | User can use ``gcloud auth login --update-adc`` to update the ADC. |
+--------------------------------+---------------+--------------------------------------------------------------------+
