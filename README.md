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

Development canaries covered a focused code change and a one-command retry: the skill loaded implicitly, kept changes inside the requested files, reused accepted evidence, and left collateral status files unchanged. These tests support the behavior but do not mechanically guarantee every future run.

## Usage

Automatic invocation is enabled. It can also be invoked explicitly:

```text
$lean-delivery implement this request with the smallest sufficient change
```

## License

MIT
