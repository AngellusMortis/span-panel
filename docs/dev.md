---
hide:
- navigation
---
# Development

## Setup

### With VS Code

Development with this project is designed to be done via VS Code + Docker. It is a pretty standard Python package, so feel free to use anything else, but all documentation assumes you are using VS Code.

* [VS Code](https://code.visualstudio.com/) + [Remote Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Docker](https://docs.docker.com/get-docker/)
    * If you are using Linux, you need Docker Engine 19.0 or newer and you need to enable [Docker Buildkit](https://docs.docker.com/develop/develop-images/build_enhancements/)
    * If you are using Docker Desktop on MacOS or Windows, you will need Docker Desktop 3.2.0 or newer

Once you have all three setup,

1. Clone repo
2. Open the main folder
3. You should be prompted to "Reopen folder to develop in a container". If you are not, you can open the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) run the "Remote-Containers: Reopen in Container" command.

This should be all you need to do to get a working development environment. The docker container will automatically be build and VS Code will attach itself to it. The integrated terminal in VS Code will already be set up with the `span-panel` command.

### Docker (without VS Code)

You can still setup develop without VS Code, but it is still recommended to use the development container to ensure you have all of the required dependencies. As a result, the above requirement for Docker is still needed.

Once you have Docker setup,

1. Clone repo
2. Build and open dev container

   ```bash
   docker buildx build -f Dockerfile --target=dev -t span-panel-dev .
   docker run --rm -it -v /home/cbailey/dev/span-panel:/workspaces/span-panel span-panel-dev bash
   ```

## Authenticating with SPAN Panel Automatically

The project allows you to create an environment file to put your local protect instance data into so you do not need to constantly enter in or accidentally commit it to the Git repo.

Make a file in the root of the project named `.env` with the following and change accordingly:

```
SPAN_HOST=http://your_span_ip
SPAN_TOKEN=your_token
```

## Linting and Testing

The following scripts exist to easily format, lint and test code in the same fashion as CI:

```
.bin/format-code
.bin/lint-code
.bin/test-code
```

These commands are also all available as [VS Code tasks](https://code.visualstudio.com/Docs/editor/tasks) as well. Tests are also fully integration with the Testing panel in VS Code and can be easily debug from there.

## Updating Requirements

To generate an updated pinned requirements file to be used for testing and CI using the `.bin/update-requirements` script.

There is also a [VS Code task](https://code.visualstudio.com/Docs/editor/tasks) to run this as well.
