---
id: es-vanish
title: An Euler system class kills the Bloch-Kato Selmer group
kind: theorem
decl: GlobalTheory.Ord2.es_vanish
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.LocPublishedOfLitCoh
covers: 877
status: drafted
drafted_by: writer@claude
---
This theorem shows that a representation $W$ in the ordinary normal form with an Euler system class has a zero Bloch-Kato Selmer group. [The vanishing theorem for an ordinary source](/entry/vanish-ord-l-of-zeta-ur/) applies it to the normal form that it builds. The proof passes through three Selmer groups: the strict one of the Tate dual, the ordinary one of the dual, and the ordinary one of $W$. Then it compares the Bloch-Kato condition with the ordinary condition.

## Statement

Let $\ell$ be a prime, $e \in \mathbb{N}$, $S$ a finite set of places, $A$ a place of $\overline{\mathbb{Q}}$ above $\ell$, and $W \colon G_\mathbb{Q} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$. The conditions $\mathrm{Nf}(e, S, A, W)$ and $\mathrm{ES}(W, A)$ are those of [the zeta element theorem](/entry/zeta-ur/). Let $W^* = W \otimes \bar\chi(\det W)^{-1}$, with $\bar\chi$ the [[cyclotomic character|XSGB5K2KEG]]. $\mathrm{StrZero}(V, A)$ and $\mathrm{GrZero}(V, A)$ say that every cocycle of $V$ that is unramified at all primes $w \ne \ell$ and is a coboundary on the decomposition group at $A$ (strict), or ordinary at $A$ (Greenberg), is a coboundary. [The entry for `grZero_of_grZero_dual1`](/entry/gr-zero-of-gr-zero-dual1/) defines them in full.

**Theorem.** Assume $\mathrm{LitCoh}$, the literature statements on [[Galois cohomology|9MPCZ3EAJM]]. If $\mathrm{Nf}(e, S, A, W)$ and $\mathrm{ES}(W, A)$ hold, then every Bloch-Kato cocycle of $W$ is a coboundary.

## Proof

1. [`strict_vanishing_dual_of_literature`](/entry/strict-vanishing-dual-of-literature/): the Euler system class gives $\mathrm{StrZero}(W^*, A)$.
2. `ordinarySelmer_dual_vanishes_of_strict` upgrades it to $\mathrm{GrZero}(W^*, A)$. It uses $\mathrm{ES}$ again.
3. [`ordinarySelmer_vanishes_of_dual_vanishes`](/entry/ordinary-selmer-vanishes-of-dual-vanishes/) gives $\mathrm{GrZero}(W, A)$.
4. `blochKato_cocycle_unramified_and_greenbergOrdinary`: each Bloch-Kato cocycle of $W$ is unramified away from $\ell$ and ordinary at $A$. Its input is the structure $\mathrm{LocalPublishedTheorems}$, which `localGaloisCohomology_of_galoisCohomology` fills with 7 of the 12 fields of $\mathrm{LitCoh}$ (`LocalFiniteness`, `LocalTateDuality` and `LocalEulerChar`, each with its `K` version, and `BlochKatoLocal`).
5. So by step 3 each Bloch-Kato cocycle is a coboundary.

## In the Lean code

The theorem is in [LocPublishedOfLitCoh.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/LocPublishedOfLitCoh.lean#L16), with `localGaloisCohomology_of_galoisCohomology` at line 13. $\mathrm{Nf}$, $\mathrm{ES}$, $\mathrm{StrZero}$, $\mathrm{GrZero}$ and the twist `dual1` are in [FinalTheorems.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/FinalTheorems.lean#L24). $\mathrm{LitCoh}$ is in [Brauer.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/Brauer.lean#L105).

- `GlobalTheory.T.strict_vanishing_dual_of_literature`, a second name for `StrictKill.main`.
- `GlobalTheory.T.ordinarySelmer_dual_vanishes_of_strict`, a second name for `GlobalTheory.Ord2.Upgrade.upgrade`. We have not opened it.
- `GlobalTheory.T.ordinarySelmer_vanishes_of_dual_vanishes`, a second name for `grZero_of_grZero_dual1`.
- `GlobalTheory.T.blochKato_cocycle_unramified_and_greenbergOrdinary`, a second name for `GlobalTheory.Ord2.bk_unr_gr`. We have not opened it.

The theorem is in a file named after the helper `localGaloisCohomology_of_galoisCohomology`, not after `es_vanish`. Step 3 does not use $\mathrm{ES}$.
