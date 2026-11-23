---
id: breuil-kisin-lattice-stable-and-hodge-tate-jumps
title: The monodromy of a Breuil-Kisin module and its Hodge-Tate jumps (statement)
kind: theorem
decl: GlobalTheory.T.breuilKisin_lattice_stable_and_hodgeTate_jumps
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.BreuilKisinLatticeStableAndHodgeTateJumpsStatement
covers: 346
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`ENStable_and_jumps`](/entry/enstable-and-jumps/). Step 5 of [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/) calls it to get the condition `EN_mem` of a pack and, with the jump part of `IsGood`, that the jumps of the Breuil-Kisin module lie in $U$. The statement and its proof are in the entry for `ENStable_and_jumps`.

## Statement

The statement is word for word that of [`ENStable_and_jumps`](/entry/enstable-and-jumps/). In short: assume `FontaineBcris` and $\ell \ne 2$. Let $P$ be a $\varphi$-module identified with a lattice $T$ of $G_{\mathbb{Q}_\ell}$, over Witt vectors and over the crystalline period ring, compatibly and with horizontal vectors fixed by $G_{K_\varpi}$. Then $E N$ maps the lattice $M$ of $P$ into its extension to series that converge on $|X| \le |\ell|^{1/e}$, and the jumps of $P$ lie in each set that contains the Hodge-Tate jumps of $T$.

## Proof

The proof is one line, `exact @GlobalTheory.NgalFil.ENStable_and_jumps`. It passes all hypotheses along.

## In the Lean code

The theorem is in [BreuilKisinLatticeStableAndHodgeTateJumpsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BreuilKisinLatticeStableAndHodgeTateJumpsStatement.lean#L10). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)` with `ENStable_and_jumps` in each slot, under `maxHeartbeats 1000000`.
