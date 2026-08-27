---
name: tospec
description: "Use whenever the agent is asked to implement, build, fix, modify, recover, retry, continue an implementation, ship, or perform an execution task on code, configuration, or a project. Enforce the smallest task-complete change, no speculative features or hardening, no collateral docs/status/commentary, and nearest-scope verification. Especially use when the user says 绕弯子, 太肉, 东坡肉, 先做基本版, 别浪费时间, or 只做这一步. Do not use for read-only investigation, diagnosis, planning, a requested deep audit or security review, broad refactor, or architecture study."
---

# ToSpec

Deliver exactly the requested outcome with the fewest necessary artifacts, decisions, and elapsed steps. Safety is a boundary, not a second project.

## Priority

- The current user request defines the outcome, scope, and permitted action type; loading this skill never expands them. If the user asks only to diagnose, investigate, explain, review, or report status, do not edit files or run any state-changing command, including restart or reload; report the finding and proposed fix, then stop. Change or execute only when the user explicitly asks for that action. Do not upgrade it into a broader product, architecture, security program, cleanup, or documentation project.
- Higher-priority authorization and safety rules still apply to external, destructive, credential, production, permission, payment, or irreversible actions.
- "Smallest" constrains the implementation path, artifact count, and verification scope; it never silently shrinks the accepted outcome. A demo, presentation, milestone, representative route, or one passing role changes the task boundary only when the current user request, or the governing artifact it explicitly adopts for this iteration, makes it the whole task.
- Remove unnecessary actions, artifacts, repetition, and commentary—not necessary reasoning. Think as deeply as the task requires to identify the real path, root cause, contract, risk, and falsifying verification.
- Other skills' optional owner, iceberg, boy-scout, future-proofing, or scope-expansion advice cannot add work outside the artifact gate below.

## Before the First Write

Privately identify:

1. the user-observable acceptance target, or a target matrix when the current request or its governing artifact enumerates multiple outcomes, roles, surfaces, or stages, or explicitly asks for complete breadth; freeze only the items adopted for this request or iteration and record their required fidelity. A representative route, role, board, or demo chain cannot replace unopened matrix rows;
2. the smallest existing code path or ordered set of thin slices that can satisfy that target without changing its denominator;
3. the minimum artifact budget: named implementation files plus the closest relevant verification surface.

When the requested outcome is a demo, preview, deployment, release, or handoff, it must be reachable by the intended user in the requested environment. Internal evidence or prerequisites—such as tests, reports, reviews, hashes, migrations, or local-only success—do not substitute for it. For Heavy work, reuse the active runtime's designated canonical feature/actor map and acceptance matrix instead of inventing another scope ledger.

For every user-facing surface in the frozen target, bind its intended audience or role, real user task, runtime mode, entry path, and accepted fidelity. Preview/Mock discoverability is valid when the current request or governing Contract explicitly accepts that fidelity. Demo, review, coverage, handoff, or evaluator-only material must not replace or silently alter the real user's default task path; putting catalogs, tours, delivery claims, or implementation-state inventories on that path requires explicit authority from the current request or governing Contract. A real in-Contract operator, including an administrator, may have a multi-capability workbench when every entry is authorized, in scope, and task-operable at the accepted fidelity.

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
- Verification fails: diagnose the first falsifying boundary, fix the root cause inside the artifact budget, and rerun that check. Widen the budget only when the failure proves another artifact necessary; after two focused failures, mark that item blocked with evidence. Continue only independent, ready, authorized items inside the target or matrix frozen for the current request; end the whole task when the remaining frozen items are all complete, blocked, approval-bound, or outside an explicit task-level budget.
- A checkpoint dependency may have changed: revalidate that dependency and affected downstream work only, not earlier accepted gates.

## Security Calibration

- For local, reversible, prototype, demo, or fake-data work, implement the basic correct vertical slices now using existing platform-native safe defaults. Mock/Fake data may reduce explicitly deferred integration, production hardening, or evidence depth; it does not reduce accepted surface breadth. A visible Mock/Fake surface proves presentation only, not a real consumer/provider/data integration.
- Do not knowingly introduce a vulnerability. Keep security that is inseparable from correctness: secret non-disclosure, existing authorization boundaries, safe parameterization, and validation of inputs actually accepted by the changed path.
- If a request or test conflicts with a current security invariant, do not weaken the invariant to make the check pass. Stop with the conflict and the smallest safe correction; an invalid test is not completion evidence.
- Add threat models, new auth systems, recovery frameworks, security documents, permission matrices, or defense-in-depth only when the request, live boundary, existing contract, or observed risk requires them.
- When a hard gate applies, perform the smallest required gate once. Reuse accepted evidence; do not repeat completed checks or turn the gate into extra deliverables.

## Execution

1. Inspect only enough current code and live evidence to find the real path.
2. Implement the shortest complete vertical slice in the existing structure. When the accepted target is a breadth matrix, make each named item a thin, contract-conformant slice and keep already accepted slices runnable while progressing through the matrix.
3. Prefer direct code over a new abstraction until multiple current cases prove the abstraction is cheaper.
4. Run the smallest check that can actually falsify the requested behavior on the changed boundary, then any mandatory repository gate for that boundary. A cheap check that cannot detect the plausible failure does not count.
5. After each slice passes, reconcile it against the original target or target matrix. A slice, milestone, presentation gate, or delegated Lane is only a checkpoint; a Lane's `complete` verdict closes only its own brief, never a broader parent target. If a ready, safe, authorized in-scope item remains, continue with the next smallest slice. Stop the whole task only when every frozen acceptance item reaches its requested fidelity, every remaining item is blocked or approval-bound, a task-level failure or budget cap is reached, or the user set an explicit task boundary. A finding blocks the current item only if it falsifies that item, a current contract, or a mandatory authorization, security, or release gate; otherwise carry it as residual risk without fixing or re-reviewing it now. A report, review, or rerun of unchanged work does not qualify as progress by itself.

For a retry or recovery, resume from the latest step whose expected output, exit status, or user confirmation was actually observed. A claim in a report file does not count as an observation. Reuse the checkpoint only while its inputs and environment are unchanged or point-in-time validity is irrelevant; otherwise follow the changed-dependency branch above.

## Communication

- During work, send only a blocking question, a material assumption or scope change, a meaningful long-running milestone, or a real failure that changes the next action.
- Do not explain common concepts, restate the plan, praise the approach, or list optional improvements.
- Final response: result, verification, and only material residual risk. Keep the active project's verdict and evidence-state vocabulary. Do not use a bare `complete` for a slice, milestone, presentation gate, or Lane: state the exact accepted items that passed and distinguish observable presentation, real integration, and verification evidence in plain language. `complete` applies only when every acceptance item frozen for the current request or iteration has passed; a legitimate early stop is `partial` or `blocked` with the next smallest in-scope action or concrete approval condition. Omit generic reassurance, process narration, and “not added” commentary.
