# Optional Codex integration

`lean-delivery` is standalone for clearly Light implementation work. A Codex setup that currently mandates reading a long collaboration SOP for every non-Light task can pair it with a short canonical router.

This is an integration pattern, not an installer. Do not overwrite an existing global workflow without reviewing its authorization, deployment, credential, destructive-action, and verification gates.

The tested pattern keeps the canonical entry short and moves detailed workflow sections behind explicit triggers:

- Light tasks use the Skill's inline criteria and do not open the SOP.
- A bounded authorization/security change uses a fast path only when one existing enforcement function, current contract, allow/deny tests, local reversibility, and no schema/runtime/external/cross-layer change are all proven.
- Any unknown condition returns to normal Heavy.
- Normal Heavy opens only the exact detailed section required by the current phase.

Relevant global entry shape:

```markdown
- If `lean-delivery` is loaded and all inline Light conditions hold, use them as conservative sufficient conditions for Light without opening the SOP; inline Light must imply router §0 Light.
- Heavy classification determines risk coverage; it does not by itself require cross-project memory, a whole-SOP read, todo artifacts, or multi-Agent orchestration.
- A bounded Heavy fast path may skip those costs only when every eligibility condition is proven; otherwise read the exact normal-Heavy sections required by current evidence.
```

The local canary that motivated this pattern retained same-tenant allow, wrong-role deny, cross-tenant deny, and missing-resource behavior while avoiding the detailed SOP and cross-project memory. That is one bounded case, not proof that every Heavy task should take the fast path.

Validate the one-way Light invariant after changing either text:

```bash
python3 scripts/validate_light_tiering.py \
  --skill SKILL.md \
  --router /path/to/programming-collaboration-workflow.md \
  --global-entry /path/to/AGENTS.md
```
