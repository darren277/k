#!/usr/bin/env bash

# Aliases to shorten common kubectl commands

## Basic 'kubectl' shortcut
alias k='kubectl'

## Common resource getters
alias kg='kubectl get'
alias kgpo='kubectl get pod'
alias ksysgpo='kubectl --namespace=kube-system get pod'

## Deletion shortcuts
alias krm='kubectl delete'
alias krmf='kubectl delete -f'
alias krming='kubectl delete ingress'
alias krmingl='kubectl delete ingress -l'
alias krmingall='kubectl delete ingress --all-namespaces'

## Service getters with various output/watch combos
alias kgsvcoyaml='kubectl get service -o=yaml'
alias kgsvcwn='kubectl get service --watch --namespace'
alias kgsvcslwn='kubectl get service --show-labels --watch --namespace'

## Watch a file-based manifest
alias kgwf='kubectl get --watch -f'


# How to use: `source ./kube_aliases.sh`.
