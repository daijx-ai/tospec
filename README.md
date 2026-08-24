# Lean Delivery

An Agent Skill for shipping exactly what the user requested—without speculative features, collateral status files, excessive safety ceremony, or commentary about work that was intentionally not done.

## Install

```bash
npx skills add daijx-ai/lean-delivery-skill
```

Or copy this repository into a user or project skills directory supported by your agent runtime.

## What it enforces

- smallest task-complete change;
- an artifact admission gate before touching extra files;
- basic safe defaults without speculative production hardening;
- reuse of still-valid checkpoints instead of replaying completed gates;
- verification that can falsify the changed behavior;
- concise progress and final reporting;
- a hard stop when the next action would not change the requested result.

The skill keeps higher-priority authorization and safety gates for external, destructive, credential, production, permission, payment, and irreversible actions.

## Evidence boundary

Development canaries covered a one-line change, fake-data input validation, a bounded role/tenant authorization change, CI configuration, a missing-target failure branch, a correct read-only non-trigger, and a conflicting TLS test. The skill kept edits inside the requested implementation file, preserved validation and authorization rejection paths, avoided collateral status/docs work, stopped without inventing a missing path, and rejected a test that required disabling a declared security boundary.

On the bounded authorization canary, the observed context reduction also depended on a short mechanical Codex workflow router. Installing this repository installs the Skill only; it does not rewrite global Agent rules. See [the optional Codex integration example](examples/codex-integration.md) if your runtime currently reads a large SOP for every task.

The optional integration includes a standard-library validator that enforces the one-way invariant `inline Light => router §0 Light`.

## Usage

Automatic invocation is enabled. It can also be invoked explicitly:

```text
$lean-delivery implement this request with the smallest sufficient change
```

## License

MIT
