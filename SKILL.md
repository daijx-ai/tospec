---
name: lean-delivery
description: "Use whenever the agent is asked to implement, build, fix, modify, recover, retry, continue an implementation, ship, or perform an execution task on code, configuration, or a project. Enforce the smallest task-complete change, no speculative features or hardening, no collateral docs/status/commentary, and nearest-scope verification. Especially use when the user says 绕弯子, 太肉, 东坡肉, 先做基本版, 别浪费时间, or 只做这一步. Do not use for read-only investigation, diagnosis, planning, a requested deep audit or security review, broad refactor, or architecture study."
---

# Lean Delivery

Deliver exactly the requested outcome with the fewest necessary artifacts, decisions, and elapsed steps. Safety is a boundary, not a second project.

## Priority

- The current user request defines the outcome and scope. Do not upgrade it into a broader product, architecture, security program, cleanup, or documentation project.
- Higher-priority authorization and safety rules still apply to external, destructive, credential, production, permission, payment, or irreversible actions.
- Other skills may improve persistence, quality, or review, but their optional owner, iceberg, boy-scout, future-proofing, or scope-expansion advice cannot add work outside this skill's artifact gate.
- A complaint about slowness or over-engineering is a signal to delete steps, not a reason to add a process report, retrospective, or more commentary.

## Before the First Write

Privately reduce the task to:

1. one observable requested outcome;
2. the smallest existing code path that can produce it;
3. the minimum artifact budget: named implementation files plus the closest relevant verification surface.

Do not narrate this reduction unless a material ambiguity blocks implementation.

Here, a clearly self-contained Light task means one requested behavior, a target path discoverable in the current repository, local reversibility, and no change to a Contract, schema, authorization boundary, persisted/shared data, runtime configuration, or external system. For such a task, do not search cross-project memory, history, ASSETS, routing maps, or unrelated status files. Do not read a long SOP end to end: load only the exact cited section needed for task tiering or verification, then return to the requested files. If any Light criterion is absent, read the relevant current project source before acting.

## Artifact Gate

Create or edit an artifact only when at least one is true:

1. it directly implements the requested behavior;
2. an existing contract must change for that behavior to work;
3. it is the closest test or verification needed to prove the behavior;
4. it cleans up something introduced by this change.

Otherwise, do not touch it. In particular:

- Do not add login, debounce, retries, caching, i18n, feature flags, plugin systems, extension points, compatibility layers, abstractions, or dependencies without a current requirement or observed failure.
- Do not create implementation reports, authorization reports, decision logs, handoffs, TODO narratives, status snapshots, checklists, or new planning files unless the user requested them or one exact canonical project contract requires that exact artifact for the completed transition.
- Do not update README, CHANGELOG, TASKS, PROGRESS, BLOCKED, status mirrors, hashes, or indexes merely because a command ran. Update one existing canonical state file only when the completed transition would otherwise leave current operational instructions materially false or unsafe; do not sync mirrors unless the user explicitly asks. Never fan one small action into several duplicate status edits.
- Do not put rejected ideas or explanations of why something was not added into code comments, docs, titles, UI copy, commit messages, or PR text.
- Do not clean up adjacent code or docs just because they are nearby.

If a new file outside the private artifact budget becomes necessary, stop for one sentence internally and admit it only through the four conditions above. Ask the user only when it materially expands scope or risk.

## Security Calibration

- For local, reversible, prototype, demo, or fake-data work, implement the basic correct vertical slice now using existing platform-native safe defaults. Do not design speculative production hardening.
- Do not knowingly introduce a vulnerability. Keep security that is inseparable from correctness: secret non-disclosure, existing authorization boundaries, safe parameterization, and validation of inputs actually accepted by the changed path.
- Add threat models, new auth systems, recovery frameworks, security documents, permission matrices, or defense-in-depth only when the request, live boundary, existing contract, or observed risk requires them.
- When a hard gate applies, perform the smallest required gate once. Reuse accepted evidence; do not repeat completed checks or turn the gate into extra deliverables.

## Execution

1. Inspect only enough current code and live evidence to find the real path.
2. Implement the shortest complete vertical slice in the existing structure.
3. Prefer direct code over a new abstraction until multiple current cases prove the abstraction is cheaper.
4. Run the smallest check that can actually falsify the requested behavior on the changed boundary, then any mandatory repository gate for that boundary. A cheap check that cannot detect the plausible failure does not count.
5. Stop when the requested outcome works and the relevant evidence passes. Do not continue improving the project.

For a retry or recovery, resume from the last accepted checkpoint. A checkpoint is the latest step whose expected output, exit status, or user confirmation was actually observed in the current task; it is not a report file and does not require creating one. Reuse it only while the inputs and environment it depended on are unchanged or its point-in-time validity is irrelevant. If evidence is missing or one dependency may have changed, revalidate only that dependency, not earlier accepted gates. Do not rewrite the story of the failure or generate a new batch of reports unless the user explicitly asks.

## Communication

- During work, send only a blocking question, a material assumption or scope change, a meaningful long-running milestone, or a real failure that changes the next action.
- Do not explain common concepts, restate the plan, praise the approach, or list optional improvements.
- Final response: result, verification, and only material residual risk. Omit rejected alternatives, generic reassurance, process narration, and “not added” commentary.

## Stop Check

Before continuing after the requested outcome is already proven, ask: “Would this next action change the user's requested result?” If no, stop.

Canonical anti-pattern: the user asks for tomato and eggs; do not add braised pork, do not rename the dish “tomato and eggs without braised pork,” and do not add a comment explaining why braised pork was omitted.
