# lnyousif.github.io app-ops

`app-ops.json` defines native application operations. Forgelet owns job execution;
Groma uses the same runner. The pinned tool versions are in `toolchain.json`.

```sh
forgelet job run validate
groma job run validate
```

Sibling-checkout launchers are also available under `scripts`.

This remains a native Jekyll/GitHub Pages site. Build/test jobs require Ruby and the gems from `Gemfile`; hosting stays with GitHub Pages. No container deployment configuration is introduced.

Jobs run only when selected. No scheduled task, deployment, or data reset is added.
