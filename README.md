# Uumpa CI Toolbox

A set of tools (AKA toolbox) for running continuous integration workflows.

## Goals

* Python as the primary language
* Minimal vendor lock

## Reference

<!-- start reference -->

### uci

```
Usage: uci [OPTIONS] COMMAND [ARGS]...

  Uumpa CI Toolbox

Options:
  --help  Show this message and exit.

Commands:
  docker
  docs
  git
  github
  helm
  kubectl
  minikube
  ssh
  util      Misc.
  version   Print the Uumpa CI Toolbox version
  webmon
  yaml
```

#### uci git

```
Usage: uci git [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  check-last-commit-message  Check the last commit message for specified...
  checkout                   Checkout a Git repository and optionally...
  get-branch-name            Get the branch name from a Git ref
  get-last-commit-message    Get the last commit message
  get-tag-name               Get the tag name from a Git ref
```

#### uci git checkout

```
Usage: uci git checkout [OPTIONS]

  Checkout a Git repository and optionally make it available for editing

Options:
  --github-repo-name TEXT   in the format of owner/repo (e.g. "OriHoch/uumpa-
                            ci-toolbox")  [required]
  --branch-name TEXT        [required]
  --github-token TEXT       GitHub personal access token to authenticate for
                            write access
  --fetch-depth INTEGER     How many commits to fetch
  --ssh-key TEXT            content of private ssh key which can be used for
                            write access to the repo
  --ssh-key-file TEXT       path to private ssh key which can be used for
                            write access to the repo
  --path TEXT               target path for the checkout  [required]
  --config-user-name TEXT   configure the user name used when making commits
                            from the repo
  --config-user-email TEXT  configure the user email used when making commits,
                            if user-name is provided it will default to "user-
                            name@localhost"
  --help                    Show this message and exit.
```

#### uci git get-tag-name

```
Usage: uci git get-tag-name [OPTIONS]

  Get the tag name from a Git ref

Options:
  --ref TEXT  Git ref (e.g. "refs/tags/v1.2.3" will return "v1.2.3")
              [required]
  --help      Show this message and exit.
```

#### uci git get-branch-name

```
Usage: uci git get-branch-name [OPTIONS]

  Get the branch name from a Git ref

Options:
  --ref TEXT  Git ref (e.g. "refs/heads/main" will return "main")  [required]
  --help      Show this message and exit.
```

#### uci git get-last-commit-message

```
Usage: uci git get-last-commit-message [OPTIONS]

  Get the last commit message

Options:
  --help  Show this message and exit.
```

#### uci git check-last-commit-message

```
Usage: uci git check-last-commit-message [OPTIONS]

  Check the last commit message for specified strings

  If any of the options match - it will exit with returncode 0, otherwise it
  will exit with returncode 1

Options:
  --equals TEXT       Commit message equals to this specified string
  --starts-with TEXT  Commit message starts with this specified string
  --contains TEXT     Commit message contains this specified string
  --help              Show this message and exit.
```

#### uci github

```
Usage: uci github [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  actions                         Commands that should be run from...
  add-environment-secret          Add an environment secret to a GitHub...
  create-and-configure-deploy-key
                                  Create and configure a deploy key from...
  create-deploy-key               Add a deploy key to a GitHub repo
```

#### uci github actions

```
Usage: uci github actions [OPTIONS] COMMAND [ARGS]...

  Commands that should be run from GitHub actions scripts.

  All commands depend on GitHub actions environment variables to be set.

  Some commands require GITHUB_TOKEN environment variable which should be set
  in the actions yaml script env as:     GITHUB_TOKEN: ${{
  secrets.GITHUB_TOKEN }}

Options:
  --help  Show this message and exit.

Commands:
  docker-login     Login to ghcr.io allowing to push images to the GitHub...
  get-branch-name  Get the branch name of the currently running action
  get-tag-name     Get the tag name of the currently running action
  self-checkout    Checkout the repository which is currently running...
```

#### uci github actions self-checkout

```
Usage: uci github actions self-checkout [OPTIONS]

  Checkout the repository which is currently running this GitHub actions
  script

Options:
  --fetch-depth INTEGER     How many commits to fetch
  --path TEXT               Path to checkout to, defaults to current directory
  --config-user-name TEXT   User name used to make commits
  --config-user-email TEXT  User email used to make commits, defaults to user-
                            name@localhost
  --help                    Show this message and exit.
```

#### uci github actions get-tag-name

```
Usage: uci github actions get-tag-name [OPTIONS]

  Get the tag name of the currently running action

Options:
  --help  Show this message and exit.
```

#### uci github actions get-branch-name

```
Usage: uci github actions get-branch-name [OPTIONS]

  Get the branch name of the currently running action

Options:
  --help  Show this message and exit.
```

#### uci github actions docker-login

```
Usage: uci github actions docker-login [OPTIONS]

  Login to ghcr.io allowing to push images to the GitHub container registry
  for the current repository

Options:
  --help  Show this message and exit.
```

#### uci github create-deploy-key

```
Usage: uci github create-deploy-key [OPTIONS]

  Add a deploy key to a GitHub repo

  Required GITHUB_TOKEN environment variable to be set with a GitHub personal
  access token

Options:
  --repository TEXT  GitHub repository name (owner/name)  [required]
  --key-title TEXT   Title of the deploy key, will be shown on GitHub deploy
                     keys UI  [required]
  --public-key TEXT  Content of the SSH public key of the deploy key
                     [required]
  --read-only        If true, will set the key as read-only
  --help             Show this message and exit.
```

#### uci github add-environment-secret

```
Usage: uci github add-environment-secret [OPTIONS]

  Add an environment secret to a GitHub repo

  Required GITHUB_TOKEN environment variable to be set with a GitHub personal
  access token

Options:
  --repository TEXT  GitHub repository name (owner/name)  [required]
  --key TEXT         Secret name  [required]
  --value TEXT       Secret value  [required]
  --help             Show this message and exit.
```

#### uci github create-and-configure-deploy-key

```
Usage: uci github create-and-configure-deploy-key [OPTIONS]

  Create and configure a deploy key from one repository to a different
  repository.

  This will allow the repository specified in "--add-environment-secret-
  repository" to make changes in the repository specified in "--create-deploy-
  key-repository" by using git checkout with the ssh key that will be defined
  in the environment secret.

  Required GITHUB_TOKEN environment variable to be set with a GitHub personal
  access token with appropriate permissions to both repositories

Options:
  --create-deploy-key-repository TEXT
                                  Will add the deploy key to this repository
                                  [required]
  --add-environment-secret-repository TEXT
                                  Will add the environment secret to this
                                  repository  [required]
  --deploy-key-title TEXT         Title of the deploy key, displayed on GitHub
                                  UI  [required]
  --environment-secret-name TEXT  Name of the environment secret  [required]
  --help                          Show this message and exit.
```

#### uci docker

```
Usage: uci docker [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  build-cache  Build a Docker image with optional cache-from argument.
  tag-push     Tag and push a Docker image.
```

#### uci docker build-cache

```
Usage: uci docker build-cache [OPTIONS] DOCKER_BUILD_ARGS...

  Build a Docker image with optional cache-from argument.

  It first attempts to pull the cache-from image, if it exists - it uses it as
  cache-from argument, otherwise it builds without cache

Options:
  --cache-from TEXT  Docker image to cache from  [required]
  --help             Show this message and exit.
```

#### uci docker tag-push

```
Usage: uci docker tag-push [OPTIONS]

  Tag and push a Docker image.

  It first tags the SOURCE_TAG_NAME with the PUSH_TAG_NAME, and then pushes
  the PUSH_TAG_NAME

Options:
  --source-tag-name TEXT  [required]
  --push-tag-name TEXT    [required]
  --help                  Show this message and exit.
```

#### uci yaml

```
Usage: uci yaml [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  update  Update a yaml file with the given json.
```

#### uci yaml update

```
Usage: uci yaml update [OPTIONS] PATCH_JSON YAML_FILE

  Update a yaml file with the given json.

  Recursively replaces/adds attributes from the json to the yaml. If a value
  is null - deletes the attribute from the yaml.

Options:
  --help  Show this message and exit.
```

#### uci ssh

```
Usage: uci ssh [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  key-gen  Generate an SSH public/private key pair
```

#### uci ssh key-gen

```
Usage: uci ssh key-gen [OPTIONS]

  Generate an SSH public/private key pair

Options:
  --comment TEXT   Public key comment  [required]
  --filename TEXT  Path to the private key to create, public key will use the
                   same filename with .pub suffix  [required]
  --help           Show this message and exit.
```

#### uci docs

```
Usage: uci docs [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  render-markdown-from-click-cli  Generate markdown documentation from a...
```

#### uci docs render-markdown-from-click-cli

```
Usage: uci docs render-markdown-from-click-cli [OPTIONS]

  Generate markdown documentation from a click cli command.

  Exits with returncode 1 if there is no change in the markdown text and
  returncode 0 if there was a change

Options:
  --python-venv TEXT          path to Python virtualenv which has the relevant
                              click cli
  --cli-command TEXT          the name of the relevant click cli command
                              binary  [required]
  --cli-module TEXT           the main cli module name (e.g.
                              "uumpa_ci_toolbox.cli")  [required]
  --main-command TEXT         the main command within the cli module (e.g.
                              "main")  [required]
  --output-file TEXT          path to the markdown file to update with the
                              rendered documentation  [required]
  --start-line-contains TEXT  comment within the markdown file that marks the
                              start of the documentation  [required]
  --end-line-contains TEXT    comment within the markdown file that marks the
                              end of the documentation  [required]
  --with-timestamp            Include a timestamp in the help markdown
  --help                      Show this message and exit.
```

#### uci helm

```
Usage: uci helm [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  install  Install Helm client in the given version
```

#### uci helm install

```
Usage: uci helm install [OPTIONS]

  Install Helm client in the given version

Options:
  --version TEXT          Helm version to install, e.g. "v3.2.4"  [required]
  --target-filename TEXT
  --with-sudo
  --help                  Show this message and exit.
```

#### uci minikube

```
Usage: uci minikube [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  install  Install Minikube in the given version
```

#### uci minikube install

```
Usage: uci minikube install [OPTIONS]

  Install Minikube in the given version

Options:
  --version TEXT          Minikube version to install, e.g. "v1.21.0"
                          [required]
  --target-filename TEXT
  --with-sudo
  --help                  Show this message and exit.
```

#### uci util

```
Usage: uci util [OPTIONS] COMMAND [ARGS]...

  Misc. utilities and helper commands

Options:
  --help  Show this message and exit.

Commands:
  wait-for  Calls the condition script every second until it exits with...
```

#### uci util wait-for

```
Usage: uci util wait-for [OPTIONS] CONDITION_SCRIPT

  Calls the condition script every second until it exits with returncode 0

Options:
  --timeout-seconds INTEGER  [required]
  --timeout-message TEXT
  --help                     Show this message and exit.
```

#### uci kubectl

```
Usage: uci kubectl [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  install  Install Kubectl in the given version
```

#### uci kubectl install

```
Usage: uci kubectl install [OPTIONS]

  Install Kubectl in the given version

Options:
  --version TEXT          Kubectl version to install, e.g. "v1.19.0"
                          [required]
  --target-filename TEXT
  --with-sudo
  --help                  Show this message and exit.
```

#### uci webmon

```
Usage: uci webmon [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  start        Starts a web service which runs the given python_code on...
  start-multi  Starts multiple webmon services listening on the same port...
```

#### uci webmon start

```
Usage: uci webmon start [OPTIONS] PORT PYTHON_CODE

  Starts a web service which runs the given python_code on each request.

  This is useful for monitoring things, a web monitoring service can be
  connected to it and alert on abstract conditions

  The python_code should define a webmon() function which returns a tuple of
  (boolean, dict)

  All code, including imports should be within the webmon function

  python_code example:

  def webmon():   import random   if random.randint(0,1):     return True,
  {'hello': 'world'}   else:     return False, {'error': 'failed'}

Options:
  --help  Show this message and exit.
```

#### uci webmon start-multi

```
Usage: uci webmon start-multi [OPTIONS] PORT CONFIG_FILE

  Starts multiple webmon services listening on the same port based on a yaml
  config file

  Example config file:

  webmons:   - path: /random     # all code, including imports should be
  within the webmon function     python_code: |       def webmon():
  import random         if random.randint(0,1):           return True,
  {'hello': 'world'}         else:           return False, {'error': 'failed'}
  - path: /test     # all code, including imports should be within the webmon
  function     python_file: /path/to/my_code.py

Options:
  --help  Show this message and exit.
```

#### uci version

```
Usage: uci version [OPTIONS]

  Print the Uumpa CI Toolbox version

Options:
  --help  Show this message and exit.
```
<!-- end reference -->
