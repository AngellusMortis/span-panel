---
hide:
- navigation
---
# Command Line

The `span-panel` command is provided to give a CLI interface to interact with your SPAN Panel. All
commands support JSON output so it works great with `jq` for complex scripting.

## Authentication

Following traditional [twelve factor app design](https://12factor.net/), the preferred way to provided authentication
credentials to provided environment variables, but CLI args are also supported.

### Getting an Auth Token

Before being able to do anything, you need to get an auth token from your SPAN Panel. The `generate-token` subcommand will walk you through how.

```bash
export SPAN_HOST=http://your_span_ip

span-panel generate-token
```

### Environment Variables

```bash
export SPAN_HOST=http://your_span_ip
export SPAN_TOKEN=your_token

span-panel panel meter
```

### CLI Args

```bash
span-panel -h http://your_span_ip -t your_token panel meter
```
