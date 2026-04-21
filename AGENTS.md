# AGENTS.md

## Project goal

Build and maintain a reusable research engine for iSite that supports:
- country-level high-value property scanning
- structured DIS recommendation logic
- public-search augmentation
- evidence grading
- proxy basis standardization
- repeatable exports

## Ground rules

- Do not present proxy inference as direct fact.
- Do not recommend DIS from a single weak source.
- Resolve entity before judging value.
- Keep cross-source conflicts visible.
- If DIS is recommended, explicitly map the deployment edge to **pRRU** or **hRRU**.
- Use **DIS (digital indoor system)** instead of `digital DAS`.
- Use **pRRU** for pure indoor environments.
- Use **hRRU** for semi-open environments.

## Working order

1. Read `skills/isite-scan/references/` before implementation.
2. Implement structured schemas first.
3. Keep source adapters abstract until a source is approved.
4. Add tests with every core module change.
5. Preserve output-field compatibility with the field dictionary.

## Done criteria

A change is not done unless:
- tests pass
- evidence / proxy fields remain structured
- DIS terminology is correct
- remote unit mapping is explicit when applicable
