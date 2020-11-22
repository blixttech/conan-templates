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

Refer [azure-pipelines-template.yml](azure-pipelines-template.yml) file for more parameters.

As user-defined variables are injected as environmental variables, following variables may be specified in a variable group in the "Library".
  * CONAN_LOGIN_USERNAME
  * CONAN_PASSWORD
  * CONAN_REMOTES
  * CONAN_UPLOAD

Followings can be set empty if user/channel information is not needed i.e. when the package is used as ``mypackage/x.y.z``
  * CONAN_USERNAME
  * CONAN_CHANNEL