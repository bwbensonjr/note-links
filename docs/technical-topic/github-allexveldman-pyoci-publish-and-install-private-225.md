---
id: 225
url: https://github.com/AllexVeldman/pyoci
title: 'GitHub - AllexVeldman/pyoci: Publish and install private python packages using
  OCI/docker registries.'
domain: github.com
source_date: '2025-10-03'
tags:
- github-repo
- python
- devops
- cli-tool
summary: PyOCI is a tool that enables publishing and installing private Python packages
  using OCI (Docker) registries like GitHub Container Registry, eliminating the need
  for separate package management services. It acts as a proxy between pip and any
  OCI-compliant registry, allowing users to leverage existing container registry infrastructure
  with its access controls. The project can be used through a public instance at pyoci.com
  or self-hosted via Docker, supporting features like package labeling, authentication,
  and integration with tools like Renovate.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - AllexVeldman/pyoci: Publish and install private python packages using OCI/docker registries.

PyOCI
=====

Publish and download (private) python packages using an OCI registry for storage.

[![Test](https://github.com/AllexVeldman/pyoci/actions/workflows/test.yaml/badge.svg)](https://github.com/AllexVeldman/pyoci/actions/workflows/test.yaml)
[![Examples](https://github.com/AllexVeldman/pyoci/actions/workflows/examples.yaml/badge.svg)](https://github.com/AllexVeldman/pyoci/actions/workflows/examples.yaml)
[![Deploy](https://github.com/AllexVeldman/pyoci/actions/workflows/deploy.yaml/badge.svg)](https://github.com/AllexVeldman/pyoci/actions/workflows/deploy.yaml)
[![Coverage](https://camo.githubusercontent.com/06c0d9715f77c0471f33b883ad0d07a165a800c8c50fffc9c05eaa0bb607bd2b/68747470733a2f2f736f6e6172636c6f75642e696f2f6170692f70726f6a6563745f6261646765732f6d6561737572653f70726f6a6563743d416c6c657856656c646d616e5f70796f6369266d65747269633d636f766572616765)](https://sonarcloud.io/summary/new_code?id=AllexVeldman_pyoci)

Why PyOCI
---------

To not have to rely on `yet-another-cloud-provider` for private Python packages, PyOCI, makes `ghcr.io` act like a python index.  
In addition, this completely removes the need for separate access management as GitHub Packages access control applies.

Most subscriptions with cloud providers include an [OCI](https://opencontainers.org/) (docker image) registry where private containers can be published and distributed from.

PyOCI allows using any (private) OCI registry as a python package index, as long as it implements the [OCI distribution specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md).
It acts as a proxy between pip and the OCI registry.

An instance of PyOCI is available at <https://pyoci.com>, to use this proxy, please see the [Getting started](#getting-started).

Tested registries:

* [ghcr.io](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
* [Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry)

Published packages will show up in the OCI registry UI:

[![ghcr.io hello-world package versions](https://private-user-images.githubusercontent.com/59562474/355042686-c3595da9-91e7-4ee6-b890-2ed9baca3c9d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc4NTcsIm5iZiI6MTc4MDI0NzU1NywicGF0aCI6Ii81OTU2MjQ3NC8zNTUwNDI2ODYtYzM1OTVkYTktOTFlNy00ZWU2LWI4OTAtMmVkOWJhY2EzYzlkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MTIzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTliNGY3YWJkM2RiY2FkZTI3NzQxY2NiMWFkZmRlYmU3NzZkZWFjMGJlNjliOGMxODRhMGYzNzUzNDgyNWM5NWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.68p2KGOzirHkyqN5qXt8noG5gK4njpFC7Zvkscj5Res)](https://private-user-images.githubusercontent.com/59562474/355042686-c3595da9-91e7-4ee6-b890-2ed9baca3c9d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc4NTcsIm5iZiI6MTc4MDI0NzU1NywicGF0aCI6Ii81OTU2MjQ3NC8zNTUwNDI2ODYtYzM1OTVkYTktOTFlNy00ZWU2LWI4OTAtMmVkOWJhY2EzYzlkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MTIzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTliNGY3YWJkM2RiY2FkZTI3NzQxY2NiMWFkZmRlYmU3NzZkZWFjMGJlNjliOGMxODRhMGYzNzUzNDgyNWM5NWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.68p2KGOzirHkyqN5qXt8noG5gK4njpFC7Zvkscj5Res)
[![ghcr.io Distinct distributions will show up as separate architectures for the same versions](https://private-user-images.githubusercontent.com/59562474/355043198-63d130cf-5551-4131-b48b-a6e8f259cbc5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc4NTcsIm5iZiI6MTc4MDI0NzU1NywicGF0aCI6Ii81OTU2MjQ3NC8zNTUwNDMxOTgtNjNkMTMwY2YtNTU1MS00MTMxLWI0OGItYTZlOGYyNTljYmM1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MTIzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJkMTc1NjFlZDY4NWM0ODJiNTY1NjVmOGQ5NzM0ZjdjNGZjOTlkZTU4YmYxMmE0YzA1NDI2NjgwNWYyYzUxNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.Jh-ubjXa-jhI4cYgSS6Ag6bPXQvNiYVil00yayZFurU)](https://private-user-images.githubusercontent.com/59562474/355043198-63d130cf-5551-4131-b48b-a6e8f259cbc5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODAyNDc4NTcsIm5iZiI6MTc4MDI0NzU1NywicGF0aCI6Ii81OTU2MjQ3NC8zNTUwNDMxOTgtNjNkMTMwY2YtNTU1MS00MTMxLWI0OGItYTZlOGYyNTljYmM1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTMxVDE3MTIzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJkMTc1NjFlZDY4NWM0ODJiNTY1NjVmOGQ5NzM0ZjdjNGZjOTlkZTU4YmYxMmE0YzA1NDI2NjgwNWYyYzUxNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.Jh-ubjXa-jhI4cYgSS6Ag6bPXQvNiYVil00yayZFurU)

Getting started
---------------

To install a package with pip using PyOCI:

```
pip install --index-url="http://<username>:<password>@<pyoci-url>/<OCI-registry-url>/<namespace>/" <package-name>
```

* `<pyoci-url>`: <https://pyoci.com>
* `<OCI-registry-url>`: URL of the OCI registry to use.
* `<namespace>`: namespace within the registry, for most registries this is the username or organization name.

Example installing package `hello-world` from organization `allexveldman` using `ghcr.io` as the registry:

```
pip install --index-url="https://$GITHUB_USER:$GITHUB_TOKEN@pyoci.com/ghcr.io/allexveldman/" hello-world
```

Warning

If the package contains dependencies from regular pypi, these will not resolve.

Pip does not have a proper way of indicating you only want to resolve `<package-name>` through PyOCI and it's dependencies through pypi.
Poetry does provide you with [a way](https://python-poetry.org/docs/repositories/#package-source-constraint) to do this.
[As does uv](https://docs.astral.sh/uv/concepts/projects/dependencies/#index).

For more examples, including how to publish a package, see the [examples](/AllexVeldman/pyoci/blob/main/docs/examples).

Host your own
-------------

If you don't want, or can't, use <https://pyoci.com>, you can host your own using the docker container.

`docker run ghcr.io/allexveldman/pyoci:latest`

Note that only HTTP is supported at this moment,
PyOCI is expected to run behind a reverse proxy that handles TLS termination, or a trusted environment.

### Environment variables

* `PORT`: port to listen on, defaults to `8080`.
* `PYOCI_PATH`: Host PyOCI on a subpath, for example: `PYOCI_PATH="/acme-corp"`.
* `PYOCI_MAX_BODY`: Limit the maximum accepted body size in bytes when publishing packages, defaults to 50MB.
* `PYOCI_MAX_VERSIONS`: Limit how many versions (in reverse alphabetical order) to fetch filenames for when listing a package.
  By default PyOCI will only include the last `100` versions.
  To not limit the versions, set this value to `0`.
* `OTLP_ENDPOINT`: If set, forward logs, traces, and metrics to this OTLP collector endpoint every 30s.
* `OTLP_AUTH`: Full Authorization header value to use when sending OTLP requests.
* `RUST_LOG`: Log filter, defaults to `info`.

The following environment variables will be added as attributes to the OTLP resources:

* `DEPLOYMENT_ENVIRONMENT` -> `deployment.environment`

Set by Azure Container App, can change if I every decide to move host:

* `CONTAINER_APP_NAME` -> `k8s.container.name`
* `CONTAINER_APP_REVISION` -> `k8s.pod.name`
* `CONTAINER_APP_REPLICA_NAME` -> `k8s.replicaset.name`

### Health check

PyOCI exposes the `/health` endpoint that returns HTTP 200 if the server is up and processing requests.

Note

This endpoint is always `/health` and does not change with `PYOCI_PATH`.

Add Labels to your package
--------------------------

Labels can be added to your package by including them as a `PyOCI :: Label :: <Key> :: <Value>` [classifier](https://packaging.python.org/en/latest/specifications/core-metadata/#classifier-multiple-use) of the package.
If the classifiers are found in the package upload request, the key-value pairs will be added as [annotations](https://github.com/opencontainers/image-spec/blob/main/annotations.md) (aka labels in docker terms) to the OCI image.

Note that these classifiers are case-sensitive and [non-standard](https://pypi.org/classifiers/).

For example, to [associate a package](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#labelling-container-images)
on `ghcr.io` with a repo on `github.com`, add the
`PyOCI :: Label :: org.opencontainers.image.source :: https://github.com/<org>/<repo>`
classifier to your project.
See the [examples](/AllexVeldman/pyoci/blob/main/docs/examples) for how to add classifiers to your project.

Package sub-paths
-----------------

OCI allows for images to contain paths, for example `python/team1/hello-world`.
Python does not allow for such a prefix.

To publish/use a package with a path prefix, append the path to the index url.

So to install `hello-world` as part of the `python/team1/` path in the `allexveldman` organisation on `ghcr.io`,
use `pip install --index-url="https://$GITHUB_USER:$GITHUB_TOKEN@pyoci.com/ghcr.io/allexveldman/python/team1/" hello-world`

Note that this prefix is only reflected in the OCI registry, the package itself will be installed in your python environment as just `hello-world`.

Authentication
--------------

Pip's [Basic authentication](https://pip.pypa.io/en/stable/topics/authentication/#basic-http-authentication)
is forwarded as-is to the target registry as part of the [token authentication](https://distribution.github.io/distribution/spec/auth/token/) flow.

Changing a package
------------------

PyOCI will refuse to upload a package file if the package name, version and architecture already exist.
To update an existing file, delete it first and re-publish it.

Deleting a package
------------------

There is no formal specification for deleting python packages, instead you can use the OCI registry provided methods to delete your package.

PyOCI also supports deleting a package file using `DELETE /<registry>/<namespace>/<package-name>/<filename>`, support depends on the
underlying registry's support for the [content management](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#content-management)
section of the OCI Distribution specification.

Renovate + ghcr.io
------------------

As PyOCI acts as a private pypi index, Renovate needs to be configured to use credentials for your private packages
(<https://docs.renovatebot.com/getting-started/private-packages/>).

To prevent having to check-in [encrypted secrets](https://docs.renovatebot.com/getting-started/private-packages/#encrypting-secrets)
you can:

1. Self-host renovate as a github workflow
2. Set `package: read` permissions for the workflow
3. Pass the `GITHUB_TOKEN` as an environment variable to Renovate
4. Add a hostRule for the Renovate runner to apply basic auth for pyoci using the environment variable
5. In the [package settings](https://docs.github.com/en/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility#ensuring-workflow-access-to-your-package) of the private package give the repository running renovate `read` access.

Note that at the time of writing, [GitHub App Tokens can't be granted `read:package` permissions](https://github.com/orgs/community/discussions/24636),
this is why you'll need to use the `GITHUB_TOKEN`.

`.github/workflows/renovate.yaml`

```
...
concurrency:
  group: Renovate

# Allow the GITHUB_TOKEN to read packages
permissions:
  contents: read
  packages: read

jobs:
  renovate:
    ...
      - name: Self-hosted Renovate
        uses: renovatebot/github-action@v40.2.4
        with:
          configurationFile: config.js
          token: '${{ steps.get_token.outputs.token }}'
        env:
          RENOVATE_PYOCI_USER: pyocibot
          RENOVATE_PYOCI_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

`config.js`

```
module.exports = {
  ...
  hostRules: [
    {
      matchHost: "pyoci.com",
      hostType: "pypi",
      username: process.env.RENOVATE_PYOCI_USER,
      password: process.env.RENOVATE_PYOCI_TOKEN
    },
  ],
};
```

Contributing
------------

See the [contributing](/AllexVeldman/pyoci/blob/main/CONTRIBUTING.md)
