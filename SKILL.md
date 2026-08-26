---
name: tospec
description: "Use whenever the agent is asked to implement, build, fix, modify, recover, retry, continue an implementation, ship, or perform an execution task on code, configuration, or a project. Enforce the smallest task-complete change, no speculative features or hardening, no collateral docs/status/commentary, and nearest-scope verification. Especially use when the user says 绕弯子, 太肉, 东坡肉, 先做基本版, 别浪费时间, or 只做这一步. Do not use for read-only investigation, diagnosis, planning, a requested deep audit or security review, broad refactor, or architecture study."
---

# ToSpec

Deliver exactly the requested outcome with the fewest necessary artifacts, decisions, and elapsed steps. Safety is a boundary, not a second project.

## Priority

- The current user request defines the outcome, scope, and permitted action type; loading this skill never expands them. If the user asks only to diagnose, investigate, explain, review, or report status, do not edit files or run any state-changing command, including restart or reload; report the finding and proposed fix, then stop. Change or execute only when the user explicitly asks for that action. Do not upgrade it into a broader product, architecture, security program, cleanup, or documentation project.
- Higher-priority authorization and safety rules still apply to external, destructive, credential, production, permission, payment, or irreversible actions.
- Remove unnecessary actions, artifacts, repetition, and commentary—not necessary reasoning. Think as deeply as the task requires to identify the real path, root cause, contract, risk, and falsifying verification.
- Other skills' optional owner, iceberg, boy-scout, future-proofing, or scope-expansion advice cannot add work outside the artifact gate below.

## Before the First Write

Privately identify:

1. one user-observable acceptance target, not an internal proxy; when the requested outcome is a demo, preview, deployment, release, or handoff, it must be reachable by the intended user in the requested environment, and internal evidence or prerequisites—such as tests, reports, reviews, hashes, migrations, or local-only success—do not substitute for it;
2. the smallest existing code path that can produce it;
3. the minimum artifact budget: named implementation files plus the closest relevant verification surface.

A clearly Light task has one requested behavior, a target discoverable in the current repository, local reversibility, and no confirmed product behavior or Contract, schema, authorization or security boundary, persisted/shared-data, global or cross-runtime rule, production/CI/release/deployment/runtime-configuration, or external-system change. Make that tiering decision from these criteria without opening a long SOP, cross-project memory, history, ASSETS, routing maps, or unrelated status files.

If any criterion is absent, uncertain, or fails, escalate once: privately name the crossed boundary; inspect the current contract, tests, and directly affected callers that govern it; and extend verification to falsify that boundary, including deny or negative cases where applicable. If the current runtime designates a tiering SOP, read only the section for the resulting tier; otherwise this escalation is complete in itself. Escalation deepens inspection and verification only; the artifact gate and communication rules are unchanged.

Do not narrate this reduction unless ambiguity materially changes scope, risk, or acceptance.

## Artifact Gate

Create or edit an artifact only when at least one is true:

1. it directly implements the requested behavior;
2. an existing contract must change for that behavior to work;
3. it is the closest test or verification needed to prove the behavior;
4. it cleans up something introduced by this change.

Otherwise, do not touch it. In particular:

- Do not add login, debounce, retries, caching, i18n, feature flags, plugin systems, extension points, compatibility layers, abstractions, or dependencies without a current requirement or observed failure.
- Do not create reports, decision logs, handoffs, TODO narratives, status snapshots, checklists, planning files, or explanations of rejected ideas unless requested or required by one exact canonical contract.
- Do not update README, CHANGELOG, TASKS, PROGRESS, BLOCKED, status mirrors, hashes, or indexes merely because a command ran. Update one canonical state file only when omission would leave current operational instructions materially false or unsafe; never fan one action into duplicate status edits.
- Do not clean up adjacent code or docs just because they are nearby.

Canonical anti-pattern: when asked for tomato and eggs, do not add braised pork, rename it “tomato and eggs without braised pork,” or add a comment explaining why pork was omitted.

## Failure Branches

- Target unresolved: search only nearby repository structure and named path references. If still unresolved, ask one blocking question and do not write or invent a path.
- Necessary context absent or a Light criterion fails: perform the escalation above once and continue under it without rewriting completed work.
- Verification fails: diagnose the first falsifying boundary, fix the root cause inside the artifact budget, and rerun that check. Widen the budget only when the failure proves another artifact necessary; after two focused failures, stop with evidence.
- A checkpoint dependency may have changed: revalidate that dependency and affected downstream work only, not earlier accepted gates.

## Security Calibration

- For local, reversible, prototype, demo, or fake-data work, implement the basic correct vertical slice now using existing platform-native safe defaults. Do not design speculative production hardening.
- Do not knowingly introduce a vulnerability. Keep security that is inseparable from correctness: secret non-disclosure, existing authorization boundaries, safe parameterization, and validation of inputs actually accepted by the changed path.
- If a request or test conflicts with a current security invariant, do not weaken the invariant to make the check pass. Stop with the conflict and the smallest safe correction; an invalid test is not completion evidence.
- Add threat models, new auth systems, recovery frameworks, security documents, permission matrices, or defense-in-depth only when the request, live boundary, existing contract, or observed risk requires them.
- When a hard gate applies, perform the smallest required gate once. Reuse accepted evidence; do not repeat completed checks or turn the gate into extra deliverables.

## Execution

1. Inspect only enough current code and live evidence to find the real path.
2. Implement the shortest complete vertical slice in the existing structure.
3. Prefer direct code over a new abstraction until multiple current cases prove the abstraction is cheaper.
4. Run the smallest check that can actually falsify the requested behavior on the changed boundary, then any mandatory repository gate for that boundary. A cheap check that cannot detect the plausible failure does not count.
5. Stop when the acceptance target works and the relevant evidence passes. A finding blocks the current milestone only if it falsifies that target, a current contract, or a mandatory authorization, security, or release gate; otherwise carry it as residual risk in the final response and wherever the current contract requires, without fixing or re-reviewing it now. Continue only when the next action changes the target, removes a demonstrated blocker, verifies a change just made, or supplies required evidence that is absent or stale. A report, review, or rerun of unchanged work does not qualify by itself.

For a retry or recovery, resume from the latest step whose expected output, exit status, or user confirmation was actually observed. A claim in a report file does not count as an observation. Reuse the checkpoint only while its inputs and environment are unchanged or point-in-time validity is irrelevant; otherwise follow the changed-dependency branch above.

## Communication

- During work, send only a blocking question, a material assumption or scope change, a meaningful long-running milestone, or a real failure that changes the next action.
- Do not explain common concepts, restate the plan, praise the approach, or list optional improvements.
- Final response: result, verification, and only material residual risk. Omit generic reassurance, process narration, and “not added” commentary.
