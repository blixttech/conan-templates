# CI/CI templates

This directory contains configuration templates for various CI/CD systems.

## Azure Pipelines

To use Azure Pipelines template, project's ``azure-pipelines.yml`` file has to be extend as follows.

```yml
resources:
  repositories:
    - repository: templates
      type: github
      name: blixttech/conan-templates
      ref: main
      # Following is the name of the service connection used to
      # checkout the template repository.
      endpoint: conan-packages

extends:
  template: ci/azure-pipelines-template.yml@templates
  parameters:
    conanArchs: "x86_64"
    conanBuildTypes: "Release"
    # Put other parameters here. 
```

Refer ``azure-pipelines-template.yml`` file for more parameters.

As user-defined variables are injected as environmental variables, sensitive information such as 
``CONAN_LOGIN_USERNAME`` and ``CONAN_PASSWORD`` can be set in a variable group using the Library in the UI. 