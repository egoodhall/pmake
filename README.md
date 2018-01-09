# pmake
#### A make-inspired build script written in python.
- `Directives`: A directive in `pmake` is a set of tasks that should be run.
- `Groups`: A group is a set of directives that can be run simultaneously

## Example build file
```json
{
    "log_dir": "log/build",
    "groups": [
        [
            {"tag": "frontend", "directive": "frontend"},
            {"tag": "backend", "directive": "backend"}
        ],
        [
            {"tag": "dockerize", "directive": "dockerize"}
        ]
    ],
  "directives": {
      "backend":{
          "require": {
              "build_tool": {"opt": ["mvn"], "err": "Maven is not installed"}
          },
          "run": [
              {"cmd": "{build_tool} package", "msg": "Packaging Java files"}
          ],
          "path": "backend",
          "log_file": "log/build/backend.log"
      },
      "dockerize": {
          "require": {
              "docker_compose": {"opt": ["docker-compose"], "err": "docker-compose is not installed"},
              "docker": {"opt": ["docker-compose"], "err": "docker-compose is not installed"}
          },
          "run": [
              {"cmd": "{docker_compose} down", "msg": "Removing existing containers"},
              {"cmd": "{docker_compose} build", "msg": "Building new images"},
              {"cmd": "{docker_compose} up --no-start", "msg": "Creating containers with new images"},
              {"cmd": "{docker} image prune", "msg": "Pruning old images"}
          ],
          "log_file": "log/build/dockerize.log"
      },
      "frontend": {
          "require": {
              "build_tool": {"opt": ["yarn", "npm"], "err": "Neither Yarn nor NPM is installed"}
          },
          "run": [
              {"cmd": "{build_tool} build", "msg": "Compiling static JS files"}
          ],
          "path": "frontend",
          "log_file": "log/build/frontend.log"
      }
  }
}
```
