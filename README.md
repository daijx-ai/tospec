# ToSpec

Build to spec. Prove it works.

An Agent Skill for shipping exactly what the user requested—without speculative features, collateral status files, excessive safety ceremony, or commentary about work that was intentionally not done.

## Install

```bash
npx skills add daijx-ai/tospec
```

Or copy this repository into a user or project skills directory supported by your agent runtime.

## What it enforces

- smallest task-complete change;
- one observable target or a request-scoped target matrix at the accepted fidelity;
- an artifact admission gate before touching extra files;
- basic safe defaults without speculative production hardening;
- reuse of still-valid checkpoints instead of replaying completed gates;
- continued progress across ready, authorized matrix items without promoting a slice or delegated Lane to whole-task completion;
- separation of evaluator-only delivery material from the real user's task path unless the request or Contract says otherwise;
- verification that can falsify the changed behavior;
- an explicitly required integrity check or consumer readback before a destructive write, rather than only a final-state test afterward;
- concise progress and final reporting;
- a hard stop when the frozen result is complete, blocked or approval-bound, or reaches an explicit task or budget boundary.

The skill keeps higher-priority authorization and safety gates for external, destructive, credential, production, permission, payment, and irreversible actions.

## Evidence boundary

Development canaries covered a one-line change, fake-data input validation, a bounded role/tenant authorization change, CI configuration, a missing-target failure branch, a correct read-only non-trigger, and a conflicting TLS test. The skill kept edits inside the requested implementation file, preserved validation and authorization rejection paths, avoided collateral status/docs work, stopped without inventing a missing path, and rejected a test that required disabling a declared security boundary.

On the bounded authorization canary, the observed context reduction also depended on a short mechanical Codex workflow router. Installing this repository installs the Skill only; it does not rewrite global Agent rules. See [the optional Codex integration example](examples/codex-integration.md) if your runtime currently reads a large SOP for every task.

The optional integration includes a standard-library validator that enforces the one-way invariant `inline Light => router §0 Light`.

## Usage

Automatic invocation is enabled. It can also be invoked explicitly:

```text
$tospec implement this request with the smallest sufficient change
```

## License

MIT
