# Utilities

## Aliases

How to use: `source ./kube_aliases.sh`.

Also, you could add this to your `~/.bashrc`:

```bash
if [ -f "/path/to/kube_aliases.sh" ]; then
    source "/path/to/kube_aliases.sh"
fi
```

For more advanced aliases, you could do something like this:

```bash
# In your kube_aliases.sh (or a separate file)
function kgs() {
  # If the first argument is 'yml', output service in YAML
  if [[ $1 == "yml" ]]; then
    kubectl get service -o=yaml
  else
    # Otherwise, just do a normal 'get service' with whatever arguments are passed
    kubectl get service "$@"
  fi
}
```

Then `kgs yml` would translate to `kubectl get service --show-labels --watch`.

Or even:

```bash
function kgs() {
  case "$1" in
    yml)
      kubectl get service -o=yaml
      ;;
    w)
      kubectl get service --watch
      ;;
    slwn)
      kubectl get service --show-labels --watch --namespace "${2:-default}"
      ;;
    *)
      # Default behavior, pass all arguments through to 'kubectl get service'
      shift
      kubectl get service "$@"
      ;;
  esac
}
```

Adding `kgs w` and `kgs slwn dev`.
